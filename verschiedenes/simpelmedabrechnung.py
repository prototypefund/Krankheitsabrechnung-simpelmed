#!/usr/bin/env python3

"""SimpelMed Abrechnung Prototyp.

(C) 2024 by Berthold Gehrke <kontakt@simpelmed.de>
License: AGPL v3 or later (details at http://www.gnu.org)
"""

# Standardbibliothek
# import io
import os
import psycopg2
# import shutil
# import stat
import sys

# Dieses Programm _nicht_ als Superuser/root starten.
if os.name in ['posix'] and os.geteuid() == 0:
    print("""
Starten Sie dieses Programm nicht als Admin/root!
-------------------------------------------------
Das ist _sehr_ unsicher und kann die Datenbank beschädigen ...
Starten Sie das Programm als »normaler« Nutzer.""")
    sys.exit(1)

# print("Guten Tag aus /usr/share/gnumed/simpelmedabrechnung.py!")

HOST = 'localhost'
DATENBANK = 'gnumed_v22'
DBNUTZER = 'any-doc'
PORT = 5432
KENNWORTDBNUTZER = 'any-doc'

conn = psycopg2.connect(host=HOST,
                        database=DATENBANK,
                        user=DBNUTZER,
                        password=KENNWORTDBNUTZER)
cursor = conn.cursor()

# q124neu wird erstellt: 'Inner Join' mit drei Tabellen.
cursor.execute('TRUNCATE GKVA.q124neu;')
cursor.execute("""INSERT INTO GKVA.q124neu
               (SELECT firstnames, lastnames, dob, started, fk_patient
               FROM clin.encounter ce
               INNER JOIN
               dem.names dn
               ON
               ce.fk_patient = dn.id_identity
               INNER JOIN dem.identity
               ON
               dem.identity.pk = dn.id_identity
               WHERE active=true);""")

# Runden des Arzt-Patientinnen-Kontaktes auf das Quartal ...
cursor.execute("""UPDATE GKVA.q124neu
               SET
               quartal = date_trunc('quarter', "kontakt");""")

# ... und alle Zeilen entfernen, die nicht im gewünschten Quartal liegen.
cursor.execute("""DELETE FROM GKVA.q124neu
               WHERE quartal < '2024-01-01';""")

# Runden des Geburtstages auf den Tag ...
cursor.execute("""UPDATE GKVA.q124neu
               SET
               dob = date_trunc('day', "dob");""")

# Berechne das Alter und füge es ein: Spalte 'jahr'.
# Cave: Das Alter wird anhand der vollen Kalenderjahre berechnet,
# nicht tagesgenau, was für den Punktwert exakter ist ->
# für die Demo-Logik ausreichend, später verfeinern!
cursor.execute("""UPDATE GKVA.q124neu SET "ebm_euro_eins" \
= extract(year from "dob");""")
cursor.execute("""UPDATE GKVA.q124neu SET "ebm_ziffer_zwei" \
= extract(year from "kontakt");""")
# Lies die Abrechnungsdatei aus der Datenbank
# Gehe durch alle Zeilen und berechne die Differenz aus
# 'aktuellem Jahr' = row[10] = 'ebm_ziffer_zwei'
# (als Zwischenspeicher, wird später gelöscht und nicht nach q124 übernommen)
# und 'Geburtsjahr' = row[9] = 'ebm_euro_eins'
# (als Zwischenspeicher, dito)
# speichere die Differenz = Lebensalter mit der q124neu_id für die
# weitere Verarbeitung in einer Liste.
# Variablenbezeichner 'alterlj' und nicht 'alter', da letzteres
# ein SQL-Schlüsselwort darstellt.
altersliste = list()
cursor.execute("""SELECT * FROM gkva.q124neu;""")
for row in cursor:
    alterlj = str(int(row[10]) - int(row[9]))
    altersliste.append((alterlj, str(row[14])))
# print(altersliste)
# Füge das 'Lebensalter' in die Spalte 'jahr' ein
cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
start = 0
for row in result:
    table_modification = """UPDATE gkva.q124neu SET jahr = """\
                         + altersliste[start][0] + """ WHERE q124neu_id = """\
                         + altersliste[start][1] + """;"""
    cursor.execute(table_modification)
    start += 1
# »Aufräumen«: temporäre Spaltenwerte zurücksetzen
# Setze die Spalte ebm_euro_eins auf NULL
cursor.execute("""SELECT * FROM gkva.q124neu;""")
table_modification = """UPDATE gkva.q124neu SET ebm_euro_eins = NULL;"""
cursor.execute(table_modification)
# Setze die Spalte ebm_ziffer_zwei auf NULL
cursor.execute("""SELECT * FROM gkva.q124neu;""")
table_modification = """UPDATE gkva.q124neu SET ebm_ziffer_zwei = NULL;"""
cursor.execute(table_modification)
# Das Alter, berechnet aus Differenz »Jahr des aktuellen Quartals» und dem
# »Geburtsjahr« des Patienten (nicht taggenau!) steht nun in Spalte 'jahr'.

# Berechne Punkte und Eurowert der »Praxispauschale «aus Alter und EBM-Katalog,
# setzte die Ergebnisse ein in die Spalten ebm_punkte_eins und ebm_euro_eins.
# Dies darf allerdings nur einmal je Quartal je Patient erfolgen ->
# Mehrfacheinträge werden gelöscht, siehe # BEGIN Mehrfacheinträge entfernen

punkteliste = list()
cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
for row in result:
    # row[6] = 'jahr' = Lebensalter
    # bis zum 4. Lebensjahr laut EBM-Katalog
    if int(row[6]) < 5:
        punkte = 225
        eurowert = '2685'
    # zwischen 5. und 19. Lebensjahr
    elif int(row[6]) < 20:
        punkte = 142
        eurowert = '1695'
    # zwischen 20. und 55. Lebensjahr
    elif int(row[6]) < 56:
        punkte = 114
        eurowert = '1360'
    # zwischen 56. und 75. Lebensjahr
    elif int(row[6]) < 76:
        punkte = 148
        eurowert = '1766'
    # zwischen 76. und 120. Lebensjahr
    elif int(row[6]) < 121:
        punkte = 200
        eurowert = '2387'
    # ein Alter über 120 erzeugt einen Fehler/Abbruch
    else:
        sys.exit("Pat. älter als 120")
    pruef_schon_pauschaliert = int(row[4])  # pk_patient
    pruef_id = int(row[14])  # q124neu_id
    pruef_ergebnis = 9
    kontaktzeit = row[3]
    punkteliste.append([punkte, eurowert, pruef_schon_pauschaliert,
                        pruef_id, pruef_ergebnis, kontaktzeit])
# nur DEBUG
# print(punkteliste)

cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
start = 0
for row in result:
    table_modification = """UPDATE gkva.q124neu SET ebm_punkte_eins = """\
                         + str(punkteliste[start][0]) + \
                         """ WHERE pk_patient = """ + \
                         str(punkteliste[start][2]) + """;"""
    cursor.execute(table_modification)
    table_modification = """UPDATE gkva.q124neu SET ebm_euro_eins = """\
                         + punkteliste[start][1] + \
                         """ WHERE pk_patient = """ + \
                         str(punkteliste[start][2]) + """;"""
    cursor.execute(table_modification)
    start += 1

# BEGIN Mehrfacheinträge entfernen
# Jetzt verfügt in q124neu jede Zeile über die Einträge
# 'EBM-Pauschale-Ziffer' sowie 'Punkte' und 'Euro' dazu:
# nun werden die Mehrfacheinträge entfernt.

mehrfach_patient_list = [[item[2], item[5], item[3]] for item in punkteliste]


def erstes_element(x):
    return x[0]


mehrfach_patient_list.sort(key=erstes_element)

index_liste = list()
for lfd_nr in range(1, len(mehrfach_patient_list)):
    if mehrfach_patient_list[lfd_nr][0] == \
       mehrfach_patient_list[lfd_nr - 1][0]:
        # hier noch nach Datum ordnen!?
        # d.h., das 'jüngere' Element löschen ...
        index_liste.append(lfd_nr)

index_liste.sort(reverse=True)

for i in index_liste:
    mehrfach_patient_list.pop(i)

mehrfach_patient_list = [item[2] for item in mehrfach_patient_list]

cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
for row in result:
    if row[14] not in mehrfach_patient_list:
        table_modification = """UPDATE gkva.q124neu SET ebm_ziffer_eins \
= NULL WHERE q124neu_id = """+str(row[14])+""";"""
        cursor.execute(table_modification)

cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
for row in result:
    if row[14] not in mehrfach_patient_list:
        table_modification = """UPDATE gkva.q124neu SET ebm_punkte_eins \
= NULL WHERE q124neu_id = """+str(row[14])+""";"""
        cursor.execute(table_modification)

cursor.execute("""SELECT * FROM gkva.q124neu;""")
result = cursor.fetchall()
for row in result:
    if row[14] not in mehrfach_patient_list:
        table_modification = """UPDATE gkva.q124neu SET ebm_euro_eins = \
NULL WHERE q124neu_id = """+str(row[14])+""";"""
        cursor.execute(table_modification)

# »Aktualisierung« von q124 durch q124neu

cursor.execute("""INSERT INTO GKVA.q124
               (firstnames, lastnames, dob, kontakt, pk_patient, quartal,
               jahr, ebm_ziffer_eins, ebm_punkte_eins, ebm_euro_eins,
               ebm_ziffer_zwei, ebm_punkte_zwei, ebm_euro_zwei, fertig)
               (SELECT
               firstnames, lastnames, dob, kontakt, pk_patient, quartal,
               jahr, ebm_ziffer_eins, ebm_punkte_eins, ebm_euro_eins,
               ebm_ziffer_zwei, ebm_punkte_zwei, ebm_euro_zwei, fertig
               FROM GKVA.q124neu
               WHERE kontakt > (SELECT MAX(kontakt) FROM GKVA.q124));""")

cursor.execute("""DELETE FROM GKVA.q124
               WHERE q124_id = 1;""")

# Die drei folgenden Zeilen nur DEBUG.
# cursor.execute("""SELECT * FROM GKVA.q124neu;""")
# result = cursor.fetchall()
# print(result)

# Ergebnisse schreiben und Datenbank-Verbindung schließen.
conn.commit()
cursor.close()
conn.close()

# Eine zweite Instanz mit ggf. privilegiertem Kennwort (Chefin) starten.
os.system("python3 -m Gnumed.gnumed --skip-update-check \
--log-file='~/gkvabrechnung.log' 'gkvaChefin' &")

# Zur Eingabe und zum Vergleich der Daten eine CSV-Tabelle starten.
# Verbindungsdaten zur Datenbank:
# postgresql://127.0.0.1:5432/gnumed_v22
# any-doc
os.system("libreoffice --base ~/gnumed/simpelmed_pg.odb &")
# print("Auf Wiedersehen aus /usr/share/gnumed/simpelmedabrechnung.py!")
sys.exit()

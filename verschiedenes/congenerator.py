#!/usr/bin/env python3

"""
Erzeuge eine con-Datei aus der SimpelMed-Datenbank GKVA.q124
und schreibe diese nach ~/gnumed.

Copyright (C) 2024 by Berthold Gehrke <kontakt@simpelmed.de>
Free use of this software is granted under the terms of the
GNU Affero General Public License Version 3 or higher (GNU AGPLv3+).
Einzelheiten siehe https://www.gnu.org/licenses/agpl-3.0.en.html
"""

# Standardbibliothek
import csv
import datetime as dt
import os
import sys

# Fremdmodule
import psycopg2
from psycopg2 import Error

# Dieses Programm _nicht_ als Superuser/root starten.
if os.name in ['posix'] and os.geteuid() == 0:
    print("""
Starten Sie dieses Programm nicht als Admin/root!
-------------------------------------------------
Das ist _sehr_ unsicher und kann die Datenbank beschädigen ...
Starten Sie das Programm als »normaler« Nutzer.""")
    sys.exit(1)

# print("Guten Tag aus /usr/share/gnumed/congenerator.py!\n")

# Praxisdaten und Konstanten
ZEICHENSATZ = "4"                            # ISO-8859-15
ENTHALTENES_DATENPAKET = "1"                 # ausschließlich ADT
NBSNR = "11234567"                           # Betriebsstättennummer, fiktiv
BEZEICHNUNG_BETRIEBSSTAETTE = "Hauptstrasse"
LEBENSLANGE_ARZTNUMMER = "123456601"
ARZTTITEL = "Dr.med."
ARZT_VORNAME = "Sidney"
ARZT_NAME = "Lohmann"

# EDV-Anbieter
KBV_PRUEFNUMMER = "Y/1/2201/36/498"          # fiktiv
KV_BEZIRK = "123"                            # Bayern
SOFTWAREVERANTWORTLICHER = "SimpelMed"

# Zeitstempel für den Dateinamen und
# Erstellungsdatum für die con-Datei
zeit = dt.datetime.now()
zeitstempel = zeit.strftime("%d.%m.%Y_%H.%M")
#print(f"{zeitstempel=}")
erstellungsdatum = zeit.strftime("%d.%m.%Y")
#print(f"{erstellungsdatum=}")

# Datenbank-Nutzer und Kennwort
DATENBANK_NUTZER = "any-doc"
DATENBANBK_KENNWORT = "any-doc"
IP_ADRESSE = "127.0.0.1"
PORT = "5432"
# ENDE Praxisdaten und Konstanten

# Verbindungstest Datenbank "gnumed_v22"
# Falls beim Test erfolgreich, kann dieser
# 'try-except-finally'-Block auskommentiert werden.
##try:
##    connection = psycopg2.connect(user = DATENBANK_NUTZER,
##                                  password = DATENBANBK_KENNWORT,
##                                  host = IP_ADRESSE,
##                                  port = PORT,
##                                  database="gnumed_v22")
##    cursor = connection.cursor()
##    # DEBUG/Info: zeige Details zur PostgreSQL-Datenbank
##    print("")
##    print("PostgreSQL-Server Informationen:")
##    print(connection.get_dsn_parameters(), "\n")
##    # SQL: Versionsinfo abfragen ...
##    cursor.execute("SELECT version();")
##    # ... und ausgeben.
##    record = cursor.fetchone()
##    print("Sie sind verbunden mit:\n", record)
##    print(f"{connection=}")
##    print("")
##    postgreSQL_test_anfrage = 'SELECT lastnames FROM dem.names LIMIT 10;'
##    cursor.execute(postgreSQL_test_anfrage)
##    ergebnis = cursor.fetchall()
##    for zeile in ergebnis:
##        print(zeile)
##    print("")
##except (Exception, Error) as error:
##    print("Fehler bei der Verbindung zu PostgreSQL", error)
##finally:
##    if connection:
##        cursor.close()
##        connection.close()
##        print("PostgreSQL: Verbindung ist geschlossen.\n")


# Hole die Daten der »Abrechnungstabelle« q124.
# Jede Zeile der Liste 'ergebnis' stellt einen Datensatz dar.
global ergebnis
ergebnis = list()
def verbindung():
    global ergebnis
    try:
        connection = psycopg2.connect(user=DATENBANK_NUTZER,
                                      password=DATENBANBK_KENNWORT,
                                      host=IP_ADRESSE,
                                      port=PORT,
                                      database="gnumed_v22")
        cursor = connection.cursor()
        postgreSQL_abrechnung_holen = 'SELECT * FROM GKVA.q124;'
        cursor.execute(postgreSQL_abrechnung_holen)
        ergebnis = cursor.fetchall()
    except (Exception, Error) as error:
        print("Fehler bei der Verbindung zu PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            #print("PostgreSQL: Verbindung ist geschlossen.\n")

    ##if ergebnis:
    ##    for zeile in ergebnis:
    ##        print(zeile)
    ##    print("")

verbindung()
# Final auf '' <leerer string> setzen.
condatei_erlaeuterung = 'ja'

# Die Liste »elemente« enthält jeweils eine Zeile der con-Datei.
elemente = list()
#print(f"{ergebnis=}")
##if ergebnis:
##    for zeile in ergebnis:
##        print(zeile)
##    print("")
if condatei_erlaeuterung:
    elemente.append("8000 con0"+"                        // con-Datei")
else:
    elemente.append("8000 con0")
if condatei_erlaeuterung:
    elemente.append("8000 con0"+"                        // Erstellungsdatum")
else:
    elemente.append("9103 "+erstellungsdatum)
elemente.append("9106 "+ZEICHENSATZ)
elemente.append("9132 "+ENTHALTENES_DATENPAKET)
elemente.append("8000 besa")
elemente.append("0201 "+NBSNR)
elemente.append("0203 "+BEZEICHNUNG_BETRIEBSSTAETTE)
elemente.append("0212 "+LEBENSLANGE_ARZTNUMMER)
elemente.append("0219 "+ARZTTITEL)
elemente.append("0220 "+ARZT_VORNAME)
elemente.append("0221 "+ARZT_NAME)
elemente.append("8000 rvsa")
elemente.append("8000 adt0")
elemente.append("0105 "+KBV_PRUEFNUMMER)
elemente.append("9102 "+KV_BEZIRK)
elemente.append("0102 "+SOFTWAREVERANTWORTLICHER)
for datensatz in ergebnis:
    elemente.append("**************************")
    if condatei_erlaeuterung:
        elemente.append("8000 0101"+"                        // Satzart »Ambulante Behandlung«")
    else:
        elemente.append("8000 0101")
    elemente.append("3101 "+datensatz[1])
    elemente.append("3102 "+datensatz[0])
    elemente.append("3103 "+str(datensatz[2])[:10])
    elemente.append("--  --  --  --  --  --")
    if condatei_erlaeuterung:
        elemente.append("5000 "+str(datensatz[7])+"                      // Leistungsziffer")
    else:
        elemente.append("5000 "+str(datensatz[7]))
    if condatei_erlaeuterung:
        eurowert = str(datensatz[9])
        if eurowert == 'None':
            elemente.append("9999 *FEHLANZEIGE*               // NICHT ANGEGEBEN")
        else:
            elemente.append("9999 "+eurowert[:2]+","+eurowert[2:4]+"                      // Eurowert (inoffiziell)")
    else:
        elemente.append("9999 "+eurowert[:2]+","+eurowert[2:4])


def die_laenge(item):
    # plus 4, weil die Angabe der Länge aus drei Stellen/Bytes besteht,
    # dazu kommt die Leerstelle zum nächsten Feld.
    return len(item) + 4


# Der Dateiname der con-Datei setzt sich wie folgt zusammen:
# Zhhnnnnnnnnn_TT.MM.JJJJ_hh.mm.eee
# Z: ISO 8859-15,
# hh: enthaltene Datenpakete (ADT und/oder KADT und/oder SADT),
# hier immer »01« entsprechend ausschließlich ADT,
# nnnnnnnnn: 9-stellige Betriebsstättennummer (BSNR) der Ärztin,
# TT.MM.JJJJ_hh.mm: Zeitstempel mit Stunde und Minute,
# eee: Dateiformat; hier immer »con« als Versäumniswert.
heimatverzeichnis = os.path.expanduser('~')
with open(heimatverzeichnis+'/gnumed/Z01'+NBSNR+'_'+zeitstempel+'.CON', 'w',
          encoding='iso-8859-15') as condatei:
    for listeneintrag in elemente:
        # »zfill(3)« füllt die Zeichenkette am Anfang
        # mit Nullen auf drei Stellen.
        condatei.write(
            str(die_laenge(listeneintrag)).zfill(3)+" "+listeneintrag+"\r\n")


# Erstelle eine Übersicht im Tabellenformat und berechne eine einfache
# Abrechnungsstatistik.

# Optional: (un-)kommentiere dazu die Print-Anweisung
# Lies die Spaltennamen und zeige dies an.
# Lies die Abrechnungsdatei aus der Datenbank
connection = psycopg2.connect(user=DATENBANK_NUTZER,
                              password=DATENBANBK_KENNWORT,
                              host=IP_ADRESSE,
                              port=PORT,
                              database="gnumed_v22")
cursor = connection.cursor()
postgreSQL_abrechnung_holen = 'SELECT * FROM GKVA.q124;'
cursor.execute(postgreSQL_abrechnung_holen)
ergebnis = cursor.fetchall()

spaltennamen = []
datenzeilen = []
spaltennamen = [desc[0] for desc in cursor.description]
for row in cursor:
    datenzeilen.append(row)
print("Spaltennamen: {}\n".format(spaltennamen))

# Die Spaltennamen / - lfd. Nummern lauten wie folgt:
# firstnames / 0,
# lastnames / 1,
# dob / 2,
# kontakt / 3,
# pk_patient / 4,
# quartal / 5,
# jahr / 6,
# ebm_ziffer_eins / 7,
# ebm_punkte_eins / 8,
# ebm_euro_eins / 9,
# ebm_ziffer_zwei / 10,
# ebm_punkte_zwei / 11,
# ebm_euro_zwei / 12,
# fertig / 13,
# q124_id / 14.

# Lies nochmals die Abrechnungsdatei aus der Datenbank,
# da der obige Cursor »verbraucht« ist.
cursor = connection.cursor()
postgreSQL_abrechnung_holen = 'SELECT * FROM GKVA.q124;'
cursor.execute(postgreSQL_abrechnung_holen)
result = cursor.fetchall()
# print(result)

# ... und erzeuge daraus eine csv-Datei.
with open(heimatverzeichnis+'/gnumed/q124tabelle.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in result:
        writer.writerow(row)

with open(heimatverzeichnis+"/gnumed/q124tabelle.csv", 'r') as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    zeilennummer = 1
    # Daten sortieren nach der zweiten Spalte (Familienname)
    # alphabetisch rückwärts. Cave: Namen mit beginnendem
    # Kleinbuchstaben landen damit ganz vorn.
    sortedlist = sorted(csv_reader_object,
                        key=lambda row: row[1], reverse=True)
    for row in sortedlist:
##        print(str(zeilennummer).zfill(3),
##              f'- {row[0].rjust(15)}  {row[1].ljust(15).upper()} \
##| Termin: {row[2][:10].center(11)} | EBM_#1 {row[5].center(8)} \
##| Punkte: {row[6].center(11)} | Euro: {row[7].center(11)} \
##| EBM_#2 {row[8].center(8)} | Punkte: {row[9].center(11)} \
##| Euro: {row[10].center(11)}| fertig: {row[11].center(11)}')
        zeilennummer += 1
# print(type(sortedlist))
print(f'Anzahl Datensätze: {zeilennummer-1}')

# Mittelwert ebm_#1 bestimmen;
# cave: die Daten sind alle vom Typ 'str' -> in »float« umwandeln.
SummeEBM1 = 0.0
AnzahlEBM1 = 0
for row in sortedlist:
    if row[9]:
        SummeEBM1 += float(row[9])
        AnzahlEBM1 += 1
print(f"{SummeEBM1=}")
print(f"{AnzahlEBM1=}")
if AnzahlEBM1:
    print("Durchschnitt:", SummeEBM1/AnzahlEBM1)

connection.commit()
cursor.close()
connection.close()

# print("Auf Wiedersehen von /usr/share/gnumed/congenerator.py!")
sys.exit()

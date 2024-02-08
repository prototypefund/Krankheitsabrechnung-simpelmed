#!/usr/bin/env python3
""" Vollständiger Dump der PostgreSQL-Datenbank plus Komprimierung gzip.
    Zusätzlich werden die Einstellungen für »transaction read only«
    sowie »locale_provider« angepasst.
    Root-Rechte bzw. Postgres-Passwort erforderlich.

    Autor: Berthold Gehrke <kontakt@simpelmed.de>
    (c) 2024, Lizenz: AGPLv3
    """

import os
import re

# Eingabe- und Ausgabe-Datei, ggf. anpassen!
eingabe = '/dev/shm/volloriginal.sql'
ausgabe = '/dev/shm/vollbearbeitet.sql'
ergebnis = 'ergebnis.sql.gz'

print("Starten pg_dumpall.")
os.system("sudo -u postgres pg_dumpall -c --if-exists -U postgres > "+eingabe)
print("pg_dumpall fertig.")
print("")

# Die Eingabe-Datei wird gelesen und _nicht_ verändert.
with open(eingabe, "r") as die_eingabe:
    a = die_eingabe.read()
print("Eingabe-Datei:", eingabe)
print("Ausgabe-Datei:", ausgabe)
print("")
print("""Bearbeite die Ersetzung
      vorher - SET default_transaction_read_only TO 'on'
      nachher - SET default_transaction_read_only TO 'off';""")
a, zaehler = re.subn(r"SET default_transaction_read_only TO 'on';",
                     r"SET default_transaction_read_only TO 'off';", a)
print("")
print("Die Ersetzung wurde wie oft durchgeführt? ->", zaehler, "<- Mal.")
print("")
print("""Bearbeite die Ersetzung
      vorher - SET default_transaction_read_only = on;
      nachher - SET default_transaction_read_only = off;""")
a, zaehler = re.subn(r"SET default_transaction_read_only = on;",
                     r"SET default_transaction_read_only = off;", a)
print("")
print("Die Ersetzung wurde wie oft durchgeführt? ->", zaehler, "<- Mal.")
print("")
print("""Bearbeite die Ersetzung
      vorher - LOCALE_PROVIDER = libc
      nachher leer '' """)
a, zaehler = re.subn(r"LOCALE_PROVIDER = libc", r"", a)
print("")
print("Die Ersetzung wurde wie oft durchgeführt? ->", zaehler, "<- Mal.")
with open(ausgabe, "w") as die_ausgabe:
    die_ausgabe.write(a)
print("")
print("Anpassung des »dump.sql« abgeschlossen.")
print("")
# Die folgenden Schritte bei Bedarf auskommentieren und/oder anpassen.
os.system("gzip -7 -k "+ausgabe)
print("Komprimierung »gz« abgeschlossen.")
os.system("mv "+ausgabe+".gz ~/"+ergebnis)
os.system("rm "+ausgabe)
print("Temp. Dateien in /dev/shm gelöscht.")
os.system("chown wer:wer "+ausgabe+".gz")
print("Neuer Besitzer für die komprimierte Dumpdatei.")
print("Fertig: siehe Datei '"+ergebnis+"'.")

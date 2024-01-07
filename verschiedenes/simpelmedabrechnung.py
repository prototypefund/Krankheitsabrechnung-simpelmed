#!/usr/bin/env python3

"""SimpelMed Abrechnung Prototyp. Kann sowohl innerhalb SimpelMed
als auch 'standalone' gestartet werden.

(C) 2024 by Berthold Gehrke <kontakt@simpelmed.de>
License: AGPL v3 or later (details at http://www.gnu.org)
"""

# standard library
import sys
import os
import psycopg2

import shutil
import stat
import io


# Dieses Programm niemals als importiertes Modul ...
##if __name__ != "__main__":
##    print("Starten Sie dieses Programm nicht innerhalb eines anderen!")
##    print("----------------------------------------------------------")
##    sys.exit(1)

# ... und auch nicht als Superuser/root starten!
##if os.name in ['posix'] and os.geteuid() == 0:
##    print("""
##Starten Sie dieses Programm nicht als Admin/root!.
##-------------------------------------------------
##Das ist _sehr_ unsicher und kann die Datenbank beschädigen ...
##Starten Sie das Programm als »normaler« Nutzer.""")
##    sys.exit(1)

print("Guten Tag aus /usr/share/gnumed/simpelmedabrechnung.py!")

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

cursor.execute('TRUNCATE GKVA.q124neu;')
cursor.execute("""INSERT INTO GKVA.q124neu
               (SELECT firstnames, lastnames, started, fk_patient
               FROM clin.encounter ce
               INNER JOIN
               dem.names dn
               ON
               ce.fk_patient = dn.id_identity WHERE active=true);""")

cursor.execute("""UPDATE GKVA.q124neu
               SET
               quartal = date_trunc('quarter', "kontakt");""")

cursor.execute("""DELETE FROM GKVA.q124neu
               WHERE quartal < '2024-01-01';""")

cursor.execute("""INSERT INTO GKVA.q124
               (lastnames, names, kontakt, pk_patient, quartal)
               (SELECT lastnames, names, kontakt, pk_patient, quartal
               FROM GKVA.q124neu
               WHERE kontakt > (SELECT MAX(kontakt) FROM GKVA.q124));""")

cursor.execute("""DELETE FROM GKVA.q124
               WHERE test_id = 1;""")

cursor.execute("""SELECT * FROM GKVA.q124neu;""")

result = cursor.fetchall()
print(result)

conn.commit()
cursor.close()
conn.close()
#print("Auf Wiedersehen aus /usr/share/gnumed/simpelmedabrechnung.py!")
os.system('simpelmed gkvaChefin')

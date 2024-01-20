#!/usr/bin/env python3

"""
SimpelMed: Dateien der GNUmed-Installation
ersetzen bzw. umbenennen und die notwendigen
SQL-Befehle einspielen.

root / su  / sudo erforderlich

Procedere:
»simpelmed_install.zip«
herunterladen und in (beliebiges) Verzeichnis entpacken.
In dieses Verzeichnis wechseln.
sudo python3 ./simpelmed_install.py

Alle benötigten Dateien sollen in einem Verzeichnis liegen.
Die zip-Datei enthält folgende Dateien, hier mit vollem Pfad
unterhalb der Wurzel einer Standardinstallation zur Info;
im Archiv natürlich nur der Basis-Name.

simpelmed_install.py (diese Datei)
/usr/share/gnumed/simpelmedabrechnung.py (Start-Script)
/usr/share/gnumed/bitmaps/simpelmed.png (Logo SimpelMed)
/usr/share/gnumed/Gnumed/gnumed.py
/usr/share/gnumed/Gnumed/humblewx.py
/usr/share/gnumed/Gnumed/business/gmPraxis.py
/usr/share/gnumed/Gnumed/wxpython/gmGuiMain.py
/usr/share/gnumed/Gnumed/wxpython/gmAuthWidgets.py
/usr/share/gnumed/Gnumed/wxpython/gmMedicationWidgets.py
/usr/share/gnumed/Gnumed/wxpython/gmGKVAbrechnungWidgets.py
/usr/share/gnumed/Gnumed/wxpython/gui/gmGKVAbrechnungPlugin.py
/usr/bin/simpelmed (Start-Script)
/home/<user>/gnumed/simpelmed_pg.odb

init_simpelmed_db.sql
q124_ebm.sql

(c) 2024 by Berthold Gehrke <kontakt@simpelmed.de>
AGPLv3 or higher
"""

import os
import shutil
import sys

if not (os.access('/usr/bin', os.F_OK | os.W_OK) and
        os.access('/usr/share/gnumed', os.F_OK | os.W_OK)):
    sys.exit("Abbruch -> Admin/root/sudo-Rechte erforderlich!")


def sicherkopie(datei):
    """ Beispiel: xyz.py wird zu xyz_py.ori"""
    if os.access(datei, os.F_OK):
        os.rename(datei, (lambda datei: datei[:-3])(datei)+'_py.ori')
    else:
        print("Fehler?! Konnte keine Kopie erstellen:", datei)


# DATEI_TUPEL[2] = 1 -> Sicherkopie ja
# DATEI_TUPEL[2] = 0 -> Sicherkopie nein
DATEI_TUPEL = (
    ('./gnumed.py', '/usr/share/gnumed/Gnumed/gnumed.py', 1),
    ('./humblewx.py', '/usr/share/gnumed/Gnumed/humblewx.py', 0),
    ('./gmPraxis.py', '/usr/share/gnumed/Gnumed/business/gmPraxis.py', 1),
    ('./gmGuiMain.py', '/usr/share/gnumed/Gnumed/wxpython/gmGuiMain.py', 1),
    ('./gmAuthWidgets.py',
     '/usr/share/gnumed/Gnumed/wxpython/gmAuthWidgets.py', 1),
    ('./gmMedicationWidgets.py',
     '/usr/share/gnumed/Gnumed/wxpython/gmMedicationWidgets.py', 1),
    ('./gmGKVAbrechnungWidgets.py',
     '/usr/share/gnumed/Gnumed/wxpython/gmGKVAbrechnungWidgets.py', 0),
    ('./gmGKVAbrechnungPlugin.py',
     '/usr/share/gnumed/Gnumed/wxpython/gui/gmGKVAbrechnungPlugin.py', 0),
    ('./simpelmedabrechnung.py',
     '/usr/share/gnumed/simpelmedabrechnung.py', 0),
    ('./simpelmed.png', '/usr/share/gnumed/bitmaps/simpelmed.png', 0),
    ('./simpelmed', '/usr/bin/simpelmed', 0),)

for item in DATEI_TUPEL:
    if item[2] == 1:
        sicherkopie(item[1])
    shutil.copyfile(item[0], item[1])

# Ausführungsrechte gewähren
os.chmod('/usr/bin/simpelmed', 0o755)
os.chmod('/usr/share/gnumed/simpelmedabrechnung.py', 0o755)

loginuser = os.getlogin()
shutil.copyfile('./simpelmed_pg.odb',
                '/home/'+loginuser+'/gnumed/simpelmed_pg.odb')

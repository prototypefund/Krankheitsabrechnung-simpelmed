-- Aus einer 'gnumed-' wird eine 'simpelmed-Datenbank':
-- Schema GKVA (steht für GKV-Abrechnung) erstellen und 
-- entsprechende leere Tabellen fuer das 1.Quartal/24
-- einfügen. Der EBM-Katalog wird in einer eigenen Datei
-- bereitgestellt 'q124_ebm.sql'.

\c gnumed_v22;

DROP TABLE IF EXISTS GKVA.q124;
DROP TABLE IF EXISTS GKVA.q124neu;
DROP TABLE IF EXISTS GKVA.q124ebm;
DROP SCHEMA IF EXISTS GKVA;
CREATE SCHEMA GKVA;

-- »dob« = 'day of birth';
-- »kontakt« = 'APK' Arzt-Patienten-Kontakt
-- = persönliche Vorstellung in der Praxis.
CREATE TABLE IF NOT EXISTS GKVA.q124 (
   firstnames VARCHAR ( 50 ) NOT NULL,
   lastnames VARCHAR ( 50 ) NOT Null,
   dob TIMESTAMP NOT NULL,
   kontakt TIMESTAMP NOT NULL,
   pk_patient SMALLINT,
   quartal TIMESTAMP,
   jahr SMALLINT,
   ebm_ziffer_eins SMALLINT DEFAULT 030000,
   ebm_punkte_eins SMALLINT,
   ebm_euro_eins FLOAT,
   ebm_ziffer_zwei SMALLINT,
   ebm_punkte_zwei SMALLINT,
   ebm_euro_zwei FLOAT,
   fertig SMALLINT,
   q124_id SERIAL PRIMARY KEY
);

-- Dummy-Eintrag. Wird entfernt, sobald das erste Mal
-- 'GKVAbrechnung' aufgerufen wird.
INSERT INTO GKVA.q124(firstnames, lastnames, dob, kontakt) VALUES
  ('Petronella-Marianne', 'Gibtesnicht', '1999-09-09', '2024-01-01');
UPDATE GKVA.q124 SET quartal = date_trunc('quarter', "kontakt");

-- Die Tabelle GKVA.q124neu hat außer q124_id / q124neu_id die  
-- identische Signatur wie q124. Diese Tabelle wird temporär benötigt
-- zur Aktualisierung von q124, falls neue Patientinnen dazukommen.
CREATE TABLE IF NOT EXISTS GKVA.q124neu (
   firstnames VARCHAR ( 50 ) NOT NULL,
   lastnames VARCHAR ( 50 ) NOT Null,
   dob TIMESTAMP NOT NULL,
   kontakt TIMESTAMP NOT NULL,
   pk_patient SMALLINT,
   quartal TIMESTAMP,
   jahr SMALLINT,
   ebm_ziffer_eins SMALLINT DEFAULT 030000,
   ebm_punkte_eins SMALLINT,
   ebm_euro_eins FLOAT,
   ebm_ziffer_zwei SMALLINT,
   ebm_punkte_zwei SMALLINT,
   ebm_euro_zwei FLOAT,
   fertig SMALLINT,
   q124neu_id SERIAL PRIMARY KEY
);

ALTER SCHEMA GKVA OWNER TO "any-doc";
ALTER TABLE GKVA.q124 OWNER TO "any-doc";
ALTER TABLE GKVA.q124neu OWNER TO "any-doc";

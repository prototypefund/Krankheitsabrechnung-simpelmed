-- Aus einer 'gnumed-' wird eine 'simpelmed-Datenbank':
-- Schema GKVA (steht für GKV-Abrechnung) erstellen und 
-- entsprechende leere Tabellen fuer das 1.Quartal/24
-- einfügen. Der EBM-Katalog wird in einer eigenen Datei
-- bereitgestellt 'q124_ebm.sql'.

\c gnumed_v22;

DROP TABLE IF EXISTS GKVA.q124;
DROP TABLE IF EXISTS GKVA.q124neu;
DROP SCHEMA IF EXISTS GKVA;

CREATE SCHEMA GKVA;

CREATE TABLE IF NOT EXISTS GKVA.q124 (
   lastnames VARCHAR ( 50 ) NOT NULL,
   names VARCHAR ( 50 ) NOT Null,
   kontakt TIMESTAMP NOT NULL,
   pk_patient SMALLINT,
   quartal TIMESTAMP,
   ebm_ziffer_eins SMALLINT,
   ebm_ziffer_zwei SMALLINT,
   fertig SMALLINT,
   q124_id SERIAL PRIMARY KEY
);

-- Dummy-Eintrag. Wird entfernt, sobald das erste
-- mal 'GKVAbrechnung' aufgerufen wird.

INSERT INTO GKVA.q124(lastnames, names, kontakt) VALUES
  ('Gibtesnicht', 'Petronella-Marianne', '2024-01-01');
UPDATE GKVA.q124 SET quartal = date_trunc('quarter', "kontakt");

-- Die Tabelle GKVA.q124neu hat außer q124_id die  
-- identische Signatur wie q124. Temporär benötigt
-- zur Aktualisierung von q124 (wenn neue Pat. dazukommen)

CREATE TABLE IF NOT EXISTS GKVA.q124neu (
   lastnames VARCHAR ( 50 ) NOT NULL,
   names VARCHAR ( 50 ) NOT Null,
   kontakt TIMESTAMP NOT NULL,
   pk_patient SMALLINT,
   quartal TIMESTAMP,
   ebm_ziffer_eins SMALLINT,
   ebm_ziffer_zwei SMALLINT,
   fertig SMALLINT,
   test_id SMALLINT
);


ALTER SCHEMA GKVA OWNER TO "any-doc";
ALTER TABLE GKVA.q124 OWNER TO "any-doc";
ALTER TABLE GKVA.q124neu OWNER TO "any-doc";


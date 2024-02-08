-- Tabelle »EBM-Katalog« im Schema GKVA (GKV-Abrechnung) erstellen,
-- gültig für das Q1 2024.
-- Es handelt sich um eine Demo. 

\c gnumed_v22;

DROP TABLE IF EXISTS GKVA.q124ebm;

CREATE TABLE IF NOT EXISTS GKVA.q124ebm (
   ebmziffer VARCHAR ( 50 ) NOT NULL,
   ebmpunkte VARCHAR ( 20 ) NOT NULL,
   ebmeuro VARCHAR ( 20 ) NOT NULL,
   ausschluss_sitzung VARCHAR ( 100 ),
   ausschluss_behfall VARCHAR ( 100 ),
   ebmlegende VARCHAR ( 500 ) NOT Null,
   kommentar VARCHAR ( 200 ),
   q124ebm_id SERIAL PRIMARY KEY
);

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (030000, 123, '26,85', '01436', '01600, 01601, 01610, 03030', 'Versichertenpauschale bis zum vollendeten 4. Lebensjahr', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (030000, 142, '16,95', '01436', '01600, 01601, 01610, 03030', 'Versichertenpauschale ab Beginn des 5. bis zum vollendeten 18. Lebensjahr', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (030000, 114, '13,60', '01436', '01600, 01601, 01610, 03030', 'Versichertenpauschale ab Beginn des 19. bis zum vollendeten 54. Lebensjahr', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (030000, 148, '17,66', '01436', '01600, 01601, 01610, 03030', 'Versichertenpauschale ab Beginn des 55. bis zum vollendeten 75. Lebensjahr', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (030000, 200, '23,87', '01436', '01600, 01601, 01610, 03030', 'Versichertenpauschale ab Beginn des 76. Lebensjahres', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (01436, 18, '2,15', '03000, 03030, 04000, 04030, 30700, 37706', '-', 'Konsultationspauschale', '-');

INSERT INTO GKVA.q124ebm (ebmziffer, ebmpunkte, ebmeuro, ausschluss_sitzung, ausschluss_behfall, ebmlegende, kommentar)
VALUES (01601, 108, '12,89', '31010, 31011, 31012, 31013', '01793, 01794, 01841, 03000, 03030, 04000, 04030, 25213, 25214, 30700, 34810, 34820, 34821, 37706', 'Individueller Arztbrief', '-');

ALTER TABLE GKVA.q124ebm OWNER TO "any-doc";

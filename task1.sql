DROP TABLE IF EXISTS pets;
CREATE TABLE pets(type TEXT, name TEXT, age INTEGER, sex TEXT);
INSERT INTO pets VALUES('cat', 'Daisy', 3, 'female');
INSERT INTO pets VALUES('cat', 'Dave the magical cheese wizard', 2, 'male');
INSERT INTO pets VALUES('dog', 'July', 8, 'female');
INSERT INTO pets VALUES('dog', 'Ray', 9, 'male');

SELECT * FROM pets;

ALTER TABLE pets 
ADD COLUMN weight INTEGER 
DEFAULT 'unknown';

UPDATE pets
SET age = 4
WHERE name = 'Daisy';

DELETE FROM pets
WHERE name = 'Ray';

SELECT * FROM pets;

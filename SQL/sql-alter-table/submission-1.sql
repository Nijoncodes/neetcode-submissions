CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

-- Add new collum called age and integer to table 

ALTER TABLE books ADD COLUMN published_year INTEGER;

-- Alter Colums name 

ALTER TABLE books RENAME COLUMN id TO isbn;

-- Deletes Column author in the books table 

ALTER TABLE books DROP COLUMN author;














-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;

# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

student, cohort, student_name, cohort_name, starting_date
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| cohort                | name, start_date    |
| student               | name, cohort        |

1. Name of the first table (always plural): `students` 

    Column names: `name`, `cohort`

2. Name of the second table (always plural): `cohort` 

    Column names: `name`, `start_date`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: students
id: SERIAL
name: text
cohort: text

Table: cohort
id: SERIAL
name: text
start_date: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
);

-- Then the table with the foreign key second.
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```
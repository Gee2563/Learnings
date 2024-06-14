CREATE TABLE cohorts (
id SERIAL PRIMARY KEY,
name text,
starting_date INT
);

CREATE TABLE students (
id SERIAL PRIMARY KEY,
name TEXT,
cohort_id INT,
CONSTRAINT fk_cohort FOREIGN KEY(cohort_id)
REFERENCES cohorts(id)
on DELETE CASCADE
);
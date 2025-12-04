-- 1) Create tables students and grades
CREATE TABLE "students" (
	"ID"	INTEGER,
	"full_name"	TEXT,
	"birth_year"	INTEGER,
	PRIMARY KEY("ID")
)

CREATE TABLE "grades" (
	"ID"	INTEGER,
	"student_id"	INTEGER,
	"subject"	TEXT,
	"grade"	INTEGER,
	PRIMARY KEY("ID"),
	FOREIGN KEY("student_id") REFERENCES "students"("ID")
)

-- 2) Insert data in tables students and grades
INSERT INTO students (full_name, birth_year)
VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- 3) Find all grades for Alice Johnson
SELECT *
FROM grades
WHERE student_id =
    (
    SELECT id
    FROM students
    WHERE full_name = "Alice Johnson"
);

-- 4) Calculate the average grade per student
SELECT
    students.id AS student_id,
    students.full_name AS student_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
LEFT JOIN grades ON students.id = grades.student_id
GROUP BY students.id;

-- 5) List all sudent born after 2004
SELECT *
FROM students
WHERE birth_year > 2004;

-- 6) Create a query that lists all subjects and their average grades
SELECT
    subject,
    ROUND(AVG(grade), 2) AS average_grade
FROM grades
GROUP BY subject;

-- 7) Find the top 3 students with the highest average grades
SELECT
    students.id AS student_id,
    students.full_name AS student_name,
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
LEFT JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average_grade DESC, students.full_name
LIMIT 3;

-- 8) Show all students who have scored below 80 in any subject
SELECT DISTINCT
    students.id,
    students.full_name
FROM students
INNER JOIN grades ON students.id = grades.student_id
WHERE grades.grade < 80
ORDER BY students.full_name;

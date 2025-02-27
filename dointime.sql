-- INSERT into student (name, surname) select DISTINCT students_name, students_surname from student_course_1

select * from student

INSERT into course (name, price) select DISTINCT course_name, course_price from student_course_1

select * from course

delete from student_course

select * from student_course

insert into student_course values (1,1)

INSERT into student_course (student_id, course_id) select DISTINCT student.id, course.id from student_course_1
inner JOIN student on student.name = student_course_1.students_name
inner JOIN course on course.name = student_course_1.course_name

select s.name, s.surname, c.name, c.price from student_course as sk
inner join student as s on s.id = sk.student_id
inner join course as c on c.id = sk.course_id

select s.name, s.surname, count(*), sum(c.price) from student_course as sk
inner join student as s on s.id = sk.student_id
inner join course as c on c.id = sk.course_id
group by s.name, s.surname

select * from student_course as sk
inner join student as s on s.id = sk.student_id
inner join course as c on c.id = sk.course_id
group by c.name

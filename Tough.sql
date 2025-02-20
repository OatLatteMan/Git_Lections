select id, name from zamestnanec
where id > 2 or id = 1
order by name -- DESC -- ASC
limit 10

select * from zamestnanec
where name like 'T%'

select * from zamestnanec
where id > 2 and name like '%a%'

select count(*) from zamestnanec

select min(id) from zamestnanec

select max(id) from zamestnanec

select min(id), max(id) from zamestnanec

select sum(id) * sum(id) from zamestnanec
where id > 2

----------------------------------------------------------------
-- CRUD
-- c = create (SQL: INSERT)
-- r = read / retrieve (SQL: select)
-- u = update (SQL: UPDATE)
-- d = delete (SQL: DELETE)

UPDATE zamestnanec SET name = 'Ladislav Krejci' where id = 1

SELECT * from zamestnanec limit 100

UPDATE zamestnanec set name = 'xyz' where name like '%a%'

update zamestnanec set name = 'Tomas Vaclik' where id = 1
update zamestnanec set name = 'Vitezslav Jaros' where id = 2
update zamestnanec set name = 'Vladislav Repka' where id = 3
update zamestnanec set name = 'Patrik Schick' where id = 4
select * from zamestnanec limit 5

delete from zamestnanec where id = 3
select * from zamestnanec

update zamestnanec set id = 3 where id = 4
insert into zamestnanec (name) values ('Adam Hlozek')
update zamestnanec set id = 4 where id = 5
select * from zamestnanec






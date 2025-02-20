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


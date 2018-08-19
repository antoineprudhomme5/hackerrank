select 
(select count(*) from station) -
(select count(distinct city) from station)
as n;
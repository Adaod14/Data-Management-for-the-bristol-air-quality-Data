select b.Location, avg(a.`PM2.5`), avg(a.`VPM2.5`)
from readings a inner join sites b
on a.Site_id = b.Site_id
where year(a.Date_time) = 2019 and time(Date_time) = '08:00:00'
group by b.Location
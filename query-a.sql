select a.Date_time, b.Location, max(a.NOx)
from readings a inner join sites b
on a.Site_id = b.Site_id
where year(Date_time) = 2019
group by b.Location
having max(NOx)
ORDER BY max(NOx) DESC
limit 1


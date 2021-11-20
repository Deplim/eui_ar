-- 참조 : http://b1ix.net/87 

select t1.ssid, t1.sort, t1.status 
from testbl as t1, 
(select ssid, max(sort) as max_sort from testbl group by ssid) as t2 
where t1.sort = t2.max_sort and t1.ssid = t2.ssid;
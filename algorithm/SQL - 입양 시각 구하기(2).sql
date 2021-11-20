#프로그래머스 | 입양 시각 구하기(2) : (https://programmers.co.kr/learn/courses/30/lessons/59413)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

set @hour = -1;
select
    (@hour := @hour +1) as HOUR,
    (select count(*) from animal_outs where hour(`datetime`) = @hour) as `COUNT`
from animal_outs 
where @hour < 23
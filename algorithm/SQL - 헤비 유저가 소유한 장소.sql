--프로그래머스 | 입양 시각 구하기(2) : (https://programmers.co.kr/learn/courses/30/lessons/59413)
-- EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

SELECT *
from PLACES
WHERE HOST_ID in (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING count(*)>=2)
ORDER BY ID
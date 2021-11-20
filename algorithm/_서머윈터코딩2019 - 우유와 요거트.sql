--프로그래머스 | 우유와 요거트 : (https://programmers.co.kr/learn/courses/30/lessons/62284)
-- EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

SELECT CART_ID from 
(select * from CART_PRODUCTS where Name="Milk" or Name="Yogurt" Group by Name, CART_ID)A
GROUP BY CART_ID HAVING COUNT(*)>=2 
ORDER BY CART_ID
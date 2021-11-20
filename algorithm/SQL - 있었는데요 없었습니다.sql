--프로그래머스 | 우유와 요거트 : (https://programmers.co.kr/learn/courses/30/lessons/59043)
-- EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

SELECT I.ANIMAL_ID, O.NAME
FROM ANIMAL_INS AS I, ANIMAL_OUTS AS O
WHERE I.ANIMAL_ID=O.ANIMAL_ID AND I.DATETIME > O.DATETIME
ORDER BY I.DATETIME
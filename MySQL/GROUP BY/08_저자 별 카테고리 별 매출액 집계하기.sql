-- 코드를 입력하세요
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(PRICE * SALES_SUM) AS TOTAL_SALES
FROM (
    SELECT BOOK_ID, CATEGORY, A.AUTHOR_ID, PRICE, AUTHOR_NAME
    FROM BOOK A
    LEFT JOIN AUTHOR B
    ON A.AUTHOR_ID = B.AUTHOR_ID
) X
JOIN (
    SELECT BOOK_ID, SUM(SALES) AS SALES_SUM
    FROM BOOK_SALES
    WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-01'
    GROUP BY BOOK_ID
) Y
ON X.BOOK_ID = Y.BOOK_ID
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC
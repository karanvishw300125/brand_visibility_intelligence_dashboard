 1. OVERVIEW

 KPI: Total Products
SELECT COUNT(*) AS total_products
FROM products;


 KPI: Average Price
SELECT ROUND(AVG(price), 2) AS avg_price
FROM products
WHERE price IS NOT NULL
AND price > 0;


 KPI: Average Rating
SELECT ROUND(AVG(rating), 2) AS avg_rating
FROM products
WHERE rating IS NOT NULL
AND rating BETWEEN 1 AND 5;


 KPI: Total Reviews
SELECT COALESCE(SUM(Reviews), 0) AS total_reviews
FROM products
WHERE Reviews IS NOT NULL
AND Reviews >= 0;


 Chart: Price Distribution
SELECT
    CASE
        WHEN price < 1000 THEN 'Below 1000'
        WHEN price < 5000 THEN '1000 - 4999'
        WHEN price < 10000 THEN '5000 - 9999'
        WHEN price < 25000 THEN '10000 - 24999'
        WHEN price < 50000 THEN '25000 - 49999'
        WHEN price < 100000 THEN '50000 - 99999'
        ELSE '100000+'
    END AS price_bucket,
    COUNT(*) AS product_count
FROM products
WHERE price IS NOT NULL
AND price > 0
GROUP BY price_bucket
ORDER BY
    CASE price_bucket
        WHEN 'Below 1000' THEN 1
        WHEN '1000 - 4999' THEN 2
        WHEN '5000 - 9999' THEN 3
        WHEN '10000 - 24999' THEN 4
        WHEN '25000 - 49999' THEN 5
        WHEN '50000 - 99999' THEN 6
        WHEN '100000+' THEN 7
    END;


 Chart: Products per Keyword
SELECT
    keyword,
    COUNT(*) AS product_count
FROM products
GROUP BY keyword
ORDER BY product_count DESC;


 Chart: Platform Share
SELECT
    platform,
    COUNT(*) AS product_count
FROM products
WHERE platform IS NOT NULL
GROUP BY platform
ORDER BY product_count DESC;



 2. BRAND INSIGHTS

 KPI: Top Brand
SELECT
    brand,
    COUNT(*) AS product_count
FROM products
WHERE brand IS NOT NULL
GROUP BY brand
ORDER BY product_count DESC
LIMIT 1;


 KPI: Average Visibility Score
SELECT
    ROUND(AVG(visibility_score), 2) AS avg_visibility_score
FROM products
WHERE visibility_score IS NOT NULL;


 Chart: Brand vs Product Count
SELECT
    brand,
    COUNT(*) AS product_count
FROM products
WHERE brand IS NOT NULL
GROUP BY brand
ORDER BY product_count DESC;


 Chart: Brand vs Average Rating
SELECT
    brand,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
WHERE brand IS NOT NULL
AND rating IS NOT NULL
AND rating BETWEEN 1 AND 5
GROUP BY brand
ORDER BY avg_rating DESC;


 Chart: Top Brands in Top 10 Positions
SELECT
    brand,
    COUNT(*) AS top_10_products
FROM products
WHERE brand IS NOT NULL
AND position IS NOT NULL
AND position <= 10
GROUP BY brand
ORDER BY top_10_products DESC;



 3. PRICING ANALYSIS

 KPI: Average Price
SELECT
    ROUND(AVG(price), 2) AS avg_price
FROM products
WHERE price IS NOT NULL
AND price > 0;


 KPI: Maximum Price
SELECT
    ROUND(MAX(price), 2) AS max_price
FROM products
WHERE price IS NOT NULL
AND price > 0;


 KPI: Discounted Products
 raw_price is missing in current dataset,
 so this will return 0 / NULL.
SELECT
    ROUND(
        100.0 * SUM(
            CASE
                WHEN raw_price IS NOT NULL
                AND raw_price > price
                THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS discounted_percentage
FROM products
WHERE price IS NOT NULL
AND price > 0;


 Chart: Price Distribution
SELECT
    CASE
        WHEN price < 1000 THEN 'Below 1000'
        WHEN price < 5000 THEN '1000 - 4999'
        WHEN price < 10000 THEN '5000 - 9999'
        WHEN price < 25000 THEN '10000 - 24999'
        WHEN price < 50000 THEN '25000 - 49999'
        WHEN price < 100000 THEN '50000 - 99999'
        ELSE '100000+'
    END AS price_bucket,
    COUNT(*) AS product_count
FROM products
WHERE price IS NOT NULL
AND price > 0
GROUP BY price_bucket
ORDER BY product_count DESC;


 Chart: Price vs Ranking
SELECT
    price,
    position,
    title,
    brand,
    platform
FROM products
WHERE price IS NOT NULL
AND price > 0
AND position IS NOT NULL
ORDER BY position;


 Chart: Price vs Rating
SELECT
    price,
    rating,
    title,
    brand,
    platform
FROM products
WHERE price IS NOT NULL
AND price > 0
AND rating IS NOT NULL
AND rating BETWEEN 1 AND 5;



 4. PLATFORM ANALYSIS

 KPI: Total Platforms
SELECT
    COUNT(DISTINCT platform) AS total_platforms
FROM products
WHERE platform IS NOT NULL;


 KPI: Best Platform by Average Rating
SELECT
    platform,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
WHERE platform IS NOT NULL
AND rating IS NOT NULL
AND rating BETWEEN 1 AND 5
GROUP BY platform
ORDER BY avg_rating DESC
LIMIT 1;


 Chart: Platform vs Product Count
SELECT
    platform,
    COUNT(*) AS product_count
FROM products
WHERE platform IS NOT NULL
GROUP BY platform
ORDER BY product_count DESC;


 Chart: Platform vs Average Price
SELECT
    platform,
    ROUND(AVG(price), 2) AS avg_price
FROM products
WHERE platform IS NOT NULL
AND price IS NOT NULL
AND price > 0
GROUP BY platform
ORDER BY avg_price ASC;


 Chart: Platform vs Average Rating
SELECT
    platform,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
WHERE platform IS NOT NULL
AND rating IS NOT NULL
AND rating BETWEEN 1 AND 5
GROUP BY platform
ORDER BY avg_rating DESC;



 5. VISIBILITY & RANKING

 KPI: Average Position
SELECT
    ROUND(AVG(position), 2) AS avg_position
FROM products
WHERE position IS NOT NULL;


 KPI: Average Visibility Score
SELECT
    ROUND(AVG(visibility_score), 2) AS avg_visibility_score
FROM products
WHERE visibility_score IS NOT NULL;


 Chart: Ranking Distribution
SELECT
    position,
    COUNT(*) AS product_count
FROM products
WHERE position IS NOT NULL
GROUP BY position
ORDER BY position ASC;


 Chart: Rating vs Ranking
SELECT
    rating,
    position,
    title,
    brand,
    platform
FROM products
WHERE rating IS NOT NULL
AND rating BETWEEN 1 AND 5
AND position IS NOT NULL
ORDER BY position ASC;


 Chart: Reviews vs Ranking
SELECT
    Reviews,
    position,
    rating,
    title,
    brand,
    platform
FROM products
WHERE Reviews IS NOT NULL
AND Reviews >= 0
AND position IS NOT NULL
ORDER BY position ASC;



 6. PRODUCT EXPLORER

 Searchable / sortable product data
SELECT
    title,
    brand,
    price,
    rating,
    Reviews,
    platform,
    position,
    NULL AS discount
FROM products
ORDER BY position ASC;


 Top-performing products
SELECT
    title,
    brand,
    keyword,
    price,
    rating,
    Reviews,
    platform,
    position,
    visibility_score
FROM products
WHERE position IS NOT NULL
ORDER BY position ASC
LIMIT 10;



 ADDITIONAL BUSINESS ANALYSIS

 Top 10 percentage
SELECT
    ROUND(
        100.0 * SUM(
            CASE
                WHEN position <= 10 THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(position), 0),
        2
    ) AS top_10_percentage
FROM products
WHERE position IS NOT NULL;


 Best ranked product
SELECT
    title,
    brand,
    keyword,
    price,
    rating,
    platform,
    position,
    visibility_score
FROM products
WHERE position = 1
ORDER BY visibility_score DESC;


 Highest visibility products
SELECT
    title,
    brand,
    keyword,
    platform,
    position,
    ROUND(visibility_score, 2) AS visibility_score
FROM products
WHERE visibility_score IS NOT NULL
ORDER BY visibility_score DESC
LIMIT 20;


 Brand average position
SELECT
    brand,
    ROUND(AVG(position), 2) AS avg_position
FROM products
WHERE brand IS NOT NULL
AND position IS NOT NULL
GROUP BY brand
ORDER BY avg_position ASC;


 Platform average position
SELECT
    platform,
    ROUND(AVG(position), 2) AS avg_position
FROM products
WHERE platform IS NOT NULL
AND position IS NOT NULL
GROUP BY platform
ORDER BY avg_position ASC;


 Review engagement vs ranking
SELECT
    CASE
        WHEN Reviews < 100 THEN 'Low Reviews'
        WHEN Reviews < 1000 THEN 'Medium Reviews'
        ELSE 'High Reviews'
    END AS review_category,
    COUNT(*) AS product_count,
    ROUND(AVG(position), 2) AS avg_position
FROM products
WHERE Reviews IS NOT NULL
AND position IS NOT NULL
GROUP BY review_category
ORDER BY avg_position ASC;


 Top 10 vs Below Top 10 comparison
SELECT
    CASE
        WHEN position <= 10 THEN 'Top 10'
        ELSE 'Below Top 10'
    END AS ranking_group,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(rating), 2) AS avg_rating,
    ROUND(AVG(Reviews), 2) AS avg_reviews,
    ROUND(AVG(visibility_score), 2) AS avg_visibility_score
FROM products
WHERE position IS NOT NULL
GROUP BY ranking_group
ORDER BY
    CASE ranking_group
        WHEN 'Top 10' THEN 1
        ELSE 2
    END;
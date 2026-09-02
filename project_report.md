# Insight Generation & Business Recommendations

## Key Business Insights

1. **Brand visibility varies significantly across products.**
   Some brands achieve stronger search visibility and appear more frequently in higher-ranking positions, indicating better marketplace presence and search performance.

2. **Top-ranking products represent the strongest visible products in the dataset.**
   Products appearing within the top 10 positions have substantially better visibility scores because visibility score is directly derived from search position.

3. **Product price does not appear to be the only factor determining search ranking.**
   Products across different price ranges are present in both high and lower search positions, suggesting that ranking is influenced by multiple factors rather than price alone.

4. **Customer ratings can be associated with product visibility.**
   Comparing rating and ranking helps identify whether highly rated products tend to achieve better positions. This can help brands understand the importance of maintaining strong customer satisfaction.

5. **Customer reviews provide an indication of product engagement.**
   Products with a higher number of reviews can show stronger market engagement. Comparing reviews with ranking helps identify whether customer engagement is associated with better search visibility.

6. **Platform competition is uneven.**
   Some platforms contain considerably more products than others. This indicates that marketplace coverage and competitive intensity differ across platforms.

7. **Average pricing varies across platforms.**
   The platform-level price comparison highlights differences in pricing strategies and product positioning across marketplaces.

8. **Brand performance should be evaluated using multiple metrics.**
   Product count alone does not identify the strongest brand. Visibility score, average ranking, rating, and top-10 presence provide a more complete view of brand performance.

9. **The dataset contains important data-quality limitations.**
   A significant number of products do not have search-position data because ranking information was primarily available from the API dataset. Therefore, ranking-based metrics represent the ranked subset rather than the entire dataset.

10. **Discount analysis is currently limited by missing original-price data.**
    The `raw_price` field is unavailable in the current dataset, so reliable discount percentages cannot be calculated. Discount-related conclusions should therefore be treated as unavailable rather than estimated.

## Business Recommendations

* Brands should focus on improving **search visibility and top-10 rankings** for strategically important products.
* High-performing products should be monitored for their **price, rating, review volume, and platform presence** to identify successful patterns.
* Brands should compare their performance across marketplaces to identify **high-opportunity and highly competitive platforms**.
* Pricing decisions should not be based only on ranking; brands should consider **rating, reviews, competition, and platform-level pricing** together.
* Improving **customer satisfaction and review engagement** may help strengthen overall product competitiveness.
* Future data collection should capture **original price and discount information** so that discount strategies can be properly compared across brands and platforms.
* Regularly collecting fresh Google Shopping data can help create a **continuous brand visibility monitoring system** and identify changes in competitor positioning.

DROP TABLE IF EXISTS "Helpful_Non_Vine_Users";
DROP TABLE IF EXISTS "Helpful_Vine_Users";
DROP TABLE IF EXISTS "vine_rating_summary";
DROP TABLE IF EXISTS "nonvine_rating_summary";
DROP TABLE IF EXISTS "total_non_vine_reviews";
DROP TABLE IF EXISTS "total_vine_reviews";
DROP TABLE IF EXISTS "vine_rating_summary_final";
DROP TABLE IF EXISTS "nonvine_rating_summary_final";

CREATE TABLE IF NOT EXISTS "Helpful_Non_Vine_Users" AS SELECT * FROM vine_table WHERE
total_votes >= 20 AND
CAST(helpful_votes AS FLOAT)/CAST(total_votes AS FLOAT) >=0.5 AND
vine = 'N';

CREATE TABLE IF NOT EXISTS "Helpful_Vine_Users" AS SELECT * FROM vine_table WHERE
total_votes >= 20 AND
CAST(helpful_votes AS FLOAT)/CAST(total_votes AS FLOAT) >=0.5 AND
vine = 'Y';

CREATE TABLE IF NOT EXISTS "vine_rating_summary" AS SELECT star_rating, COUNT(star_rating) AS total_reviews FROM "Helpful_Vine_Users" GROUP BY star_rating;
CREATE TABLE IF NOT EXISTS "nonvine_rating_summary" AS SELECT star_rating, COUNT(star_rating) AS total_reviews FROM "Helpful_Non_Vine_Users" GROUP BY star_rating;

CREATE TABLE IF NOT EXISTS "total_non_vine_reviews" AS SELECT SUM(total_reviews) AS all_reviews FROM nonvine_rating_summary;
CREATE TABLE IF NOT EXISTS "total_vine_reviews" AS SELECT SUM(total_reviews) AS all_reviews FROM vine_rating_summary;

CREATE TABLE IF NOT EXISTS "vine_rating_summary_final" AS SELECT star_rating, total_reviews, total_reviews/total_vine_reviews.all_reviews * 100 AS percent_reviews
FROM vine_rating_summary, total_vine_reviews
ORDER BY star_rating;

CREATE TABLE IF NOT EXISTS "nonvine_rating_summary_final" AS SELECT star_rating, total_reviews, total_reviews/total_non_vine_reviews.all_reviews * 100 AS percent_reviews
FROM nonvine_rating_summary, total_non_vine_reviews
ORDER BY star_rating;

SELECT nonvine_rating_summary_final.star_rating AS star_rating,
	   nonvine_rating_summary_final.total_reviews AS non_vine_reviews,
	   vine_rating_summary_final.total_reviews AS vine_reviews, 
	   nonvine_rating_summary_final.percent_reviews AS non_vine_pert, 
	   vine_rating_summary_final.percent_reviews AS vine_pert
	   FROM nonvine_rating_summary_final, vine_rating_summary_final 
	   WHERE nonvine_rating_summary_final.star_rating = vine_rating_summary_final.star_rating;
	   
-- SELECT vine, count(vine) FROM vine_table GROUP BY vine;
-- SELECT total_vine_reviews.all_reviews AS Total_Vine_Reviews, total_non_vine_reviews.all_reviews AS Total_NonVine_Reviews FROM total_vine_reviews, total_non_vine_reviews;


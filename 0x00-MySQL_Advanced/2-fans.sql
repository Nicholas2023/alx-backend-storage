-- A script that ranks country origins
-- Ordered by the number of fans
-- Requirements: Imports table, col origin  nb_fans

SELECT origin, COUNT(*) AS nb_fans, DENSE_RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
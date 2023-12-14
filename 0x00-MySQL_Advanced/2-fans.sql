-- A script that ranks country origins
-- Ordered by the number of fans
-- Requirements: Imports table, col origin  nb_fans

SELECT origin, SUM(nb_fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

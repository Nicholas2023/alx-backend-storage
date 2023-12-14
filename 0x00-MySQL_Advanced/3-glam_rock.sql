-- A script that lists all bands with 'Glam rock'
-- as their main style, ranked by their longevity

SELECT band_name
    CASE
        WHEN formed IS NOT NULL AND split IS NOT NULL THEN (2023 - formed) - (2023 - split)
        WHEN formed IS NOT NULL THEN 2023 - formed
        ELSE NULL
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock'
ORDER BY lifespan DESC;

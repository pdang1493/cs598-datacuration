SELECT 
    id,
    menu_id,
    page_number,

    -- Full height: show as-is and convert NULLs to 'MISSING' for display
    full_height,
    CASE 
        WHEN full_height IS NULL THEN 'MISSING'
        ELSE CAST(full_height AS TEXT)
    END AS full_height_cleaned,

    -- Full width: same as above
    full_width,
    CASE 
        WHEN full_width IS NULL THEN 'MISSING'
        ELSE CAST(full_width AS TEXT)
    END AS full_width_cleaned,

    -- Clean text fields
    image_id,
    TRIM(image_id) AS image_id_cleaned,

    uuid,
    TRIM(uuid) AS uuid_cleaned

FROM MenuPage
WHERE 
    id IS NOT NULL
    AND menu_id IS NOT NULL
    AND page_number IS NOT NULL
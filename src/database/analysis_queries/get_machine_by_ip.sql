SELECT
    id,
    allias,
    ip,
    port,
    is_enabled,
    created_at.
    updated_at,
    os
FROM public.machine
where ip = $1

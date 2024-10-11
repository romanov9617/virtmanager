SELECT
    id,
    allias,
    ip::varchar(15),
    port,
    is_enabled,
    os
FROM public.machine
where allias = $1

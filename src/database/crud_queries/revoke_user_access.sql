DELETE FROM public.user_machine_access
WHERE user_id = $1 AND machine_id = $2;

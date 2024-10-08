SELECT id, username, password, salt, is_superuser, created_at, updated_at
FROM public.user
WHERE username = $1
LIMIT 1;

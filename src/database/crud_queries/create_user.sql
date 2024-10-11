INSERT INTO public.user (username, password, salt, is_superuser)
VALUES ($1, $2::varchar, $3, $4::boolean)

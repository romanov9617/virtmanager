INSERT INTO public.user_machine (user_id, machine_id, login_at)
Values ($1, $2, NOW())
RETURNING id;

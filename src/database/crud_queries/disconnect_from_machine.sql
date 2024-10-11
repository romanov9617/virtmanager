UPDATE public.user_machine
SET logout_at = NOW()
WHERE id = $1

select
	public.machine.id,
	allias,
	is_enabled,
	ip,
	port,
	public.machine.created_at,
	public.machine.updated_at
from public.machine
join public.user_machine_access
on public.machine.id = public.user_machine_access.machine_id
and public.user_machine_access.user_id = $1

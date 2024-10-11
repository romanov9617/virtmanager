SELECT
	public.machine.id
	allias,
	ip,
	port,
	os,
	public.machine.created_at as start_date_machine,
	public.user_machine_access.created_at as start_date_permission

FROM public.machine
join public.user_machine_access
on public.machine.id = public.user_machine_access.machine_id
join public.user
on public.user.id = public.user_machine_access.user_id
and public.user.id = $1

select
	public.machine.id,
	ip,
	port,
	allias,
	SUM(public.processor.frequency * public.processor_machine.usage_percent / 100) as processor_frequency_usage,
	SUM(public.hard_drive.capacity * public.hard_drive_machine.usage_percent / 100) as hard_drive_capacity_usage,
	SUM(public.memory.capacity * public.memory_machine.usage_percent / 100) as memory_capacity_usage
from public.machine


join public.hard_drive_machine
on public.machine.id = public.hard_drive_machine.machine_id

join public.hard_drive
on public.hard_drive_machine.hard_drive_id = public.hard_drive.id

join public.memory_machine
on public.machine.id = public.memory_machine.machine_id

join public.memory
on public.memory_machine.memory_id = public.memory.id

join public.processor_machine
on public.machine.id = public.processor_machine.machine_id

join public.processor
on public.processor_machine.processor_id = public.processor.id

group by public.machine.id, ip, port, allias

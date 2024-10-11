select
	public.machine.id,
	ip,
	port,
	allias,

	public.processor.id as processor_id,
	public.processor.num_nuclears as processor_num_nuclears,
	public.processor.frequency as processor_frequency,
	public.processor.max_temperature as processor_max_temperature,
	public.processor.service_life_end as processor_service_life_end,
	public.processor.warantee_period_end as processor_warantee_period_end,
	public.processor_machine.usage_percent as processor_usage_percent,

	public.hard_drive.id as hard_drive_id,
	public.hard_drive.frequency as hard_drive_frequency,
	public.hard_drive.type as hard_drive_type,
	public.hard_drive.capacity as hard_drive_capacity,
	public.hard_drive.service_life_end as hard_drive_service_life_end,
	public.hard_drive.warantee_period_end as hard_drive_warantee_period_end,
	public.hard_drive_machine.usage_percent as hard_drive_usage_percent,

	public.memory.id as memory_id,
	public.memory.capacity as memory_capacity,
	public.memory.type as memory_type,
	public.memory.frequency as memory_frequency,
	public.memory.service_life_end as memory_service_life_end,
	public.memory.warantee_period_end as memory_warantee_period_end,
	public.memory_machine.usage_percent as memory_usage_percent
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


WITH
	machine_ids as (
	INSERT INTO public.machine (allias, ip, port, os)
	VALUES ($1, $2, $3, $10)
	RETURNING id as machine_id_
	),

	hard_drive_percent as (
		select * from unnest(
			ARRAY(
			select id
			from public.hard_drive
			where public.hard_drive.id = ANY($4)
			), $5::int[]) as x(hard_drive_id, usage_percent)
	),

	hard_drive_secondary_insert as (
	INSERT INTO public.hard_drive_machine (machine_id, hard_drive_id, usage_percent)
	select machine_id_, hard_drive_percent.hard_drive_id, hard_drive_percent.usage_percent::integer
	from machine_ids, hard_drive_percent
	),

	processor_percent as (
		select * from unnest(
			ARRAY(
			select id
			from public.processor
			where public.processor.id = ANY($6)
			), $7::int[]) as x(processor_id, usage_percent)
	),

	processor_secondary_insert as (
	INSERT INTO public.processor_machine (machine_id, processor_id, usage_percent)
	select machine_id_, processor_percent.processor_id, processor_percent.usage_percent::integer
	from machine_ids, processor_percent
	),

	memory_percent as (
		select * from unnest(
			ARRAY(
			select id
			from public.memory
			where public.memory.id = ANY($8)
			), $9::int[]) as x(memory_id, usage_percent)
	),

	memory_secondary_insert as (
	INSERT INTO public.memory_machine (machine_id, memory_id, usage_percent)
	select machine_id_, memory_percent.memory_id, memory_percent.usage_percent::integer
	from machine_ids, memory_percent
	)


select *
from machine_ids

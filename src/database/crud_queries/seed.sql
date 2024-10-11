BEGIN TRANSACTION;

INSERT INTO "public"."processor" ("name", "num_nuclears", "frequency", "max_temperature", "service_life_end", "warantee_period_end")
VALUES
    ('Intel Core i5 12400F OEM (CM8071504555318, SRL4W)', 6, 2500, 100, NOW() - INTERVAL '1 day', NOW() - INTERVAL '1 year'),
    ('AMD Ryzen 5 5600 AM4, 6 x 3500 МГц, OEM', 6, 3500, 90, NOW() + INTERVAL '7 day', NOW() + INTERVAL '2 day'),
	('Intel Core i7-13700KF LGA1700 OEM (CM8071504820706)', 16, 2500, 100, NOW() + INTERVAL '2 year', NOW() + INTERVAL '1 year');

INSERT INTO "public"."hard_drive" ("type", "capacity", "frequency", "service_life_end", "warantee_period_end")
VALUES
    ('HDD', 512, 7200, NOW() - INTERVAL '1 day', NOW() - INTERVAL '1 year'),
    ('HDD', 1024, 7200, NOW() + INTERVAL '7 day', NOW() + INTERVAL '2 day'),
    ('HDD', 512, 7200, NOW() + INTERVAL '2 year', NOW() + INTERVAL '1 year');

INSERT INTO "public"."memory" ("type", "capacity", "frequency", "service_life_end", "warantee_period_end")
VALUES
    ('DDR4', 16, 3200, NOW() - INTERVAL '1 day', NOW() - INTERVAL '1 year'),
    ('DDR4', 32, 3200, NOW() + INTERVAL '7 day', NOW() + INTERVAL '2 day'),
    ('DDR4', 16, 3200, NOW() + INTERVAL '2 year', NOW() + INTERVAL '1 year');

COMMIT TRANSACTION;

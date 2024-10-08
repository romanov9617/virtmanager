BEGIN TRANSACTION;

INSERT INTO machine (allias, is_enabled, ip, created_at, updated_at) VALUES ($1, $2, $3, $4, $5);

COMMIT TRANSACTION;

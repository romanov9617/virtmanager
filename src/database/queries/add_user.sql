BEGIN TRANSACTION;

INSERT INTO "user" (username, password, salt, is_superuser, created_at, updated_at) VALUES ($1, $2, $3, $4, $5, $6);

COMMIT TRANSACTION;

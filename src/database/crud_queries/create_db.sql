BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS machine (
        parent_id UUID,
        allias VARCHAR NOT NULL,
        is_enabled BOOLEAN NOT NULL DEFAULT True,
        ip VARCHAR NOT NULL,
        port INTEGER NOT NULL,
        os VARCHAR NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(parent_id) REFERENCES "machine" (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  "user" (
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        salt VARCHAR NOT NULL,
        is_superuser BOOLEAN NOT NULL DEFAULT False,
        is_authorized BOOLEAN NOT NULL DEFAULT False,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS  processor (
        name VARCHAR NOT NULL,
        num_nuclears INTEGER NOT NULL,
        frequency INTEGER NOT NULL,
        max_temperature INTEGER NOT NULL,
        service_life_end TIMESTAMP WITHOUT TIME ZONE,
        warantee_period_end TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  memory (
        type VARCHAR NOT NULL,
        capacity INTEGER NOT NULL,
        frequency INTEGER NOT NULL,
        service_life_end TIMESTAMP WITHOUT TIME ZONE,
        warantee_period_end TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS hard_drive (
        type VARCHAR NOT NULL,
        capacity INTEGER NOT NULL,
        frequency INTEGER NOT NULL,
        service_life_end TIMESTAMP WITHOUT TIME ZONE,
        warantee_period_end TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS user_machine (
        user_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        login_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        logout_at TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES "user" (id)
        ON DELETE CASCADE,
        FOREIGN KEY(machine_id) REFERENCES machine (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS processor_machine (
        processor_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(processor_id) REFERENCES processor (id)
        ON DELETE CASCADE,
        FOREIGN KEY(machine_id) REFERENCES machine (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS memory_machine (
        memory_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(memory_id) REFERENCES memory (id)
        ON DELETE CASCADE,
        FOREIGN KEY(machine_id) REFERENCES machine (id)
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS  hard_drive_machine (
        hard_drive_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(hard_drive_id) REFERENCES hard_drive (id)
        ON DELETE CASCADE,
        FOREIGN KEY(machine_id) REFERENCES machine (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_machine_access (
        user_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        is_allowed BOOLEAN NOT NULL DEFAULT True,
        is_admin BOOLEAN NOT NULL DEFAULT False,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES "user" (id)
        ON DELETE CASCADE,
        FOREIGN KEY(machine_id) REFERENCES machine (id)
        ON DELETE CASCADE
);

COMMIT TRANSACTION;

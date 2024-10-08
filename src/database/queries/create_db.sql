BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS machine (
        allias VARCHAR NOT NULL,
        is_enabled BOOLEAN NOT NULL,
        ip INET NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  "user" (
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        salt VARCHAR NOT NULL,
        is_superuser BOOLEAN NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
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
        login_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        logout_at TIMESTAMP WITHOUT TIME ZONE,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES "user" (id),
        FOREIGN KEY(machine_id) REFERENCES machine (id)
);

CREATE TABLE IF NOT EXISTS processor_machine (
        processor_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(processor_id) REFERENCES processor (id),
        FOREIGN KEY(machine_id) REFERENCES machine (id)
);

CREATE TABLE IF NOT EXISTS memory_machine (
        memory_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(memory_id) REFERENCES memory (id),
        FOREIGN KEY(machine_id) REFERENCES machine (id)
);


CREATE TABLE IF NOT EXISTS  hard_drive_machine (
        hard_drive_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        usage_percent INTEGER NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(hard_drive_id) REFERENCES hard_drive (id),
        FOREIGN KEY(machine_id) REFERENCES machine (id)
);

CREATE TABLE IF NOT EXISTS user_machine_access (
        user_id UUID NOT NULL,
        machine_id UUID NOT NULL,
        is_allowed BOOLEAN NOT NULL,
        is_admin BOOLEAN NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        id UUID DEFAULT gen_random_uuid() NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES "user" (id),
        FOREIGN KEY(machine_id) REFERENCES machine (id)
);

COMMIT TRANSACTION;

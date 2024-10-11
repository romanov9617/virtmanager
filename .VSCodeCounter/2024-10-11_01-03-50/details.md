# Details

Date : 2024-10-11 01:03:50

Directory /home/romanov-d/code/education/virtmanager

Total : 54 files,  2502 codes, 8 comments, 561 blanks, all 3071 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [.github/workflows/virtmanager.yml](/.github/workflows/virtmanager.yml) | YAML | 25 | 0 | 4 | 29 |
| [.pre-commit-config.yaml](/.pre-commit-config.yaml) | YAML | 48 | 0 | 7 | 55 |
| [Dockerfile](/Dockerfile) | Docker | 7 | 0 | 4 | 11 |
| [README.md](/README.md) | Markdown | 1 | 0 | 0 | 1 |
| [main.py](/main.py) | Python | 6 | 0 | 4 | 10 |
| [megalinter.yml](/megalinter.yml) | YAML | 58 | 7 | 2 | 67 |
| [poetry.lock](/poetry.lock) | TOML | 933 | 1 | 73 | 1,007 |
| [pyproject.toml](/pyproject.toml) | TOML | 56 | 0 | 11 | 67 |
| [requirements.txt](/requirements.txt) | pip requirements | 40 | 0 | 1 | 41 |
| [src/__init__.py](/src/__init__.py) | Python | 1 | 0 | 1 | 2 |
| [src/abstract/__init__.py](/src/abstract/__init__.py) | Python | 1 | 0 | 1 | 2 |
| [src/abstract/chain.py](/src/abstract/chain.py) | Python | 74 | 0 | 26 | 100 |
| [src/auth.py](/src/auth.py) | Python | 63 | 0 | 21 | 84 |
| [src/bus.py](/src/bus.py) | Python | 28 | 0 | 13 | 41 |
| [src/cli/__init__.py](/src/cli/__init__.py) | Python | 7 | 0 | 2 | 9 |
| [src/cli/auth.py](/src/cli/auth.py) | Python | 49 | 0 | 17 | 66 |
| [src/cli/base.py](/src/cli/base.py) | Python | 38 | 0 | 15 | 53 |
| [src/cli/cli.py](/src/cli/cli.py) | Python | 40 | 0 | 14 | 54 |
| [src/cli/connection.py](/src/cli/connection.py) | Python | 6 | 0 | 6 | 12 |
| [src/cli/root/__init__.py](/src/cli/root/__init__.py) | Python | 10 | 0 | 2 | 12 |
| [src/cli/root/create.py](/src/cli/root/create.py) | Python | 143 | 0 | 30 | 173 |
| [src/cli/root/delete.py](/src/cli/root/delete.py) | Python | 21 | 0 | 12 | 33 |
| [src/cli/root/permission.py](/src/cli/root/permission.py) | Python | 6 | 0 | 6 | 12 |
| [src/cli/root/root.py](/src/cli/root/root.py) | Python | 22 | 0 | 9 | 31 |
| [src/cli/root/show.py](/src/cli/root/show.py) | Python | 11 | 0 | 10 | 21 |
| [src/cli/show.py](/src/cli/show.py) | Python | 6 | 0 | 6 | 12 |
| [src/config.py](/src/config.py) | Python | 28 | 0 | 12 | 40 |
| [src/database/__init__.py](/src/database/__init__.py) | Python | 14 | 0 | 5 | 19 |
| [src/database/analysis_queries/get_all_hard_drives.sql](/src/database/analysis_queries/get_all_hard_drives.sql) | MS SQL | 8 | 0 | 1 | 9 |
| [src/database/analysis_queries/get_all_memories.sql](/src/database/analysis_queries/get_all_memories.sql) | MS SQL | 8 | 0 | 1 | 9 |
| [src/database/analysis_queries/get_all_processors.sql](/src/database/analysis_queries/get_all_processors.sql) | MS SQL | 9 | 0 | 1 | 10 |
| [src/database/analysis_queries/get_enabled_machines.sql](/src/database/analysis_queries/get_enabled_machines.sql) | MS SQL | 3 | 0 | 1 | 4 |
| [src/database/base.py](/src/database/base.py) | Python | 37 | 0 | 13 | 50 |
| [src/database/crud_queries/create_db.sql](/src/database/crud_queries/create_db.sql) | MS SQL | 121 | 0 | 13 | 134 |
| [src/database/crud_queries/create_machine.sql](/src/database/crud_queries/create_machine.sql) | MS SQL | 47 | 0 | 10 | 57 |
| [src/database/crud_queries/create_user.sql](/src/database/crud_queries/create_user.sql) | MS SQL | 2 | 0 | 0 | 2 |
| [src/database/crud_queries/get_user_by_username.sql](/src/database/crud_queries/get_user_by_username.sql) | MS SQL | 4 | 0 | 1 | 5 |
| [src/database/crud_queries/seed.sql](/src/database/crud_queries/seed.sql) | MS SQL | 17 | 0 | 5 | 22 |
| [src/database/manager.py](/src/database/manager.py) | Python | 82 | 0 | 24 | 106 |
| [src/database/monitor.py](/src/database/monitor.py) | Python | 64 | 0 | 22 | 86 |
| [src/enums.py](/src/enums.py) | Python | 10 | 0 | 8 | 18 |
| [src/exceptions/__init__.py](/src/exceptions/__init__.py) | Python | 1 | 0 | 1 | 2 |
| [src/exceptions/auth.py](/src/exceptions/auth.py) | Python | 11 | 0 | 7 | 18 |
| [src/exceptions/database.py](/src/exceptions/database.py) | Python | 16 | 0 | 10 | 26 |
| [src/machine/__init__.py](/src/machine/__init__.py) | Python | 5 | 0 | 2 | 7 |
| [src/machine/creator.py](/src/machine/creator.py) | Python | 64 | 0 | 23 | 87 |
| [src/machine/product.py](/src/machine/product.py) | Python | 109 | 0 | 38 | 147 |
| [src/schemas/__init__.py](/src/schemas/__init__.py) | Python | 4 | 0 | 2 | 6 |
| [src/schemas/machine.py](/src/schemas/machine.py) | Python | 52 | 0 | 22 | 74 |
| [src/schemas/user.py](/src/schemas/user.py) | Python | 24 | 0 | 16 | 40 |
| [src/utils.py](/src/utils.py) | Python | 17 | 0 | 9 | 26 |
| [tests/conftest.py](/tests/conftest.py) | Python | 12 | 0 | 5 | 17 |
| [tests/unit/database/test_database.py](/tests/unit/database/test_database.py) | Python | 0 | 0 | 1 | 1 |
| [tests/unit/test_auth.py](/tests/unit/test_auth.py) | Python | 33 | 0 | 11 | 44 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

"""Package for the database.

It contains database queries for CRUD operations
and class DatabaseManager for incapsulate
all CRUD database logic:

- create_database
- create_user
- create_machine
- get_user_by_username

It also contains only select queries for analytics
or some another goals.
It also contains class Monitor for monitoring database.

This separation of the logic of working with the database
is done in order to be able to replicate the database in the future.
"""

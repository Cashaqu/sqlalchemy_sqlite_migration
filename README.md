# sqlalchemy_sqlite_migration

## Files

BD classes:

https://github.com/Cashaqu/sqlalchemy_sqlite_migration/blob/master/models.py

BD-file:

https://github.com/Cashaqu/sqlalchemy_sqlite_migration/blob/master/sqlalchemy.db

Migration files:

https://github.com/Cashaqu/sqlalchemy_sqlite_migration/blob/master/alembic/versions/b7de96b40195_creation.py

## Commands

Command for initialization alembic-config (creating directory ```./alembic```):
```sh
alembic init alembic
```
Create first revision:
```sh
alembic revision --autogenerate -m "Creation"
```
Push changes to DB:
```sh
alembic upgrade b7de96b40195
```

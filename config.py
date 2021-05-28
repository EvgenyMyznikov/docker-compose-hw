class Postgres:
    POSTGRES_USER = 'testuser'
    POSTGRES_PASSWORD = 'password'
    POSTGRES_HOST = 'localhost:5432'
    POSTGRES_DB = 'testdatabase'


SQLALCHEMY_DATABASE_URI = f"postgresql://{Postgres.POSTGRES_USER}:{Postgres.POSTGRES_PASSWORD}" \
                          f"@{Postgres.POSTGRES_HOST}/{Postgres.POSTGRES_DB}"

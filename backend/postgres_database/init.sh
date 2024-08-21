psql -U postgres << EOF
DROP DATABASE IF EXISTS ${DATABASE_NAME} WITH (FORCE);
DROP USER IF EXISTS ${DATABASE_USER};
CREATE USER ${DATABASE_USER};
ALTER USER pgic9s WITH PASSWORD '${DATABASE_PASSWORD}';
CREATE DATABASE ${DATABASE_NAME};
ALTER DATABASE prototype_ui_db OWNER TO ${DATABASE_USER};
GRANT ALL PRIVILEGES ON DATABASE ${DATABASE_NAME} TO ${DATABASE_USER};
EOF

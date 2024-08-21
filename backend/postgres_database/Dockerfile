FROM postgres:14.1-alpine as builder
COPY init.sh /docker-entrypoint-initdb.d/
# RUN sh /docker-entrypoint-initdb.d/init.sh
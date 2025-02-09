-- Run this as postgres superuser
CREATE DATABASE ems_db;
CREATE USER ems_user WITH PASSWORD 'your_password_here';
ALTER ROLE ems_user SET client_encoding TO 'utf8';
ALTER ROLE ems_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ems_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ems_db TO ems_user; 
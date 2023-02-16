CREATE USER 'fastapi3'@'localhost' IDENTIFIED BY 'fastapi_pass3';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD
on *.* TO 'fastapi3'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS 'rz_seed_shop';
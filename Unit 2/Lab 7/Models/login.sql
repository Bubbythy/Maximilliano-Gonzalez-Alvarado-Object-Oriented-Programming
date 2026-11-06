create database if not exists login_system_db;
use login_system_db;

create table if not exists users (
	id_user INT auto_increment primary key,
	username VARCHAR(50) not null unique,
	password varchar(256) not null,
	nombre varchar (50) not null
);
insert into users (username, password, nombre ) values ('admin', 'admin!123', 'Super Admin')

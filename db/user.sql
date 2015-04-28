drop database if exists chat;
create database chat;
use chat;

drop table if exists user;
create table user(
	uid int not null auto_increment primary key,
	username varchar(20) not null,
	password varchar(20) not null
);

drop table if exists chat;
create table chat(
	cid int not null auto_increment primary key,
	uid int not null,
	foreign key(uid) references user(uid)
);
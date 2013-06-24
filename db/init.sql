create table three_dee_model(
  id serial primary key,
  name varchar(255),
  description varchar(255),
  localpath varchar(255),
  latitude varchar(255),
  longitude varchar(255),
  s3_url varchar(255)
);

create table project(
  id serial primary key,
  name varchar(255),
  description text
);

alter table project add column s3_url varchar(512);
alter table project add column settings_json text;
alter table project add column s3_name varchar(512);
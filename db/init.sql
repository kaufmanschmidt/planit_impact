create table three_dee_model(
  id serial primary key,
  name varchar(255),
  description varchar(255),
  localpath varchar(255),
  latitude varchar(255),
  longitude varchar(255),
  s3_url varchar(255)
);
create table travel_user
(
    id         serial PRIMARY KEY,
    foreign_id int,
    name       varchar(100),
    email      varchar(100),
    age        int
);
create table travel_country
(
    id         serial PRIMARY KEY,
    foreign_id int,
    name       varchar(100)
);
create table UserCountry(
    user_id serial REFERENCES travel_country(id),
    country_id serial REFERENCES travel_user(id)
);

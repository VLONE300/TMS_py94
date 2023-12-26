CREATE TABLE travel_user (
    id SERIAL PRIMARY KEY,
    foreign_id INTEGER,
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER
);

CREATE TABLE travel_country (
    id SERIAL PRIMARY KEY,
    foreign_id INTEGER,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE UserCountry (
    id serial PRIMARY KEY,
    user_id int REFERENCES travel_user(id),
    country_id int REFERENCES travel_country(id),
    UNIQUE (user_id, country_id)
);
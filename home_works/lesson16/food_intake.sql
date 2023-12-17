create database food_intake;

create table users
(
    user_id integer PRIMARY KEY,--Гарантирует уникальность в значений в этом поле
    name    CHAR(100)           --Максимальная длинна имени 100 символов
);

create table product
(
    product_id integer PRIMARY KEY,--Гарантирует уникальность в значений в этом поле
    name       CHAR(100)           --Максимальная длинна имени 100 символов
);

create table food_intake
(
    meal_id    SERIAL PRIMARY KEY,--Гарантирует уникальность в значений в этом поле
    user_id    INTEGER REFERENCES users (user_id),--Внешний ключ связывающий user_id в таблице food_intake с user_id в таблице users
    product_id INTEGER REFERENCES product (product_id),--Внешний ключ, связывающий product_id в таблице food_intake с product_id в таблице product.
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (user_id),--Гарантирует что записи в таблице food_intake могут ссылаться на сущ. записи
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES product (product_id) --Гарантирует что записи в таблице food_intake могут ссылаться на сущ. записи
);

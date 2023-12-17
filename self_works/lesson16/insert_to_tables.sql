INSERT INTO author (name, email)
VALUES ('Bob', 'bob123@gmail.com'),
       ('Kate', 'catcat@gmail.com');


INSERT INTO article (title, topic, content, author_id)
VALUES ('Pancakes', 'cook', 'recept for pancakes', 1),
       ('cheesecake', 'cook', 'recept for cheesecake', 1);


INSERT INTO article (title, topic, content, author_id)
VALUES ('Easy Python', 'Programming', 'Python programming language.', 2),
       ('Easy SQL', 'Programming', 'SQL programming language.', 2);


INSERT INTO comment (nickname, content, rating, article_id)
VALUES ('User1', 'Great article!', 5, 1),
       ('User2', 'Interesting topic!', 4, 1),
       ('User3', 'Thanks for sharing!', 3, 1),
       ('User4', 'Looking forward to more!', 5, 1);


INSERT INTO comment (nickname, content, rating, article_id)
VALUES ('User5', 'Well explained!', 4, 2),
       ('User6', 'Nice examples!', 5, 2),
       ('User7', 'Helped me a lot!', 4, 2),
       ('User8', 'Clear and concise.', 3, 2);
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE article (
    article_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(100),
    content TEXT,
    author_id INTEGER REFERENCES author(author_id)
);

CREATE TABLE comment (
    comment_id SERIAL PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL,
    content TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    article_id INTEGER REFERENCES article(article_id)
);
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- #Создаем таблицу для статей
CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    author_id INT REFERENCES authors(author_id)
);

-- #Создаем таблицу для комментариев
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    article_id INT REFERENCES articles(article_id)
);
select author.name as author_name, article.title as article_title
from author
         join article on author.author_id = article.author_id;

select author.name as author_name, article.content as article_content
from author
         join article on author.author_id = article.author_id;

select article.title as article_title, avg(comment.rating) as comment_rating
from article
         join comment on article.article_id = comment.article_id
group by article.title;

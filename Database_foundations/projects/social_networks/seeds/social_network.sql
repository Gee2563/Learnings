DROP TABLE if EXISTS users cascade;
drop sequence if EXISTS users_id_seq;
CREATE sequence IF NOT EXISTS users_id_seq;

DROP TABLE if EXISTS user_posts;
drop sequence if EXISTS user_posts_id_seq;
CREATE sequence IF NOT EXISTS user_posts_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);


CREATE TABLE user_posts (
    id SERIAL PRIMARY KEY,
    title text,
    content TEXT,
    user_id int,
    views int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade 
);

INSERT INTO  users (username,email) VALUES ('user1','email1');
INSERT INTO  users (username,email) VALUES ('user2','email2');
INSERT INTO  users (username,email) VALUES ('user3','email3');


INSERT INTO user_posts (title,content,views,user_id) VALUES ('title1','this is content',10,1);
INSERT INTO user_posts (title,content,views,user_id) VALUES ('title2','this is content',20,2);
INSERT INTO user_posts (title,content,views,user_id) VALUES ('title3','this is content',300,1);
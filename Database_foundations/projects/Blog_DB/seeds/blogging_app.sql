DROP TABLE if EXISTS users cascade;
drop sequence if EXISTS users_id_seq;
CREATE sequence IF NOT EXISTS users_id_seq;

DROP TABLE if EXISTS posts;
drop sequence if EXISTS posts_id_seq;
CREATE sequence IF NOT EXISTS posts_id_seq;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE tags(
  post_id = int,
  users_id 
)

INSERT INTO users (email,username) VALUES ('email1','username1');
INSERT INTO users (email,username) VALUES ('email2','username2');
INSERT INTO users (email,username) VALUES ('email3','username3');

INSERT INTO posts (title,content,views,user_id) VALUES ('title1','content1',10,1);
INSERT INTO posts (title,content,views,user_id) VALUES ('title2','content2',20,2);
INSERT INTO posts (title,content,views,user_id) VALUES ('title3','content3',30,1);
INSERT INTO posts (title,content,views,user_id) VALUES ('title4','content4',100,3);
INSERT INTO posts (title,content,views,user_id) VALUES ('title5','content5',4000,1);
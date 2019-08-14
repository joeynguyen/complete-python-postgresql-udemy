CREATE TABLE USERS (
  id SERIAL PRIMARY KEY,
  email text,
  first_name text,
  last_name text,
  oauth_token text,
  oauth_token_secret text
);

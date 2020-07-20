-- Initialize the database.
-- create tables if they don't exist


CREATE TABLE IF NOT EXISTS processed_messages (
  message_id TEXT,
  message_author TEXT,
  channel TEXT,
  moderator TEXT,
  tagged TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

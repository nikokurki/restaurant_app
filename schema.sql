CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	is_admin BOOL
);
CREATE TABLE restaurants (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	address TEXT
);
CREATE TABLE ratings ( 
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE, 
	content TEXT, 
	rating INTEGER, 
	user_id INTEGER REFERENCES users, 
	sent_at TIMESTAMP,
	visible BOOL
);
CREATE TABLE info (
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE,
	description TEXT,
	open_hours TEXT
);
CREATE TABLE restaurant_groups (
    id SERIAL PRIMARY KEY,
	category TEXT,
	restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE
);

	

	
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
);
CREATE TABLE restaurants (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	longitude FLOAT,
	latitude FLOAT
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
CREATE TABLE admins (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users
);
	
	

	
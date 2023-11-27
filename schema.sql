CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
);
CREATE TABLE restaurants (
	id SERIAL PRIMARY KEY,
	name TEXT,
	longitude FLOAT,
	latitude FLOAT
);
CREATE TABLE ratings ( 
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants, 
	content TEXT, 
	rating INTEGER, 
	user_id INTEGER REFERENCES users, 
	sent_at TIMESTAMP
);
CREATE TABLE info (
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants,
	description TEXT,
	open_hours TEXT
);
CREATE TABLE restaurant_groups (
    id SERIAL PRIMARY KEY,
	category TEXT UNIQUE,
	restaurant_id INTEGER REFERENCES restaurants
);
	
	

	
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
);
CREATE TABLE ratings ( 
	rating_id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants, 
	content TEXT, 
	rating INTEGER, 
	user_id INTEGER REFERENCES users, 
	sent_at TIMESTAMP
);
CREATE TABLE restaurants (
	restaurant_id SERIAL PRIMARY KEY,
	name TEXT,
	location FLOAT
);

CREATE TABLE info (
	info_id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants,
	description TEXT,
	open_hours TEXT
);
	

	
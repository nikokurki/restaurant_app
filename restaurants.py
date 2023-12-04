from db import db
from sqlalchemy.sql import text
from flask import session

import users


def get_list():
    sql = text("SELECT id, name, longitude, latitude FROM restaurants ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_restaurant_data(restaurant_id):
    sql = text("SELECT I.description, I.open_hours, R.category FROM info I, restaurant_groups R  WHERE I.restaurant_id=:id AND R.restaurant_id=:id")
    result = db.session.execute(sql, {"id":restaurant_id})
    return result.fetchall()


def get_restaurant_name(id):
    result = db.session.execute(text("SELECT name FROM restaurants WHERE id=:id"), {"id":id})
    return result.fetchone()

def get_restaurant_id(name):
    result = db.session.execute(text("SELECT id FROM restaurants WHERE name=:name"), {"name":name})
    return result.fetchone()

def add_restaurant(name,info,longitude,latitude,category):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = text("INSERT INTO restaurants (name, longitude, latitude) VALUES (:name, :longitude, :latitude)")
        db.session.execute(sql, {"name":name, "longitude":longitude, "latitude":latitude })
        db.session.commit()
        id = get_restaurant_id(name)
        add_info(id[0], info)
        add_group(id[0], category)
        return True
    except:
        return False

def add_info(restaurant_id, description):
    open_hours = "Klo 10-22" # Placeholder
    sql = text("INSERT INTO info (restaurant_id, description, open_hours) VALUES (:restaurant_id, :description, :open_hours)")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "description":description, "open_hours":open_hours })
    db.session.commit()
    return True


def add_group(restaurant_id, category):
    sql = text("INSERT INTO restaurant_groups (category, restaurant_id) VALUES (:category, :restaurant_id)")
    db.session.execute(sql, {"category": category, "restaurant_id": restaurant_id})
    db.session.commit()
    return True
    


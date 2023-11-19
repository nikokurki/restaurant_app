from db import db
from sqlalchemy.sql import text

import users


def get_list():
    sql = text("SELECT restaurant_id, name, longitude, latitude FROM restaurants ORDER BY restaurant_id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_restaurantdata(id):
    sql = text("SELECT R.name, I.description, I.open_hours FROM restaurant R, info I WHERE R.restaurant_id = id AND I.restaurant_id = id")
    result = db.session.execute(sql, {"R.restaurant_id":id})
    return result.fetchall()



def add_restaurant(name,longitude,latitude):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO restaurants (name, longitude, latitude) VALUES (:name, :longitude, :latitude)")
    db.session.execute(sql, {"name":name, "longitude":longitude, "latitude":latitude })
    db.session.commit()
    return True

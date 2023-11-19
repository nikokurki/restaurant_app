from db import db
from sqlalchemy.sql import text

import users, restaurants

def get_list(restaurant_id):
    sql = text("SELECT R.content, R.rating, U.username, R.sent_at FROM ratings R, users U WHERE R.restaurant_id=restaurant_id ORDER BY R.rating_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()

def send(restaurant_id, content, rating):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO ratings (restaurant_id, content, rating, user_id, sent_at) VALUES (:restaurant_id, :content, :rating, :user_id, NOW())")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "rating":rating, "content":rating, "user_id":user_id})
    db.session.commit()
    return True


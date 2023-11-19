from db import db
from sqlalchemy.sql import text

import users, restaurants

def get_list(restaurant_id):
    sql = text("SELECT content, rating, user_id, sent_at FROM ratings WHERE restaurant_id=restaurant_id ORDER BY rating_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()

def send(restaurant_id, content, rating):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO ratings (restaurant_id, content, rating, user_id, sent_at) VALUES (:restaurant_id, :content, :rating, :user_id, NOW())")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "rating":rating, "content":content, "user_id":user_id})
    db.session.commit()
    return True


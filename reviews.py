from db import db
from sqlalchemy.sql import text

import users, restaurants

def get_list(restaurant_id):
    sql = text("SELECT R.rating, R.content, U.username, R.sent_at, R.id FROM ratings R, users U WHERE R.restaurant_id=:id AND R.user_id=U.id AND R.visible=TRUE ORDER BY R.id")
    result = db.session.execute(sql, {"id":restaurant_id})
    return result.fetchall()

def send(restaurant_id, content, rating):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO ratings (restaurant_id, content, rating, user_id, sent_at, visible) VALUES (:restaurant_id, :content, :rating, :user_id, NOW(), :visible)")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "rating":rating, "content":content, "user_id":user_id, "visible": True})
    db.session.commit()
    return True

def delete_review(id):
    sql = text("UPDATE ratings SET visible=FALSE WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True


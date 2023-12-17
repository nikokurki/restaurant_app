from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            if user.id == 1:
                if not is_admin(user.id):
                    add_admin(user.id)
            session["user_id"] = user.id
            session["name"] = username
            if is_admin(user.id):
                session["is_admin"] = True
            else:
                session["is_admin"] = False
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["name"]
    del session["is_admin"]




def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        is_admin = False
        sql = text("INSERT INTO users (username,password,is_admin) VALUES (:username,:password,:is_admin)")
        db.session.execute(sql, {"username":username, "password":hash_value, "is_admin":is_admin})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)


def add_admin(id):
    val = True
    sql = text("UPDATE users SET is_admin=:val WHERE id=:id")
    db.session.execute(sql, {"val": val, "id":id})
    db.session.commit()
    return True

def is_admin(id):
    sql = text("SELECT is_admin FROM users WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    result = result.fetchone()
    if result is None:
        return False
    elif result[0]:
        return True
    return False

def get_list():
    sql = text("SELECT id, username, is_admin FROM users ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

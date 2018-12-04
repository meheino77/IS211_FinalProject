#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:18:38 2018

@author: ntcrwlr77
"""

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base


from config import db


def init_db():
    
    from models import User
    
    db.create_all()
    db.session.commit()
    db.session.close()
    

def insert_users():
    
    from models import User
    
    user1 = User("meheino@sbcglobal.net", "fill")
    user2 = User("scheino@gmail.net", "what")
    
    db.session.add(user1)
    db.session.add(user2)
    
    db.session.commit()
    db.session.close()
    
    
    
def insert_user(email, pwrd):
    
    from models import User
    
    user = User(email, pwrd)
    
    
    db.session.add(user)
    
    db.session.commit()
    db.session.close()
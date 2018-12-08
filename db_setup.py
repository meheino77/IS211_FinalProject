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
    
    from models import User, Contact_Info, Registered_Courses, Course_Info
    
    db.create_all()
    db.session.commit()
    db.session.close()
    

def insert_users():
    
    from models import User
    
    user1 = User("Matthew Heino","test1@gmail.net", "fill")
    user2 = User("Paul Trudeu","test2@gmail.net", "what")
    
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
    
def insert_registered():
    
    from models import Registered_Courses
     
    db.session.add(Registered_Courses(1,1))
    db.session.add(Registered_Courses(1,3))
    db.session.add(Registered_Courses(2,2))
    db.session.add(Registered_Courses(2,4))
    
    db.session.commit()
    db.session.close()

    
def insert_contact():
    
    from models import Contact_Info
    
    contact1 = Contact_Info(1, "126 Tower Way", "AnyTown", "OfConfusion", 
                            "(516) 887-2030")
    
    contact2 = Contact_Info(2, "12 Peaceful Rd.", "Tiny Village", "OfDenial",
                            "(718) 997-2030")
    
    db.session.add(contact1)
    db.session.add(contact2)
    
    db.session.commit()
    db.session.close()
    
def insert_course_info():
    
    from models import Course_Info
    
    course1 = Course_Info("MATH", "120", "Algebra")
    course2 = Course_Info("CS", "211", "Programming 2")
    course3 = Course_Info("HIST", "211", "Western Civilization")
    course4 = Course_Info("ART", "100", "Art History")
    
    
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    
    
    db.session.commit()
    db.session.close()
    
    
    
    
    
    
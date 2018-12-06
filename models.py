#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:17:01 2018

@author: ntcrwlr77
"""

from config import db

class User(db.Model):
    
    __tabelname__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    
    
    def __init__(self, nme, email, pwrd):
        
        self.name = nme
        self.email = email
        self.password = pwrd
        
    def __repr__(self):
        return "User: {} >".format(self.name)
    
#add contact info class
class Contact_Info(db.Model):
    
    __tablename__ = 'contact_info'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    phone = db.Column(db.String)
    
    
    def __init__(self, uid, addr, cty, stte, phne):
        
        self.user_id = uid
        self.address = addr
        self.city = cty
        self.state = stte
        self.phone = phne
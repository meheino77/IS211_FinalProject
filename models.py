#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:17:01 2018

@author: ntcrwlr77
"""

from config import db

class User(db.Model):
    
    __tabelname__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    
    def __init__(self, email, pwrd):
        self.email = email
        self.password = pwrd
        
    def __repr__(self):
        return "User: {} >".format(self.name)
    
#add contact info class
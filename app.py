#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from flask import render_template, request, flash, redirect, url_for

from config import app
from db_setup import init_db, insert_user, insert_users 
from forms import LoginForm
from models import User



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    #return "Welcome"
    
    form = LoginForm()
    
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            
            isthere = User.query.filter_by(email=form.username.data, password=form.password.data).first()
    
            if isthere is not None:
                #return "POST" + isthere.email + " " + isthere.password
                return redirect(url_for('main_page'))
            else:
                return "User not found"
                


@app.route('/main_page', methods=['GET','POST'])
def main_page():
    
   # return "IN INDEX"
    return render_template('dashboard.html')

def intialize_database():
    
    init_db()
    insert_users()
    insert_user("gpheino@msn.com", "simple")
    
if __name__ == '__main__':
    
    intialize_database()
    
    app.run(debug=False)
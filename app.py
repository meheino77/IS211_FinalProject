#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from flask import render_template, request, flash, redirect, url_for, session

from config import app
from db_setup import init_db, insert_user, insert_users 
from forms import LoginForm
from models import User



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    
    form = LoginForm()
    
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            
            isthere = User.query.filter_by(email=form.username.data, password=form.password.data).first()
    
            if isthere is not None:
                
                #return "POST" + isthere.email + " " + isthere.password
                session["user_id"] = isthere.id
                session["logged_in"] = True
                return redirect(url_for('main_page'))
            else:
                return "User not found"
                
@app.route('/log_out',methods=['GET','POST'])
def log_out():
    
    session.pop('logged_in', None)
    session.pop('user_id', None)
    
    return redirect(url_for('index'))
    

@app.route('/main_page', methods=['GET','POST'])
def main_page():
    
    flash("You are logged in! ")
    return render_template('dashboard.html')


@app.route('/view_contact', methods=['GET','POST'])
def view_contact():
    
   # return "Session ID: " + str(session["user_id"]) 
    
    
   if request.method == "GET":
       ses = str(session['user_id']) 
       yorn = session['logged_in']
       
       #isContact
       flash("You Are seeing a get request")
       return render_template ('view_contact.html', sess=ses, logged_in = yorn,
                               name='Matthew Heino', address="126 Popple Bridge Rd",
                               city='Griswold', state='CT')
       
       #n render_template ('view_contact.html')


def intialize_database():
    
    init_db()
    insert_users()
    insert_user("gpheino@msn.com", "simple")
    
if __name__ == '__main__':
    
    intialize_database()
    
    app.run(debug=True)
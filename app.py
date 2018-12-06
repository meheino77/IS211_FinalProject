#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from flask import render_template, request, flash, redirect, url_for, session

from config import app
from db_setup import init_db, insert_user, insert_users, insert_contact
from forms import LoginForm, Update_Info
from models import User, Contact_Info
from config import db



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    
    form = LoginForm()
    
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            
            user= User.query.filter_by(email=form.username.data, password=form.password.data).first()
           
            
            if user is not None:
                #return "POST" + isthere.email + " " + isthere.password
                session["user_id"] = user.id
                session["logged_in"] = True
                session["name"] = user.name
                
                """ 
                ---------for updates do not remove**************
                user.password = "UPDATED" *
                db.session.commit()
                db.session.close()
                """
                
                return redirect(url_for('main_page'))
            else:
                return "User not found"
                
@app.route('/log_out',methods=['GET','POST'])
def log_out():
    
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('name', None)
    
    return redirect(url_for('index'))
    

@app.route('/main_page', methods=['GET','POST'])
def main_page():
    
    flash("You are logged in! ")
    return render_template('dashboard.html')

@app.route('/view_contact', methods=['GET','POST'])
def view_contact():
    
   # return "Session ID: " + str(session["user_id"]) 
    
   form = Update_Info()   
   ses = str(session['user_id']) 
   yorn = session['logged_in']
   nme = session['name']
       
   contact = Contact_Info.query.filter_by(user_id  = int(ses)).first()
   
   if request.method == "GET":
       """
       ses = str(session['user_id']) 
       yorn = session['logged_in']
       nme = session['name']
       
       contact = Contact_Info.query.filter_by(user_id  = int(ses)).first()
       """
       
       return render_template ('view_contact.html', sess=ses, logged_in = yorn,
                               loginname = nme, name= nme, 
                               address=contact.address,
                               city=contact.city, state=contact.state, 
                               phone = contact.phone, form=form)
       
   elif request.method == "POST":
       
       addr = form.address.data
       cty = form.city.data
       stte = form.state.data
       phne = form.phone.data
       
       contact.address = addr
       contact.city = cty
       contact.state = stte
       contact.phone = phne
       
       db.session.commit()
       db.session.close()
       
       return redirect(url_for('view_contact'))
   else:
       return "There has been an error!"
        
        
        
       
def intialize_database():
    
    init_db()
    insert_users()
    insert_contact()
   
    # insert_user("gpheino@msn.com", "simple")
    
if __name__ == '__main__':
    
    intialize_database()
    
    app.run(debug=False)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from flask import render_template, request, flash, redirect, url_for, session

from config import app
from db_setup import init_db,insert_users, insert_contact, insert_course_info, insert_registered, insert_available
from forms import LoginForm, Update_Info
from models import User, Contact_Info, Registered_Courses, Course_Info, Available_Courses
from config import db
from sqlalchemy_utils import database_exists



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    
    form = LoginForm()
    
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            
            user= User.query.filter_by(email=form.username.data, 
                                       password=form.password.data).first()
           
            
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
    
    flash("You are now logged out.")
    return redirect(url_for('index'))
    

@app.route('/main_page', methods=['GET','POST'])
def main_page():
    
    flash("You are logged in! ")
    return render_template('dashboard.html')


@app.route('/register_classes', methods=['GET','POST'])
def register_classes():
    
    departments = ['MATH','CS','ART','HIST']
    
    
    if request.method == "GET":
        #return "Entered register courses!"
       return render_template ('Register_Courses.html', departments=departments)
    elif request.method == "POST":
        
        if request.form.get("search_classes") != None:
            dpt = request.form["department"]
           
            classes = db.session.query(Available_Courses.id, Available_Courses.course_id,Course_Info.dept, Course_Info.courseNum, Course_Info.courseTitle).join(Course_Info, Available_Courses.course_id == Course_Info.id).filter(Course_Info.dept == dpt)
            
            return render_template ('Register_Courses.html', departments=departments, classes=classes)
            #cnt = classes.count()
            #return str(cnt)
        else:
            course = request.form["Register_class"]
            db.session.add(Registered_Courses(session['user_id'], course))
            db.session.commit()
            
            return redirect(url_for('view_schedule'))
            
            #return "Inner else" + str(course)
    else:
        return "Else"
       
        
@app.route('/view_contact', methods=['GET','POST'])
def view_contact():
    
   # return "Session ID: " + str(session["user_id"]) 
    
   form = Update_Info()   
   ses = str(session['user_id']) 
   yorn = session['logged_in']
   nme = session['name']
       
   contact = Contact_Info.query.filter_by(user_id  = int(ses)).first()
   
   if request.method == "GET":
       
   
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

@app.route('/view_schedule', methods=['GET','POST'])
def view_schedule():
    
    ses = session['user_id']
    
    classes =  db.session.query(Registered_Courses.id, Registered_Courses.course_id, Course_Info.dept, Course_Info.courseNum, Course_Info.courseTitle).join(Course_Info, Registered_Courses.course_id == Course_Info.id).filter(Registered_Courses.user_id == ses)
    
    if request.method == "GET":
        """
        count = test1.count()
        return "ENTERED GET" + str(ses) + str(count)
        """
        return render_template ('view_schedule.html', classes=classes)
    else:
        
        if request.form.get('delete_all_classes'):
            db.session.query(Registered_Courses).filter(Registered_Courses.user_id == ses).delete()
            db.session.commit()
        else:
            id_num = request.form.get('delete_class')
            Registered_Courses.query.filter(Registered_Courses.id == id_num).delete()
            db.session.commit() 
        return redirect(url_for('view_schedule'))
        
        
def intialize_database():
    
    if database_exists("sqlite:///studentadmin.db") is False:
        init_db()
        insert_users()
        insert_contact()
        insert_course_info()
        insert_registered()
        insert_available()
    # insert_user("gpheino@msn.com", "simple")
    
if __name__ == '__main__':
    
    intialize_database()
    
    app.run(debug=False)
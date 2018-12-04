#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from flask import render_template, request, flash

from config import app
from db_setup import init_db, insert_user, insert_users 
from forms import LoginForm



@app.route('/', methods=['GET','POST'])
def main():
    #return "Welcome"
    
    form = LoginForm()
    
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            data = form.username.data
            return "POST" + data


@app.route('/index')
def index():
    
    return "IN INDEX"

if __name__ == '__main__':
    
    #init_db()
    #insert_users()
    #insert_user("gpheino@msn.com", "simple")
    
    app.run(debug=True)
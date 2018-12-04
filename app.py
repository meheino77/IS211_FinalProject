#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""

from config import app
from db_setup import init_db, insert_user, insert_users 





@app.route('/')
def test():
    return "Welcome"



if __name__ == '__main__':
    
    init_db()
    insert_users()
    insert_user("gpheino@msn.com", "simple")
    
    app.run()
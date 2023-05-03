# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:47:35 2023

@author: wang'shi'yu
"""

import psycopg2
def AddUser(user_id,password,birthday,email,phone_number):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    #sql="""SELECT*FROM public."User" where "User".user_id=%s"""
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        sql="""INSERT INTO "User" (user_id,password,birthday,email,phone_number) VALUES(%s,%s,%s,%s,%s);"""
        c=(user_id,password,birthday,email,phone_number,)
        cur.execute(sql,c)
        conn.commit()
    if rows!=[]:
        raise Exception('reduplicated user_id error')
    #print(rows)
    conn.close()
    #return rows

def GetUserInfo(user_id):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    #print(type(rows))
    #print(rows)
    conn.close()
    birthday=rows[0][4]
    phone_number=rows[0][3]
    email=rows[0][5]
    return birthday,phone_number,email


def LoginUser(user_id,password):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    else:
        if rows[0][2]!=password:
            raise Exception('user_id or password error')
    conn.close()
            
    
def DeleteUser(user_id):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    else:
        sql ="""delete FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        cur.execute(sql,c)
        conn.commit()
    conn.close()
    
def UpdateUserInfo(user_id,birthday,phone_number,email):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    else:
        sql ="""update "User" set birthday= %s,phone_number=%s,email=%s where "User".user_id = %s;"""
        c=(birthday,phone_number,email,user_id,)
        cur.execute(sql,c)
        conn.commit()
    conn.close()
        
def GetDeviceInfo(user_id):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    else:
        sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
        c=(user_id,)
        cur.execute(sql,c)
        dev=cur.fetchall()
        if dev==[]:
            raise Exception('device not exists error')
        #conn.commit()
    conn.close()
    ip=dev[0][0]
    port=dev[0][3]
    return ip,port

def BindDevice(user_id,IP,Port):
    conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
    cur = conn.cursor()
    sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
    c=(user_id,)
    cur.execute(sql,c)
    rows = cur.fetchall()
    if rows==[]:
        raise Exception('user not exists error')
    else:
        sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
        c=(user_id,)
        cur.execute(sql,c)
        dev=cur.fetchall()
        if dev!=[]:
            raise Exception('device repeat binding error')
        else:
            sql ="""INSERT INTO public."Device" (owner,ip,port) VALUES(%s,%s,%s);"""
            c=(user_id,IP,Port,)
            cur.execute(sql,c)
            conn.commit()
    conn.close()

def UnbindDevice(user_id):
     conn = psycopg2.connect(database="production", user="postgres", password="123456", host="localhost", port="63091")
     cur = conn.cursor()
     sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
     c=(user_id,)
     cur.execute(sql,c)
     rows = cur.fetchall()
     if rows==[]:
         raise Exception('user not exists error')
     else:
         sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
         c=(user_id,)
         cur.execute(sql,c)
         dev=cur.fetchall()
         if dev==[]:
             raise Exception('device not exists error')
         else:
             sql="""delete FROM public."Device" where "Device".owner=%s;"""
             c=(user_id,)
             cur.execute(sql,c)
             conn.commit()
     conn.close()
  
        

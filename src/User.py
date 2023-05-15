# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:47:35 2023

@author: wang'shi'yu
"""

import psycopg2

class Database():
    def __init__(self,DATABASE,USER,PASSWORD,HOST,PORT):
        self.DATABASE=DATABASE
        self.USER=USER
        self.PASSWORD=PASSWORD
        self.HOST=HOST
        self.PORT=PORT
    
    #Connect the database
    def Connect(self):
        try:
            conn=psycopg2.connect(database=self.DATABASE,user=self.USER,password=self.PASSWORD,host=self.HOST,port=self.PORT)            
        except Exception as e:
            raise Exception("connect error.")
        return conn
    
    def AddUser(self,user_id,password,birthday,email,phone_number):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
            
        cur = conn.cursor()
        #sql="""SELECT*FROM public."User" where "User".user_id=%s"""
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            sql="""INSERT INTO "User" (user_id,password,birthday,email,phone_number) VALUES(%s,%s,%s,%s,%s);"""
            c=(user_id,password,birthday,email,phone_number,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        if rows!=[]:
            raise Exception('reduplicated user_id error')
        #print(rows)
        conn.close()
        #return rows
        
        
    def ChangePassword(self,user_id,password):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            sql ="""update "User" set password=%s where "User".user_id = %s;"""
            c=(password,user_id,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()
        
    def GetUserInfo(self,user_id):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)  
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
    
    
    def LoginUser(self,user_id,password):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
            
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            if rows[0][2]!=password:
                raise Exception('user_id or password error')
        conn.close()
                
        
    def DeleteUser(self,user_id):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            sql ="""delete FROM public."User" where "User".user_id=%s;"""
            c=(user_id,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()
        
    def UpdateUserInfo(self,user_id,birthday,phone_number,email):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            sql ="""update "User" set birthday= %s,phone_number=%s,email=%s where "User".user_id = %s;"""
            c=(birthday,phone_number,email,user_id,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()
            
    def GetDeviceInfo(self,user_id):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
            c=(user_id,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            dev=cur.fetchall()
            if dev==[]:
                raise Exception('device not exists error')
            #conn.commit()
        conn.close()
        ip=dev[0][0]
        port=dev[0][3]
        return ip,port
    
    def BindDevice(self,user_id,IP,Port):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
        c=(user_id,)
        try:
            cur.execute(sql,c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows==[]:
            raise Exception('user not exists error')
        else:
            sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
            c=(user_id,)
            try:
                cur.execute(sql,c)
            except Exception as e:
                raise Exception(e)
            dev=cur.fetchall()
            if dev!=[]:
                raise Exception('device repeat binding error')
            else:
                sql ="""INSERT INTO public."Device" (owner,ip,port) VALUES(%s,%s,%s);"""
                c=(user_id,IP,Port,)
                cur.execute(sql,c)
                conn.commit()
        conn.close()
    
    def UnbindDevice(self,user_id):
         try:
            conn =self.Connect()
         except Exception as e:
            raise Exception(e)
         cur = conn.cursor()
         sql="""SELECT * FROM public."User" where "User".user_id=%s;"""
         c=(user_id,)
         try:
             cur.execute(sql,c)
         except Exception as e:
             raise Exception(e)
         rows = cur.fetchall()
         if rows==[]:
             raise Exception('user not exists error')
         else:
             sql ="""SELECT * FROM public."Device" where "Device".owner=%s;"""
             c=(user_id,)
             try:
                 cur.execute(sql,c)
             except Exception as e:
                 raise Exception(e)
                 
             dev=cur.fetchall()
             if dev==[]:
                 raise Exception('device not exists error')
             else:
                 sql="""delete FROM public."Device" where "Device".owner=%s;"""
                 c=(user_id,)
                 try:
                     cur.execute(sql,c)
                 except Exception as e:
                     raise Exception(e)
                 conn.commit()
         conn.close()
      
        

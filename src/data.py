# -*- coding: utf-8 -*-

"""
@author: still(Lizhenhe)
"""

import json
import numpy as np
import torch
import psycopg2
import datetime as d
import time
import os
import pickle

ip="192.168.186.129"
port="54333"

def GetMotionData(user_id):


    conn = psycopg2.connect(database="production", user="postgres", password="123456", host=ip,
                            port=port)

    cursor = conn.cursor()

    try:
        sql = """ SELECT * FROM public."User" where "User".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        res = cursor.fetchall()
        if (res == []):
            raise Exception('user not exists error')

        sql = """ SELECT "data_sensed_by_six_multiply_nine","label" FROM public."Frame" where "Frame".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        res=cursor.fetchall()



        num=len(res)
        if(num%5!=0):
            num1=num-num%5
        else: num1=num
        ans = np.zeros(shape=[num1,56])


        #print(res[1][0].values())
        for i in range(num1):
            l=[]
            temp=res[i][0]
            for item in temp:
                if(item!="timestamp"):
                    for item1 in temp[item]:
                        l.append(temp[item][item1])
                else: l.append(temp[item])
            l.append(res[i][1])
            ans[i]=l


        ans=ans.reshape((-1,5,56))


        print("successfully")

        conn.commit()

        conn.close()
        return ans
    except Exception as e:
        print(e)


def DeleteMotionRecord(user_id,create_time):

    conn = psycopg2.connect(database="production", user="postgres", password="123456", host=ip,
                            port=port)

    cursor = conn.cursor()

    try:

        sql = """ SELECT * FROM public."User" where "User".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        res = cursor.fetchall()
        if(res==[]):
            raise Exception('user not exists error')

        sql = """ SELECT * FROM public."MotionRecord" where "MotionRecord".user_id=%s and "MotionRecord".created_time=%s """
        params = (user_id,create_time)
        cursor.execute(sql, params)
        res = cursor.fetchall()
        if (res == []):
            raise Exception('motion record not exists error')

        sql = """ SELECT * FROM public."MotionRecord" where user_id=%s and created_time=%s """
        params = (user_id, create_time)
        cursor.execute(sql, params)
        res = cursor.fetchall()
        lower_bound=res[0][3]
        upper_bound=res[0][4]

        sql = """  DELETE FROM public."Frame" where user_id=%s and time_stamp>=%s and time_stamp<=%s """
        params = (user_id, lower_bound,upper_bound)
        cursor.execute(sql, params)

        sql = """ DELETE FROM public."MotionRecord" where user_id=%s and created_time=%s """
        params = (user_id,create_time)
        cursor.execute(sql, params)
        #res = cursor.fetchall()



        print("successfully")

        conn.commit()

        conn.close()
    except Exception as e:
        raise Exception("unknown error")

def SaveMotionData(user_id,create_time,label,res):
    #res is a dict(input data)


    conn = psycopg2.connect(database="production", user="postgres", password="123456", host=ip,
                            port=port)

    cursor = conn.cursor()

    try:

        sql = """ SELECT * FROM public."User" where "User".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        data = cursor.fetchall()
        if (data == []):
            raise Exception('user not exists error')
        num=len(res)
        lower_bound=res[0]['timestamp']
        upper_bound=res[num-1]['timestamp']

        sql = """ INSERT INTO "MotionRecord"(user_id,created_time,label,lower_bound,upper_bound) VALUES (%s,%s,%s,%s,%s)"""
        params = (user_id,create_time, label, lower_bound,upper_bound)
        cursor.execute(sql, params)

        for i in range(num):
            sql = """ INSERT INTO "Frame"(user_id,time_stamp,data_sensed_by_six_multiply_nine,label) VALUES (%s,%s,%s,%s)"""
            params = (user_id, res[i]['timestamp'],json.dumps(res[i]),label)
            cursor.execute(sql, params)
        #res = cursor.fetchall()




        print("successfully")

        conn.commit()

        conn.close()
    except Exception as e:
        raise Exception("unknown error")


def GetMotionRecord(user_id):

    conn = psycopg2.connect(database="production", user="postgres", password="123456", host=ip,
                            port=port)

    cursor = conn.cursor()

    try:

        sql = """ SELECT * FROM public."User" where "User".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        data = cursor.fetchall()
        if (data == []):
            raise Exception('user not exists error')



        sql = """SELECT * FROM public."MotionRecord" where "MotionRecord".user_id=%s"""
        params = ( user_id)
        cursor.execute(sql, params)
        data = cursor.fetchall()
        label=[]
        create_time=[]
        last_time=[]
        begin=[]
        end=[]


        for i in range(len(data)):
            label.append(data[i][0])

            create_time.append(data[i][1])
            begin.append(data[i][3])
            end.append(data[i][4])
            last_time.append(data[i][4]-data[i][3])

        print("successfully")



        conn.commit()

        conn.close()
        return label,create_time,last_time
    except Exception as e:
        raise Exception("unknown error")

def ModifyMotionRecord(user_id,create_time,label):

    conn = psycopg2.connect(database="production", user="postgres", password="123456", host=ip,
                            port=port)

    cursor = conn.cursor()

    try:

        sql = """ SELECT * FROM public."User" where "User".user_id=%s """
        params = (user_id)
        cursor.execute(sql, params)
        data = cursor.fetchall()
        if (data == []):
            raise Exception('user not exists error')

        if(label<0 or label>7):
            raise Exception('label invalid error')

        sql = """ SELECT * FROM public."MotionRecord" where user_id=%s and created_time=%s """
        params = (user_id, create_time)
        cursor.execute(sql, params)
        res = cursor.fetchall()
        lower_bound = res[0][3]
        upper_bound = res[0][4]

        sql = """update "Frame" set label= %s where "Frame".user_id = %s and "Frame".time_stamp>=%s and "Frame".time_stamp<=%s """
        params = (label, user_id,lower_bound,upper_bound)
        cursor.execute(sql, params)

        sql = """update "MotionRecord" set label= %s where "MotionRecord".user_id = %s and "MotionRecord".created_time=%s"""
        params = (label,user_id,create_time)
        cursor.execute(sql, params)
        print("successfully")

        conn.commit()

        conn.close()
    except Exception as e:
        raise Exception("unknown error")




def CleanData(data):
    k=data.shape[0]
    if(k==5): return data
    if(k<3):
        raise Exception("clean-data failure(k<3)")
    res=np.zeros((5,55))
    for i in range(1,k):
        internal=data[i][54]-data[i-1][54]
        if(internal>0.25):
            raise Exception("clean-data failure(interval >0.20)")
    for i in range(k):
        res[i]=data[i]
    for i in range(k,5):
        res[i][54]=res[i-1][54]+0.20
    if(k==3):
        x0= data[0][54]
        x1 = data[1][54]
        x2 = data[2][54]
        x3=res[3][54]
        x4=res[4][54]
        for i in range(54):
            y0=data[0][i]
            y1=data[1][i]
            y2=data[2][i]
            y3=((x3-x1)*(x3-x2))/((x0-x1)*(x0-x2))*y0+((x3-x0)*(x3-x2))/((x1-x0)*(x1-x2))*y1+((x3-x0)*(x3-x1))/((
                    x2 -x0)*(x2-x1))*y2
            y4=((x4-x1)*(x4-x2))/((x0-x1)*(x0-x2))*y0+((x4-x0)*(x4-x2))/((x1-x0)*(x1-x2))*y1+((x4-x0)*(x4-x1))/((
                    x2 -x0)*(x2-x1))*y2
            res[3][i]=y3
            res[4][i]=y4
    elif(k==4):
        x0 = data[0][54]
        x1 = data[1][54]
        x2 = data[2][54]
        x3 = data[3][54]
        x4 = res[4][54]
        for i in range(54):
            y0 = data[0][i]
            y1 = data[1][i]
            y2 = data[2][i]
            y3=data[3][i]
            y4=((x4-x1)*(x4-x2)*(x4-x3))/((x0-x1)*(x0-x2)*(x0-x3))*y0  + ((x4-x0)*(x4-x2)*(x4-x3))/((x1-x0)*(x1-x2)
                *(x1-x3))*y1  +  ((x4-x0)*(x4-x1)*(x4-x3))/((x2-x0)*(x2-x1)*(x2-x3))*y2  +  ((x4-x0)*(x4-x1)*(x4-x2))/((
                x3-x0)*(x3-x1)*(x3-x2))*y3
            res[4][i]=y4

        return res


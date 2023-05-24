# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:54:09 2023

@author: wang'shi'yu 、li`zhen`he
"""


import psycopg2
import os
import pickle
import json
import numpy as np

class Database():
    def __init__(self, DATABASE='production', USER='postgres', PASSWORD='123456', HOST='liyu.utad.pt', PORT='55332'):
        self.DATABASE = DATABASE
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.PORT = PORT

    # Connect the database
    def Connect(self):
        try:
            conn = psycopg2.connect(database=self.DATABASE, user=self.USER, password=self.PASSWORD, host=self.HOST,
                                    port=self.PORT)
        except Exception as e:
            raise Exception("connect error.")
        return conn
    
    def GetallUser(self):
        try:
            conn =self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql="""SELECT user_id FROM public."User";"""
        cur.execute(sql)
        rows=cur.fetchall()
        return rows
    
    def AddManger(self,user_id,password,birthday,email,phone_number):
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
            sql="""INSERT INTO "User" (user_id,password,birthday,email,phone_number,user_type) VALUES(%s,%s,%s,%s,%s,%s);"""
            user_type=1
            c=(user_id,password,birthday,email,phone_number,user_type,)
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
    
    def LoginManger(self,user_id,password):
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
            if rows[0][1]!=password:
                raise Exception('user_id or password error')
        conn.close()
        user_type=rows[0][5]
        if user_type!=1 and user_type!=0:
            raise Exception("not manager or admin error")
        return user_type
    
    def AddUser(self, user_id, password, birthday, email, phone_number):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cur = conn.cursor()
        # sql="""SELECT*FROM public."User" where "User".user_id=%s"""
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            sql = """INSERT INTO "User" (user_id,password,birthday,email,phone_number,user_type) VALUES(%s,%s,%s,%s,%s,%s);"""
            user_type=2
            c=(user_id,password,birthday,email,phone_number,user_type,)
            
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        if rows != []:
            raise Exception('reduplicated user_id error')
        # print(rows)
        conn.close()
        # return rows

    def ChangePassword(self, user_id, password):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """update "User" set password=%s where "User".user_id = %s;"""
            c = (password, user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()

    def GetUserInfo(self, user_id):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        # print(type(rows))
        # print(rows)
        conn.close()
        birthday = rows[0][2]
        phone_number = rows[0][3]
        email = rows[0][4]
        user_type=rows[0][5]
        return birthday, phone_number, email,user_type

    def LoginUser(self, user_id, password):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            if rows[0][1] != password:
                raise Exception('user_id or password error')
        conn.close()

    def DeleteUser(self, user_id):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """delete FROM public."User" where "User".user_id=%s;"""
            c = (user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()

    def UpdateUserInfo(self, user_id, birthday, phone_number, email):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """update "User" set birthday= %s,phone_number=%s,email=%s where "User".user_id = %s;"""
            c = (birthday, phone_number, email, user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            conn.commit()
        conn.close()

    def GetDeviceInfo(self, user_id):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """SELECT * FROM public."Device" where "Device".owner=%s;"""
            c = (user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            dev = cur.fetchall()
            if dev == []:
                raise Exception('device not exists error')
            # conn.commit()
        conn.close()
        ip = dev[0][1]
        port = dev[0][2]
        return ip, port

    def BindDevice(self, user_id, IP, Port):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """SELECT * FROM public."Device" where "Device".owner=%s;"""
            c = (user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)
            dev = cur.fetchall()
            if dev != []:
                raise Exception('device repeat binding error')
            else:
                sql = """INSERT INTO public."Device" (owner,ip,port) VALUES(%s,%s,%s);"""
                c = (user_id, IP, Port,)
                cur.execute(sql, c)
                conn.commit()
        conn.close()

    def UnbindDevice(self, user_id):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)
        cur = conn.cursor()
        sql = """SELECT * FROM public."User" where "User".user_id=%s;"""
        c = (user_id,)
        try:
            cur.execute(sql, c)
        except Exception as e:
            raise Exception(e)
        rows = cur.fetchall()
        if rows == []:
            raise Exception('user not exists error')
        else:
            sql = """SELECT * FROM public."Device" where "Device".owner=%s;"""
            c = (user_id,)
            try:
                cur.execute(sql, c)
            except Exception as e:
                raise Exception(e)

            dev = cur.fetchall()
            if dev == []:
                raise Exception('device not exists error')
            else:
                sql = """delete FROM public."Device" where "Device".owner=%s;"""
                c = (user_id,)
                try:
                    cur.execute(sql, c)
                except Exception as e:
                    raise Exception(e)
                conn.commit()
        conn.close()


    def GetMotionData(self,user_id):

        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:
            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            res = cursor.fetchall()
            if (res == []):
                raise Exception('user not exists error')

            sql = """ SELECT "data_sensed_by_six_multiply_nine","label" FROM public."Frame" where "Frame".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            res = cursor.fetchall()

            num = len(res)
            if (num % 5 != 0):
                num1 = num - num % 5
            else:
                num1 = num
            ans = np.zeros(shape=[num1, 56])

            # print(res[1][0].values())
            for i in range(num1):
                l = []
                temp = res[i][0]
                for item in temp:
                    if (item != "timestamp"):
                        for item1 in temp[item]:
                            l.append(temp[item][item1])
                    else:
                        l.append(temp[item])
                l.append(res[i][1])
                ans[i] = l

            ans = ans.reshape((-1, 5, 56))

            print("successfully")

            conn.commit()

            conn.close()
            return ans
        except Exception as e:
            print(e)

    def DeleteMotionRecord(self,user_id, create_time):

        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            res = cursor.fetchall()
            if (res == []):
                raise Exception('user not exists error')

            sql = """ SELECT * FROM public."MotionRecord" where "MotionRecord".user_id=%s and "MotionRecord".create_time=%s """
            params = (user_id, create_time,)
            cursor.execute(sql, params)
            res = cursor.fetchall()
            if (res == []):
                raise Exception('motion record not exists error')

            sql = """ SELECT * FROM public."MotionRecord" where user_id=%s and create_time=%s """
            params = (user_id, create_time,)
            cursor.execute(sql, params)
            res = cursor.fetchall()
            lower_bound = res[0][3]
            upper_bound = res[0][4]

            sql = """  DELETE FROM public."Frame" where user_id=%s and time_stamp>=%s and time_stamp<=%s """
            params = (user_id, lower_bound, upper_bound,)
            cursor.execute(sql, params)

            sql = """ DELETE FROM public."MotionRecord" where user_id=%s and create_time=%s """
            params = (user_id, create_time,)
            cursor.execute(sql, params)

            print("successfully")

            conn.commit()

            conn.close()
        except Exception as e:
            raise Exception("unknown error")

    def SaveMotionData(self,user_id, create_time, label, res):
        # res is a dict(input data)

        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')
            num = len(res)
            lower_bound = res[0]['timestamp']
            upper_bound = res[num - 1]['timestamp']

            sql = """ INSERT INTO "MotionRecord"(user_id,created_time,label,lower_bound,upper_bound) VALUES (%s,%s,%s,%s,%s)"""
            params = (user_id, create_time, label, lower_bound, upper_bound,)
            cursor.execute(sql, params)

            for i in range(num):
                sql = """ INSERT INTO "Frame"(user_id,time_stamp,data_sensed_by_six_multiply_nine,label) VALUES (%s,%s,%s,%s)"""
                params = (user_id, res[i]['timestamp'], json.dumps(res[i]), label,)
                cursor.execute(sql, params)

            print("successfully")

            conn.commit()

            conn.close()
        except Exception as e:
            raise Exception("unknown error")

    def GetMotionRecord(self,user_id):

        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')

            sql = """SELECT * FROM public."MotionRecord" where "MotionRecord".user_id=%s"""
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            label = []
            create_time = []
            last_time = []
            begin = []
            end = []

            for i in range(len(data)):
                label.append(data[i][2])

                create_time.append(data[i][1])
                begin.append(data[i][3])
                end.append(data[i][4])
                last_time.append(data[i][4] - data[i][3])

            print("successfully")

            conn.commit()

            conn.close()
            return label, create_time, last_time
        except Exception as e:
            raise Exception("unknown error")

    def ModifyMotionRecord(self,user_id, create_time, label):

        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')

            if (label < 0 or label > 7):
                raise Exception('label invalid error')

            sql = """ SELECT * FROM public."MotionRecord" where user_id=%s and create_time=%s """
            params = (user_id, create_time,)
            cursor.execute(sql, params)
            res = cursor.fetchall()
            lower_bound = res[0][3]
            upper_bound = res[0][4]

            sql = """update "Frame" set label= %s where "Frame".user_id = %s and "Frame".time_stamp>=%s and "Frame".time_stamp<=%s """
            params = (label, user_id, lower_bound, upper_bound,)
            cursor.execute(sql, params)

            sql = """update "MotionRecord" set label= %s where "MotionRecord".user_id = %s and "MotionRecord".create_time=%s"""
            params = (label, user_id, create_time,)
            cursor.execute(sql, params)
            print("successfully")

            conn.commit()

            conn.close()
        except Exception as e:
            raise Exception("unknown error")

    def CleanData(self,data):
        k = data.shape[0]
        if (k == 5): return data
        if (k < 3):
            raise Exception("clean-data failure(k<3)")
        res = np.zeros((5, 55))
        for i in range(1, k):
            internal = data[i][54] - data[i - 1][54]
            if (internal > 0.25):
                raise Exception("clean-data failure(interval >0.20)")
        for i in range(k):
            res[i] = data[i]
        for i in range(k, 5):
            res[i][54] = res[i - 1][54] + 0.20
        if (k == 3):
            x0 = data[0][54]
            x1 = data[1][54]
            x2 = data[2][54]
            x3 = res[3][54]
            x4 = res[4][54]
            for i in range(54):
                y0 = data[0][i]
                y1 = data[1][i]
                y2 = data[2][i]
                y3 = ((x3 - x1) * (x3 - x2)) / ((x0 - x1) * (x0 - x2)) * y0 + ((x3 - x0) * (x3 - x2)) / (
                        (x1 - x0) * (x1 - x2)) * y1 + ((x3 - x0) * (x3 - x1)) / ((
                                                                                         x2 - x0) * (x2 - x1)) * y2
                y4 = ((x4 - x1) * (x4 - x2)) / ((x0 - x1) * (x0 - x2)) * y0 + ((x4 - x0) * (x4 - x2)) / (
                        (x1 - x0) * (x1 - x2)) * y1 + ((x4 - x0) * (x4 - x1)) / ((
                                                                                         x2 - x0) * (x2 - x1)) * y2
                res[3][i] = y3
                res[4][i] = y4
        elif (k == 4):
            x0 = data[0][54]
            x1 = data[1][54]
            x2 = data[2][54]
            x3 = data[3][54]
            x4 = res[4][54]
            for i in range(54):
                y0 = data[0][i]
                y1 = data[1][i]
                y2 = data[2][i]
                y3 = data[3][i]
                y4 = ((x4 - x1) * (x4 - x2) * (x4 - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3)) * y0 + (
                        (x4 - x0) * (x4 - x2) * (x4 - x3)) / ((x1 - x0) * (x1 - x2)
                                                              * (x1 - x3)) * y1 + (
                             (x4 - x0) * (x4 - x1) * (x4 - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3)) * y2 + (
                             (x4 - x0) * (x4 - x1) * (x4 - x2)) / ((
                                                                           x3 - x0) * (x3 - x1) * (x3 - x2)) * y3
                res[4][i] = y4

            return res

    def GetUserLog(self,user_id):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')


            sql = """ SELECT * FROM public."Log" where user_id=%s  """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            log_time=[]
            log_content=[]
            for i in range(len(data)):
                log_time.append(data[i][1])
                log_content.append(data[i][2])

            print("successfully")
            conn.commit()
            conn.close()
            return log_time,log_content
        except Exception as e:
            raise Exception("unknown error")

    def ModifyLog(self,user_id,log_time,log_content):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')

            sql = """ SELECT * FROM public."Log" where "Log".user_id=%s and "Log".log_time=%s """
            params = (user_id, log_time,)
            cursor.execute(sql, params)
            data = cursor.fetchall()

            if (data == []):
                raise Exception('log not exists error')

            sql = """ update "Log" set log_content= %s where "Log".user_id = %s and "Log".log_time=%s  """
            params = (log_content,user_id,log_time,)
            cursor.execute(sql, params)



            print("successfully")
            conn.commit()
            conn.close()
            return log_time, log_content
        except Exception as e:
            raise Exception("unknown error")

    def DeleteLog(self,user_id,log_time):
        try:
            conn = self.Connect()
        except Exception as e:
            raise Exception(e)

        cursor = conn.cursor()

        try:

            sql = """ SELECT * FROM public."User" where "User".user_id=%s """
            params = (user_id,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('user not exists error')

            sql = """ SELECT * FROM public."Log" where "Log".user_id=%s and "Log".log_time=%s """
            params = (user_id,log_time,)
            cursor.execute(sql, params)
            data = cursor.fetchall()
            if (data == []):
                raise Exception('log not exists error')

            sql = """ DELETE FROM public."Log" where user_id=%s and log_time=%s """
            params = (user_id, log_time,)
            cursor.execute(sql, params)



            print("successfully")
            conn.commit()
            conn.close()

        except Exception as e:
            raise Exception("unknown error")

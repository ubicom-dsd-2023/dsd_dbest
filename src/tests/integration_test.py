
import psycopg2

from psycopg2.errors import UniqueViolation, NotNullViolation

from datetime import datetime

import pytest


def create_connection():
    return psycopg2.connect(database='production',
                            user='postgres',
                            password='123456',
                            host='liyu.utad.pt',
                            port='55333')


def delete(conn):
    sql = """DELETE from "user" *"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def select_user_by_username(conn, username):
    sql = """SELECT * FROM "user" WHERE username = %s"""
    cur = conn.cursor()
    cur.execute(sql, (username,))
    conn.commit()
    return cur.fetchall()


def test_create_user():
    """
    Should be possible to create a user
    """

    username = "johndoe"
    password = "password"
    phone_number = "123456789"
    birthday = "1990-1-1"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (username, password, phone_number, birthday, email, created_at)

    sql = """INSERT INTO "user"(
                            username, 
                            password, 
                            phone_number, 
                            birthday, 
                            email,
                            created_at)
                            VALUES(%s,%s,%s,%s,%s,%s);"""

    conn = create_connection()

    cur = conn.cursor()
    cur.execute(sql, params)
    cur.close()
    conn.commit()

    response = select_user_by_username(conn, username)

    delete(conn)

    conn.close()

    assert len(response) == 1


def test_create_user_without_email():
    """
    should be possible to create user without email
    """

    username = "johndoe"
    password = "password"
    phone_number = "123456789"
    birthday = "1990-1-1"
    created_at = datetime.now()
    params = (username, password, phone_number, birthday, created_at)

    sql = """INSERT INTO "user"(
                            username, 
                            password, 
                            phone_number, 
                            birthday, 
                            created_at)
                            VALUES(%s,%s,%s,%s,%s);"""

    conn = create_connection()

    cur = conn.cursor()
    cur.execute(sql, params)
    cur.close()
    conn.commit()

    response = select_user_by_username(conn, username)

    delete(conn)

    conn.close()

    assert len(response) == 1


def test_create_user_without_phone_number():
    """
    should be possible to create user without phone number
    """

    username = "johndoe"
    password = "password"
    birthday = "1990-1-1"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (username, password, birthday, email, created_at)

    sql = """INSERT INTO "user"(
                            username, 
                            password, 
                            birthday, 
                            email,
                            created_at)
                            VALUES(%s,%s,%s,%s,%s);"""

    conn = create_connection()

    cur = conn.cursor()
    cur.execute(sql, params)
    cur.close()
    conn.commit()

    response = select_user_by_username(conn, username)

    delete(conn)

    conn.close()

    assert len(response) == 1


def test_create_user_with_same_username():
    """
    should not be possible create a user with same username
    """
    '''with pytest.raises(Error) as exc_info:'''
    username = "johndoe"
    password = "password"
    phone_number = "123456789"
    birthday = "1990-1-1"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (username, password, phone_number, birthday, email, created_at)

    sql = """INSERT INTO "user"(
                                username, 
                                password, 
                                phone_number, 
                                birthday, 
                                email,
                                created_at)
                                VALUES(%s,%s,%s,%s,%s,%s);"""

    conn = create_connection()
    delete(conn)
    cur = conn.cursor()

    with pytest.raises(UniqueViolation) as exc_info:

        cur.execute(sql, params)
        cur.execute(sql, params)

        conn.close()

    assert "already exists" in exc_info.value.pgerror


def test_create_user_without_username():
    """
    should not be possible create a user without username
    """
    '''with pytest.raises(Error) as exc_info:'''
    password = "password"
    phone_number = "123456789"
    birthday = "1990-1-1"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (password, phone_number, birthday, email, created_at)

    sql = """INSERT INTO "user"(password, 
                                phone_number, 
                                birthday, 
                                email,
                                created_at)
                                VALUES(%s,%s,%s,%s,%s);"""

    conn = create_connection()
    delete(conn)
    cur = conn.cursor()

    with pytest.raises(NotNullViolation) as exc_info:
        cur.execute(sql, params)

        conn.close()

        print(exc_info.value)

    assert "violates not-null constraint" in exc_info.value.pgerror


def test_create_user_without_password():
    """
    should not be possible create a user without password
    """
    '''with pytest.raises(Error) as exc_info:'''
    username = "johndoe"
    phone_number = "123456789"
    birthday = "1990-1-1"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (username, phone_number, birthday, email, created_at)

    sql = """INSERT INTO "user"(
                                username, 
                                phone_number, 
                                birthday, 
                                email,
                                created_at)
                                VALUES(%s,%s,%s,%s,%s);"""

    conn = create_connection()
    delete(conn)
    cur = conn.cursor()

    with pytest.raises(NotNullViolation) as exc_info:
        cur.execute(sql, params)

        conn.close()

        print(exc_info.value)

    assert "violates not-null constraint" in exc_info.value.pgerror


def test_create_user_without_birthday():
    """
    should not be possible create a user without birthday
    """
    '''with pytest.raises(Error) as exc_info:'''
    username = "johndoe"
    password = "password"
    phone_number = "123456789"
    email = "user@mail.com"
    created_at = datetime.now()
    params = (username, password, phone_number, email, created_at)

    sql = """INSERT INTO "user"(
                                username, 
                                password, 
                                phone_number, 
                                email,
                                created_at)
                                VALUES(%s,%s,%s,%s,%s);"""

    conn = create_connection()
    delete(conn)
    cur = conn.cursor()

    with pytest.raises(NotNullViolation) as exc_info:

        cur.execute(sql, params)

        conn.close()

    assert "violates not-null constraint" in exc_info.value.pgerror

from typing import Tuple, Any

import psycopg2
from datetime import datetime
import time


def create_connection():
    return psycopg2.connect(database='production',
                            user='postgres',
                            password='123456',
                            host='liyu.utad.pt',
                            port='55333')


def _delete(conn):
    sql = """DELETE from "user" *"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def _create_user(conn, _id):
    sql = """INSERT INTO "user"(
                            username, 
                            password, 
                            phone_number, 
                            birthday, 
                            email, created_at)
                            VALUES(%s,%s,%s,%s,%s,%s);"""

    username = f'name{_id}'
    password = "password"
    phone_number = "123456789"
    birthday_date = "1990-1-1"
    email = "user@mail.com"
    now = datetime.now()

    user = (username, password, phone_number, birthday_date, email, now)

    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()


def create_user(conn, iterations) -> float:
    """
    Create n (iterations) users
    :param conn: Connection database
    :param iterations: number of users to be created
    :return: [float value - time spend, id - last id created]
    """
    start_time = time.time()
    for i in range(iterations):
        _create_user(conn, i)
    end_time = time.time()
    return end_time - start_time


def _select_user_by_username(conn):
    sql = """SELECT * FROM "user" WHERE "username" = 'name666';"""

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def select_user(conn, iterations) -> float:
    start_time = time.time()
    for i in range(iterations):
        _select_user_by_username(conn)
    end_time = time.time()
    return end_time - start_time


def test_create_user():
    """
    Execute performance tests with next amount users:
    - 100       users
    - 1_000     users
    - 10_000    users
    - 100_000   users
    "four tests"

    :return: list with times spend, and, last id
    """
    conn = create_connection()
    times_spend_create = []
    for i in range(4):
        _iter = 10 ** (i + 2)
        print(f"Test {_iter} users")
        time_spend = create_user(conn, _iter)
        time_spend_rounded = round(time_spend, 2)
        print(f"Time spent: {time_spend_rounded} seconds")
        times_spend_create.append(time_spend_rounded)
        if i != 3:
            _delete(conn)

    conn.close()
    return times_spend_create


def test_select_user():
    conn = create_connection()
    times_spend_select_element = []

    for i in range(4):
        _iter = 10 ** (i + 2)
        print(f"Test {_iter} users")
        time_spend = select_user(conn, _iter)
        time_spend_rounded = round(time_spend, 2)
        print(f"Time spent: {time_spend_rounded} seconds")
        times_spend_select_element.append(time_spend_rounded)

    conn.close()
    return times_spend_select_element


def main():
    # test performance on create user
    times_spend_create = test_create_user()
    print(times_spend_create)

    # test performance on select specific user
    times_spend_select = test_select_user()
    print(times_spend_select)


if __name__ == '__main__':
    main()

#!/usr/bin/python

import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        while statement != '\q':
            statement = input()
            cur.execute()
            pass

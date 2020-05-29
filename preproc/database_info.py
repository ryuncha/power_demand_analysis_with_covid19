from sqlalchemy import create_engine
import pymysql

import os
import sys


pymysql.install_as_MySQLdb()


def getServerEngine(db_name = 'covid19_analysis_db'):
    p = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    with open(p+'/AWSDB_HOST.txt','r') as f:
        awsdb_host = f.readline()
    with open(p+'/AWSDB_KEY.txt','r') as f:
        awsdb_key = f.readline()

    engine = create_engine('mysql+mysqldb://'+'loadforecast'+':'+awsdb_key\
                           +'@'+awsdb_host+'/'+db_name, encoding='utf-8')
    conn = engine.connect()

    return engine, conn

if __name__ == '__main__':
    getServerEngine()
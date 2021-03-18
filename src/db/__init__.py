from ..settings import configs
import os
import sqlite3
from ..logger import currentLogger


def init_app(app):
    DB_NAME = app.config["SQLALCHEMY_DATABASE_URI"]
    currentLogger.info("DB is {0}".format(DB_NAME))
    if not os.path.exists(DB_NAME):
        # 创建数据库
        createdb(DB_NAME)
    else:
        currentLogger.warn("{0} has already been existing".format(DB_NAME))

def createdb(dbName):
    try:
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        cur.execute(
            '''
            CREATE TABLE stock (
                code      VARCHAR (10) PRIMARY KEY NOT NULL,
                name      VARCHAR (10) NOT NULL,
                prefix    VARCHAR (6)  DEFAULT ('sh'),
                update_at VARCHAR (20),
                type      INTEGER      DEFAULT(1)
            );
            ''')
        cur.execute(
            '''
            CREATE TABLE daily (
                code        VARCHAR (10) NOT NULL,
                date        VARCHAR (18) NOT NULL,
                open        VARCHAR (12),
                last_close  VARCHAR (12),
                current     VARCHAR (12),
                high        VARCHAR (12),
                low         VARCHAR (12),
                quantity    VARCHAR (20),
                amount      VARCHAR (30),
                bid1        VARCHAR (12),
                bid1_amount VARCHAR (20),
                bid2        VARCHAR (12),
                bid2_amount VARCHAR (20),
                bid3        VARCHAR (12),
                bid3_amount VARCHAR (20),
                bid4        VARCHAR (12),
                bid4_amount VARCHAR (20),
                bid5        VARCHAR (12),
                bid5_amount VARCHAR (20),
                ask1        VARCHAR (12),
                ask1_amount VARCHAR (20),
                ask2        VARCHAR (12),
                ask2_amount VARCHAR (20),
                ask3        VARCHAR (12),
                ask3_amount VARCHAR (20),
                ask4        VARCHAR (12),
                ask4_amount VARCHAR (20),
                ask5        VARCHAR (12),
                ask5_amount VARCHAR (20),
                update_at   VARCHAR (20) NOT NULL,
                turnover    VARCHAR (10),
                CONSTRAINT pk_code_date PRIMARY KEY (
                    code,
                    date
                )
            );
            ''')
        conn.commit()
        currentLogger.info("{0} has been created".format(dbName))
    except Exception as e:
        currentLogger.error('%s',e)
    finally:
        if cur!=None:
            cur.close()
        if conn!=None:
            conn.close()
        

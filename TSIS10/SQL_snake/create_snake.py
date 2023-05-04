import psycopg2
from TSIS10.PhoneBook.config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    DELETE FROM user_snake;
"""

current.execute(sql)

current.close()
db.commit()
db.close()
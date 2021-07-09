import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv


load_dotenv()
db_url = os.getenv('DB_URL')


def db_action(sql_action: str):
    """ DB Setter - Performs a DB action returns None """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(sql_action)
    conn.commit()
    curs.close()
    conn.close()


def db_query(sql_query) -> list:
    """ DB Getter - Returns query results as a list """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(sql_query)
    results = curs.fetchall()
    curs.close()
    conn.close()
    return results


def get_df() -> pd.DataFrame:
    """ Gets a DataFrame representation of the DB """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute("""SELECT clubname AS club, activityname AS activity, reactionint AS sentiment
    FROM memberreactions
    JOIN reactions ON memberreactions.reactionid = reactions.reactionid
    JOIN activities ON memberreactions.activityid = activities.activityid
    JOIN clubs ON memberreactions.clubid = clubs.clubid;""")
    cols = [k[0] for k in curs.description]
    rows = curs.fetchall()
    df = pd.DataFrame(rows, columns=cols)
    curs.close()
    conn.close()
    return df


if __name__ == '__main__':
    print(get_df())

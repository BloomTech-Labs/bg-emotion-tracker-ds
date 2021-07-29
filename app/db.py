import os
import datetime as dt

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


def db_query(sql_query: str) -> list:
    """ DB Getter - Returns query results as a list """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(sql_query)
    results = curs.fetchall()
    curs.close()
    conn.close()
    return results


def emoji_lookup(s: str) -> str:
    lookup = {
        "1F603": "😃",  # 5.0
        "1F60E": "😎",  # 4.5
        "1F642": "🙂",  # 4.0
        "1F610": "😐",  # 3.5
        "1F974": "🥴",  # 3.0
        "1F634": "😴",  # 2.5
        "1F915": "🤕",  # 2.0
        "1F971": "🥱",  # 1.5
        "1F622": "😢",  # 1.0
        "1F624": "😤",  # 0.5
    }
    return lookup.get(s.upper(), '?')


def get_df() -> pd.DataFrame:
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute("""
    SELECT clubname AS club, activityname AS activity, reactionint AS sentiment, 
    reactionvalue AS emoji, reactions.created_date AS date
    FROM memberreactions
    JOIN reactions ON memberreactions.reactionid = reactions.reactionid
    JOIN activities ON memberreactions.activityid = activities.activityid
    JOIN clubs ON memberreactions.clubid = clubs.clubid;""")
    cols = [k[0] for k in curs.description]
    rows = curs.fetchall()
    df = pd.DataFrame(rows, columns=cols)
    df['emoji'] = df['emoji'].apply(emoji_lookup)
    curs.close()
    conn.close()
    return df


def get_club_df_by_date_range(club, start, stop) -> pd.DataFrame:
    """ Inclusive date range """
    df = get_df()
    stop = dt.datetime.strptime(stop, '%Y-%m-%d') + dt.timedelta(days=1)
    df = df[(df['club'] == club) & (df['date'] >= start) & (df['date'] <= stop)]
    return df


def get_club_activity_df_by_date_range(club, activity, start, stop) -> pd.DataFrame:
    df = get_club_df_by_date_range(club, start, stop)
    return df[df['activity'] == activity]

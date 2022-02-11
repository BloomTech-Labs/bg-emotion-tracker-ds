import pandas as pd
from fastapi import APIRouter
import plotly.graph_objects as go
import plotly.express as px
import datetime as dt

from app.db import get_club_activity_df_by_date_range, get_df

router = APIRouter()


def get_pie_detail(df: pd.DataFrame, col: str) -> go.Figure:
    """ Plotly Pie Chart """
    vc_df = df[col].value_counts()
    labels = vc_df.index
    values = vc_df.values
    data = go.Pie(
        labels=labels,
        values=values,
        hole=0.5,
    )
    layout = go.Layout(
        title="",
        colorway=px.colors.qualitative.Antique,
        height=640,
        width=820,
    )
    figure = go.Figure(data, layout)
    figure.update_traces(
        textinfo='label',
        textfont_size=48,
    )
    figure.update_layout(showlegend=False)
    return figure


@router.get("/pie/{club}/{activity}/{start}/{stop}")
def get_pie(club: str, activity: str, start: str, stop: str):
    """ Pie Chart API Endpoint - Returns JSON for Plotly.js """
    df = get_club_activity_df_by_date_range(
        club=club,
        activity=activity,
        start=start,
        stop=stop,
    )
    figure = get_pie_detail(
        df=df,
        col='emoji',
    )
    return figure.to_json()


def get_bar_daily():
    clubs = {
        'Anderson',
        'Catlin',
        'Grossman',
        'Jefferson',
        'Johnston',
        'Morton',
        'Marley',
        'Notter',
        'Stelle',
    }
    df = get_df()
    stop = dt.datetime.today()
    start = stop - dt.timedelta(days=1)
    df = df[(df['date'] >= start) & (df['date'] <= stop)]
    club_results = {}
    for club in clubs:
        start = df[
            (df['activity'] == 'Club Checkin') &
            (df['club'] == club)
            ].mean(numeric_only=True)[0]
        stop = df[
            (df['activity'] == 'Club Checkout') &
            (df['club'] == club)
            ].mean(numeric_only=True)[0]
        average = stop - start
        club_results[club] = average

    result_df = pd.DataFrame(
        club_results.values(),
        index=club_results.keys(),
        columns=["Daily Net Change"],
    )
    return result_df


@router.get("/daily/")
def get_daily():
    df = get_bar_daily()
    data = go.Bar(
        x=[f"<a href='/{club}'>{club}</a>" for club in df.index],
        y=df["Daily Net Change"],
    )
    layout = go.Layout(
        title="Sentiment: Daily Net Change",
        height=600,
        width=820,
        yaxis={"title": "Checkin/Checkout Difference"},
        xaxis={'title': "B&G Clubs"},
    )
    return go.Figure(data, layout).to_json()

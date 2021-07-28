import pandas as pd
from fastapi import APIRouter
import plotly.graph_objects as go
import plotly.express as px

from app.db import get_club_activity_df_by_date_range

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
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
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

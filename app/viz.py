"""Data visualization functions"""
import pandas as pd
from fastapi import APIRouter
import plotly.graph_objects as go
import plotly.express as px

from app.db_ops import get_df

router = APIRouter()


def get_bar(df, col_1, col_2):
    col_1_name = col_1.replace('_', ' ').title()
    col_2_name = col_2.replace('_', ' ').title()

    if col_1_name == col_2_name:
        title = f"{col_1_name} Totals"
    else:
        title = f"{col_2_name} by {col_1_name}"

    df_cross = pd.crosstab(df[col_1], df[col_2])
    data = [go.Bar(name=col, x=df_cross.index, y=df_cross[col])
            for col in df_cross.columns]
    layout = go.Layout(
        title=title,
        colorway=px.colors.qualitative.Antique,
        height=600,
        width=820,
        barmode="stack",
        yaxis={"title": f"{col_2_name} Counts"},
        xaxis={'title': col_1_name}
    )
    return go.Figure(data, layout)


def get_pie(df, col, pie_type="Donut"):
    col_name = col.replace('_', ' ').title()
    vc_df = df[col].value_counts()
    labels = vc_df.index
    values = vc_df.values
    title = f"Percentage by {col_name}"
    hole = {
        "Solid": 0.0,
        "Donut": 0.5,
        "Ring": 0.8,
    }[pie_type]
    data = go.Pie(labels=labels, values=values, hole=hole)
    layout = go.Layout(
        title=title,
        colorway=px.colors.qualitative.Antique,
        height=640,
        width=820,
    )
    figure = go.Figure(data, layout)
    figure.update_traces(textinfo='label+percent')
    return figure


@router.get("/pie/{col}")
def get_pie_chart(col: str):
    return get_pie(get_df(), col).to_json()


@router.get("/bar/{col1}/{col2}")
def get_bar_chart(col1: str, col2: str):
    return get_bar(get_df(), col1, col2).to_json()

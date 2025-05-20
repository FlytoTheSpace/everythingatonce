import plotly.graph_objects as go
from typing import Callable, List
"""
a simple abstraction for graphing using plotly.py
"""

Appearance = {
    "bgcolor": "#202020",
    "gridcolor": "#505050",
    "font": {
        "color": "white",
        "family": "sans-serif",
        "size": 14
    },
    "line": {
        "width": 4,
        "color_01": "#00A0FF",
        "color_02": "#FF4000",
        "color_03": "#00FF40",
        "color_04": "#FFFF00",
        "dash": None
    }
}

fig = go.Figure()

def graph(x = List[int], y = List[int], name: str = "line", mode: str = "lines"):
    fig.add_trace(go.Scatter(x=x, y=y, mode=mode, name=name, line=dict(width=Appearance["line"]["width"],color=Appearance["line"]["color_01"],dash=Appearance["line"]["dash"])))

def show(title: str = "Title"):
    fig.update_layout(
        title=title,
        title_x=0.5,
        font=dict(
            color=Appearance["font"]["color"],
            family=Appearance["font"]["family"],
            size=Appearance["font"]["size"]
        ),
        plot_bgcolor=Appearance["bgcolor"],
        paper_bgcolor=Appearance["bgcolor"],
        title_font=dict(
            color=Appearance["font"]["color"]
        ),
        xaxis=dict(
            gridcolor=Appearance["gridcolor"],
            zeroline=True,
            tickfont=dict(
                color=Appearance["font"]["color"]
            )
        ),
        yaxis=dict(
            gridcolor=Appearance["gridcolor"],
            zeroline=True,
            tickfont=dict(
                color=Appearance["font"]["color"]
            )
        ),
        dragmode='zoom'
    )
    fig.show(config={"scrollZoom": True})

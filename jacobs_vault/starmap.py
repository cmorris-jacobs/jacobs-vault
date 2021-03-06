# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_Early_HitTest.ipynb (unless otherwise specified).

__all__ = ['starmap']

# Cell
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

# Cell
def starmap(old_df, show=True, size0=1, alpha=1, mode='svg',
           newcolors=True):
    """Polar plots a `df_alt_az_days_visible` dataframe.
    Dataframe must have: `color`, `days`, `altitude`, `azimuth`.
    old_df["days"] must be DateTimeValue or Scalar
    Returns a Plotly Express polar plot figure with:
        * Excellent in blue
        * Good in pink
        * Poor and stale in yellow

    show: if True, also display the figure here
    size0: smallest marker size (used for best hits), out of 10.
    alpha: reduce if the figure is too cluttered
    mode: 'svg' is sharpest, 'webgl' is fastest
    newcolors: if True, just use days as the color,
               else convert to original 3-color scheme.

    """
    df = old_df.copy()
    if newcolors:
        try:
            df["color"] = df["days"].dt.days
        except AttributeError:
            df["color"] = df["days"]
        df.loc[df["color"]>12] = 12
    else:
        df["color"] = 2 # covers poor and stale
        try:
            df.loc[(df["days"].dt.days <= GOOD), "color"] = 1
            df.loc[(df["days"].dt.days <= EXCELLENT), "color"] = 0
        except AttributeError:
            df.loc[(df["days"] <= GOOD), "color"] = 1
            df.loc[(df["days"] <= EXCELLENT), "color"] = 0

    df["size"] = size0 + df["color"]*2
    df["R"] = 90.0 - df["altitude"]
    #fig = px.scatter_polar(df_alt_az_days_visible, r="R", theta="azimuth", color_discrete_sequence=['black'])
    fig = px.scatter_polar(df, r="R", theta="azimuth", color="color",
                           size="size", size_max=10, render_mode=mode)
    if show:
        fig.update_traces(opacity=alpha, showlegend=False).show()
    return fig
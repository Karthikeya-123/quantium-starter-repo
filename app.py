import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.lower()

    df = df[df["product"] == "pink morsel"]

    df["price"] = df["price"].str.replace("$", "").astype(float)

    df["sales"] = df["price"] * df["quantity"]

    df = df[["date", "sales"]]

    dfs.append(df)

full_data = pd.concat(dfs)
full_data["date"] = pd.to_datetime(full_data["date"])

grouped_data = full_data.groupby("date").sum().reset_index()

grouped_data = grouped_data.sort_values("date")

fig = px.line(
    grouped_data,
    x="date",
    y="sales",
    title="Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

fig.add_shape(
    type="line",
    x0="2021-01-15", x1="2021-01-15",
    y0=0, y1=grouped_data["sales"].max(),
    line=dict(color="red", dash="dash"),
)

fig.add_annotation(
    x="2021-01-15",
    y=grouped_data["sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=1
)

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children="Soul Foods Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)


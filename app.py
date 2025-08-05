import dash
from dash import dcc, html
import pandas as pd

df = pd.read_csv("data/daily_sales_data_0.csv")
df.columns = df.columns.str.strip().str.lower()
df["sales"] = df["price"] * df["quantity"]

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children="Sales Dashboard"),

    dcc.Graph(
        id='sales-graph',
        figure={
            "data": [
                {"x": df['date'], "y": df['sales'], "type": "line", "name": "Sales"},
            ],
            "layout": {
                "title": "Sales Over Time"
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)


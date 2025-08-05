import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('pink_morsel_sales.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales by Region", style={'textAlign': 'center'}),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '20px'},
        style={'textAlign': 'center', 'margin': '20px'}
    ),

    dcc.Graph(id='sales-line-chart')
])


@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    def update_graph(selected_region):
        if selected_region == 'all':
            filtered_df = df
        else:

            filtered_df = df[df['region'].str.lower() == selected_region]

        fig = px.line(filtered_df, x='date', y='sales', color='product',
                      title=f"Sales Data ({selected_region.title()})")
        return fig


if __name__ == '__main__':
    app.run(debug=True)


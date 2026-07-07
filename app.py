from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv('combined_output.csv')

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(id="graph"),
    dcc.Checklist(
    id="checklist",
    options=["north", "south", "east", "west"],
    value=["north", "south", "east", "west"],
    inline=True
    ),
])
@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
def update_line_chart(regions):
    filtered_df = df[df['region'].isin(regions)]
    fig = px.line(filtered_df,
        x="date", y="sales", color='region', title='Sales by Region')
    return fig


app.run(debug=True)
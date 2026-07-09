from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv('data/combined_output.csv')


app.layout = html.Div([

    html.H1("Pink Morsels Sales Dashboard", style={
    'textAlign': 'center', 
    'color': '#fffffe', 
    'backgroundColor': '#232946',
    'minHeight': '25vh'}),
    dcc.Graph(id="graph"),
    dcc.Checklist(
    id="checklist",
    options=["north", "south", "east", "west"],
    value=["north", "south", "east", "west"],
    inline=True),
])
@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
def update_line_chart(regions):
    filtered_df = df[df['region'].isin(regions)]
    fig = px.line(filtered_df,
        x="date", y="sales", color='region',
        color_discrete_sequence = ['#b8c1ec', '#eebbc3', '#566B81', '#8bd3dd'])
    fig.update_layout(
        plot_bgcolor='#232946',   
        paper_bgcolor='#232946',  
        font_color='#fffffe'      
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)

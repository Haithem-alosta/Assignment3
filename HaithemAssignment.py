import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/Haithem-alosta/Assignment3/main/best-selling%20game%20consoles.csv"
data = pd.read_csv(data_url)
data3 = data[['Console Name', 'Units sold (million)', 'Released Year']]
data3 = data3.sort_values('Released Year', ascending=False)

fig_bar = px.bar(data3, x='Console Name', y='Units sold (million)', title='Units Sold for Different Consoles')
fig_box = px.box(data3, x='Console Name', y='Released Year', title='Released Years for Different Consoles')

data3_sorted = data3.sort_values(by='Units sold (million)', ascending=False)
top_5_consoles = data3_sorted.head(5)
fig_pie = px.pie(top_5_consoles, values='Units sold (million)', names='Console Name', title='Top 5 Best-Selling Gaming Consoles')

sony_df = data[data['Company'] == 'Sony']
units_sold_by_year_sony = sony_df.groupby('Released Year')['Units sold (million)'].sum()

fig_sony = px.line(x=units_sold_by_year_sony.index, y=units_sold_by_year_sony.values, title='Sony Console Sales by Year')
fig_sony.update_xaxes(title='Year')
fig_sony.update_yaxes(title='Units sold (million)')

nintendo_df = data[data['Company'] == 'Nintendo']
units_sold_by_year_nintendo = nintendo_df.groupby('Released Year')['Units sold (million)'].sum()

fig_nintendo = px.line(x=units_sold_by_year_nintendo.index, y=units_sold_by_year_nintendo.values, title='Nintendo Console Sales by Year')
fig_nintendo.update_xaxes(title='Year')
fig_nintendo.update_yaxes(title='Units sold (million)')

app.layout = html.Div([
    html.H1("Haithem Assignment 3"),
    
    dcc.Graph(figure=fig_bar),
    
    dcc.Graph(figure=fig_box),
    
    dcc.Graph(figure=fig_pie),
    
    dcc.Graph(figure=fig_sony),
    
    dcc.Graph(figure=fig_nintendo)
])

if __name__ == '__main__':
    app.run_server(debug=True)

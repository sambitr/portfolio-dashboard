import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html

# Load CSV files
files = {
    '2020': '2020-MF-pnl-NU2499.csv',
    '2021': '2021-MF-pnl-NU2499.csv',
    '2022': '2022-MF-pnl-NU2499.csv',
    '2023': '2023-MF-pnl-NU2499.csv',
    '2024': '2024-MF-pnl-NU2499.csv'
}

# Load and clean data
def load_and_clean(file, year):
    # Read CSV
    df = pd.read_csv(file)
    # Standardize column names: remove quotes, strip spaces, lowercase, and replace spaces with underscores
    df.columns = df.columns.str.replace('"', '').str.strip().str.lower().str.replace(' ', '_')
    # Filter required columns and add year
    df['year'] = year
    return df[['symbol', 'unrealized_p&l', 'year']]

# Combine data from all files
data = pd.concat([load_and_clean(files[year], year) for year in files])

#unrealized_p&l by year
total_pnl_by_year = data.groupby('year')['unrealized_p&l'].sum().reset_index()
total_pnl_by_year['pct_change'] = total_pnl_by_year['unrealized_p&l'].pct_change() * 100


top_performing_symbols = data.groupby('symbol')['unrealized_p&l'].sum().reset_index()
top_performing_symbols = top_performing_symbols.sort_values('unrealized_p&l', ascending=False).head(10)

## average unrealized P&L per symbol for each year. This can help compare funds with each other on an average basis.
avg_pnl_per_symbol = data.groupby(['symbol', 'year'])['unrealized_p&l'].mean().reset_index()



# Create Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Mutual Fund Portfolio Dashboard"),
    
    # Bar chart for Total Unrealized P&L Trends by Year
    dcc.Graph(
        figure=px.bar(total_pnl_by_year, x='year', y='unrealized_p&l', 
                  title='Total Unrealized P&L by Year', labels={'unrealized_p&l': 'Total Unrealized P&L'})
    ),
    
    # Bar chart for Total Unrealized P&L with Percentage Change Annotations
    dcc.Graph(
        figure=go.Figure()
            .add_trace(go.Bar(x=total_pnl_by_year['year'], 
                              y=total_pnl_by_year['unrealized_p&l'], 
                              name='Total Unrealized P&L'))
            .add_trace(go.Scatter(x=total_pnl_by_year['year'], 
                                 y=total_pnl_by_year['pct_change'], 
                                 mode='lines+markers', 
                                 name='Percentage Change', 
                                 yaxis='y2'))
            .update_layout(
                title='Total Unrealized P&L by Year with Percentage Change',
                yaxis=dict(title='Total Unrealized P&L'),
                yaxis2=dict(title='Percentage Change (%)', overlaying='y', side='right'),
                showlegend=True
            )
    ),
    
    # Bar chart for Unrealized P&L by Fund and Year
    dcc.Graph(
        figure=px.bar(data, x='symbol', y='unrealized_p&l', color='year', barmode='group',
                      title='Unrealized P&L Comparison Across Funds and Years')
    ),

    # Line chart for Unrealized P&L Trends by Fund
    dcc.Graph(
        figure=px.line(data, x='year', y='unrealized_p&l', color='symbol', markers=True,
                       title='Unrealized P&L Trends for Each Fund')
    ),
    
    dcc.Graph(
        figure=px.bar(top_performing_symbols, x='symbol', y='unrealized_p&l', 
                  title='Top 10 Performing Symbols', labels={'unrealized_p&l': 'Unrealized P&L'})
    ),
    
    # histogram or box plot to understand the distribution of unrealized P&L across all funds or years
    dcc.Graph(
        figure=px.histogram(data, x='unrealized_p&l', title='Distribution of Unrealized P&L')
    ),
    
    dcc.Graph(
        figure=px.line(avg_pnl_per_symbol, x='year', y='unrealized_p&l', color='symbol', markers=True,
                   title='Average Unrealized P&L Per Symbol by Year')
    )
    
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)

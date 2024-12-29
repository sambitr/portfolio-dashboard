# portfolio-dashboard

## What I wanted:
I was looking to create a dashboard to findout how my Mutual Fund Portfolio behaved over a period of 4-5 years. Basically, I wanted below things to check:

- Total YoY profit/loss
- Total profit and loss percent in comparios to last year's performance
- Profit/Loss comparison across funds
- Unrealized P&L Trends for Each Fund
- Top 10 Performing Symbols
- Distribution of Unrealized P&L
- Average Unrealized P&L Per Symbol by Year

## Problem:
Problem is that there is no readymade dashboard feature available in my broker and I did not want to pay any money for professional dashboard creation. 

## Solution:

Created this python script using pandas, plotly, Flask, dash to fetch the required details from the 5 years P&L data. I am using Zerodha as my broker and it provides below columns:

```
Symbol
ISIN
Quantity
Buy Value
Sell Value
Realized P&L
Realized P&L Pct.
Previous Closing Price
Open Quantity
Open Quantity Type
Open Value
Unrealized P&L
Unrealized P&L Pct.
```

The yearwise CSV file does not have year value in it. Hence created below dictionary to add it to identify the year associated with it.

```
# Load CSV files
files = {
    '2020': '2020-MF-pnl-NU2499.csv',
    '2021': '2021-MF-pnl-NU2499.csv',
    '2022': '2022-MF-pnl-NU2499.csv',
    '2023': '2023-MF-pnl-NU2499.csv',
    '2024': '2024-MF-pnl-NU2499.csv'
}
```

**FYI: I have uploaded a sample CSV file with the required columns in it. If you are a Zerodha user, you can get this CSV file from the Zerodha COnsole page too, from the P&L statements**

## Running Script:

```
python script.py
```
This will load the flask app and you can access it through the URL which will be provided while running the script

```
PS C:\Users\lenovo\Downloads> python script.py
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'script'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8050
Press CTRL+C to quit
```

## Result:

The above script produces below results:

![image](https://github.com/user-attachments/assets/a844c775-2472-4a06-9257-306092e2740e)

![image](https://github.com/user-attachments/assets/2e0e1e74-1594-4211-ab08-3c6397451e2f)

![image](https://github.com/user-attachments/assets/3976874e-4902-4392-940a-0abd061cd273)

![image](https://github.com/user-attachments/assets/bb3a5038-2b70-4971-b52d-eeac672bda81)

![image](https://github.com/user-attachments/assets/35f2453f-a2ab-4967-8144-c5d740f003e4)

![image](https://github.com/user-attachments/assets/f86c04ff-d11c-46f5-91d8-668c0a3b8f19)

![image](https://github.com/user-attachments/assets/baad2026-c521-41d3-a8d2-f84f185aaa77)

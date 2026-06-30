import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import yfinance as yf
stock = yf.Ticker("RELIANCE.NS")
df = stock.history(period="1y")
df=df.reset_index()

df['Close'].plot(title="Reliance Industries Stock Price - Last 1 Year")
plt.show()

df.to_csv("reliance_stock_data.csv")

conn = sqlite3.connect('reliance_stock_data.db')
df.to_sql('stock_data',conn, if_exists='replace', index=False)

close = pd.read_sql("SELECT Date,Close FROM stock_data",conn)
volume = pd.read_sql("SELECT Date,Volume FROM stock_data ORDER BY Volume DESC", conn)
monthly_avg = pd.read_sql("SELECT strftime('%Y-%m', Date) as Month, ROUND(AVG(Close), 2) as Avg_Close FROM stock_data GROUP BY Month ORDER BY Month", conn)

close['Date']= pd.to_datetime(close['Date'])
plt.figure(figsize =(12,6))
plt.plot(close['Date'],close['Close'],color ='orange')
plt.title("Reliance Industries Stock Price - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid("True")
plt.show()

volume['Date'] = pd.to_datetime(volume['Date']).dt.strftime('%d %b %Y')
plt.figure(figsize =(12,6))
plt.plot(volume['Date'],volume['Volume'],color ='blue')
plt.title("Reliance Industries Stock Price - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid("True")
plt.show()

monthly_avg['Date']= pd.to_datetime(monthly_avg['Date'])
plt.figure(figsize =(12,6))
plt.plot(monthly_avg['Date'],monthly_avg['Avg_Close'],color ='blue')
plt.title("Reliance Industries Stock Price - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid("True")
plt.show()
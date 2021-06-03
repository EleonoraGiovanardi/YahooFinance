import yfinance as yf
import pandas as pd

t = yf.Ticker("AAPL")

dati = t.history(period = "10Y")
dati.to_csv("AzioniApple10anni.csv")

print("Applicazione che si connette a YF per scaricare i dati di Apple")
print(dati.head())

t = yf.Ticker("MSFT")

dati_m = t.history(period = "10Y")
dati_m.to_csv("AzioniMSFT10anni.csv")

print("Applicazione che si connette a YF per scaricare i dati di MSFT")
print(dati.head())
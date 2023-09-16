# Fundamental data scraping from Yahoo Finance
# This code was modified in Sep 2023 from an original code by Mayank Rasu
# Visit his personal website (https://rasuquant.com/) and buy his Udemy Algorithmic Trading course for further details.

import requests
from bs4 import BeautifulSoup
import pandas as pd

def balance(ticker):

    #scraping balance sheet

    url = "https://finance.yahoo.com/quote/{}/balance-sheet?p={}".format(ticker,ticker)
    balance_sheet = {}
    table_title = {}
    
    headers = {"User-Agent" : "Chrome/96.0.4664.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            balance_sheet[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(balance_sheet).T
    temp.columns = table_title["Breakdown"]
    
    return temp

def income(ticker):

    #scraping income statement

    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker,ticker)
    income_statement = {}
    table_title = {}
    
    headers = {"User-Agent" : "Chrome/96.0.4664.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]

    return temp
    
def cashflow(ticker):

    #scraping cashflow statement

    url = "https://finance.yahoo.com/quote/{}/cash-flow?p={}".format(ticker,ticker)
    cashflow_statement = {}
    table_title = {}
    
    headers = {"User-Agent" : "Chrome/96.0.4664.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            cashflow_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(cashflow_statement).T
    temp.columns = table_title["Breakdown"]
    
    return temp

def key_stats(ticker):

    #scraping key statistics

    url = "https://finance.yahoo.com/quote/{}/key-statistics?p={}".format(ticker,ticker)    
    headers = {"User-Agent" : "Chrome/96.0.4664.110"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("table" , {"class" : "W(100%) Bdcl(c)"}) #remove/add the trailing space if getting error
    
    temp_stats = {}
    for t in tabl:
        rows = t.find_all("tr")
        for row in rows:
            temp_stats[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[-1]
    
    return temp_stats
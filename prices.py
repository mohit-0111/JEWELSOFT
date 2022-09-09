# Import Required library
from bs4 import BeautifulSoup
import requests
from tkinter import *
from datetime import date
from tkinter import ttk


# Extract Integer or Float from String
def get_number_from_string(string):
	return float(''.join([x for x in string if x.isdigit() or x == '.']))


# Returns the current local date
today = date.today()


# method to get the price of silver
def silver_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/silver-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding metha info for the current price
	price = soup.find("div", class_="gold_silver_table right-align-content").find(
		"tr", class_="odd_row").findAll("td")

	# returning the price in text
	return price[1].text


# method to get the price of gold
def gold_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/gold-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding metha info for the current price
	price = soup.find("div", class_="gold_silver_table gold_silver_table_10_days").find(
		"tr", class_="even_row").findAll("td")

	# returning the price in text
	return (price[2]).text



	



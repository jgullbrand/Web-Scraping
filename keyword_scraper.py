import requests, sys, webbrowser
from bs4 import BeautifulSoup
import csv
import time

with open('keywords.txt') as keyword_file:
	keywords = keyword_file.readlines()

with open('keywords_output.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['keyword', '1st Search Result', '2nd Search Result', '3rd Search Result', '4th Search Result','5th Search Result', 
						'6th Search Result', '7th Search Result', '8th Search Result', '9th Search Result','10th Search Result',])
	for keyword in keywords:
		keyword = keyword.strip()
		response = requests.get(f'https://www.google.com/search?q={keyword}').text
		
		result_list = []
		soup = BeautifulSoup(response, 'lxml')
		linkElems = soup.select('.r a')
		for element in linkElems:
			url = element['href'].split('q=')[1]
			clean_url = url.split('&')[0].split('%')[0]
			headline_text = element.text
			result = "Headline: " + headline_text + "\n\n" + "Link: " + clean_url
			result_list.append(result)
		time.sleep(3) # pauses the script for three seconds in between each keyword
		try:
			csv_writer.writerow([keyword, result_list[0], result_list[1], result_list[2], result_list[3], result_list[4], 
							result_list[5], result_list[6], result_list[7], result_list[8], result_list[9]])
		except Exception as e:
			pass	
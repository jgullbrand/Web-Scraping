from bs4 import BeautifulSoup
import requests
import csv



with open('news_update.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(['News Source', 'Date/Time Posted', 'Header', 'Summary'])

	db_response = requests.get('https://www.thedailybeast.com/cheat-sheet').text 
	#print(response)

	db_soup = BeautifulSoup(db_response, 'lxml')
	cheatsheet_count = 0

	for cheatsheet in db_soup.body.find_all('article', class_="Cheat"):
		if cheatsheet_count > 4:
			break
		try:
			db_time_posted = cheatsheet.find('span', class_="PublicationTime__date-from-now").text
		except Exception as e:
			continue
		db_news_source = 'Daily Beast'
		db_header = cheatsheet.div.h1.text
		db_text_summary = cheatsheet.find('div', class_="CheatBody").text
		db_text_summary_clean = db_text_summary[:200] + "..."
		cheatsheet_count+=1

		csv_writer.writerow([db_news_source, db_time_posted, db_header, db_text_summary_clean])

	ap_response = requests.get('https://www.apnews.com/apf-topnews').text 

	ap_soup = BeautifulSoup(ap_response, 'lxml')

	ap_count = 0
	for ap_article in ap_soup.find_all('div', class_="FeedCard WireStory with-image"):
		if ap_count > 4:
			break
		ap_news_source = 'The Associated Press'
		ap_header = ap_article.find('div', class_="CardHeadline").h1.text
		ap_time_posted = ap_article.find('div', class_="signature").find('span', class_="Timestamp").text
		ap_text_summary = ap_article.find('div', class_="content").text
		ap_text_summary_clean = ap_text_summary[:200] + "..."
		ap_count+=1
		csv_writer.writerow([ap_news_source, ap_time_posted, ap_header , ap_text_summary_clean])
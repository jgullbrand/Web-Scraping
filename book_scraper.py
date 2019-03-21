from bs4 import BeautifulSoup
import requests
import csv

pages_to_scrape = input("How many pages of books would you like to see? Each page has 100 books. Please enter a number from 1 to 10 \n> ")
book_count = 0

with open('books2.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(['Book Title', 'Goodreads Link', 'Book Author', 'Community Voting Score', 'Goodreads Overall Rating'])

	for page_num in range(1,int(pages_to_scrape)+1):
		response = requests.get(f'https://www.goodreads.com/list/show/567.Best_Chapter_Books_to_Read_Out_Loud?page={page_num}').text 

		soup = BeautifulSoup(response, 'lxml')

		for book_item in soup.find_all('tr', itemtype="http://schema.org/Book"):
			book_title = book_item.find('a', class_="bookTitle").span.text
			find_link = book_item.find('a', class_="bookTitle")['href']
			goodreads_link = 'https://www.goodreads.com' + find_link
			book_author = book_item.find('div', class_="authorName__container").span.text
			community_score = book_item.find('span', class_="smallText uitext").a.text
			goodreads_rating = book_item.find('span', class_="minirating").text.replace('—','')

			csv_writer.writerow([book_title, goodreads_link, book_author, community_score, goodreads_rating])

			book_count +=1

print(f"you have successfully scraped {book_count} books. Please find the full list in the CSV file.")			
## Web Scraping with Beautiful Soup & Requests

### Project 1: Vegan Ice Cream in Boston - Market Research & Keyword Analysis using Google Search
*keyword_scraper.py*

This script allows you to quickly scrape and document the first 10 results from a Google Search. In the example below, I am doing research on vegan ice cream places in the Boston area. I started with three google searches written in *keywords.txt*
```
Vegan ice cream in boston
Dairy free ice cream in Boston
Cococunt milk ice cream in Boston
```
The script, *keyword_scraper.py* reads in each of these keywords, searches google and returns the first results (headlines & links). This output allows someone to quickly get a sense for google ranking based on these keywords. The results are output to a csv file. Here's a sample of the output:
![output_keywords](https://user-images.githubusercontent.com/40340806/54774196-8e61a700-4be1-11e9-961d-ed934ec0644a.png)

### Project 2: Top Chapter Books - I wanted to build a tool that allowed me to accumulate a list of top books for my niece 
*book_scraper.py*

This script first allows you to select how many pages of this list you'd like to pull. The script pulls the book title, link to the specific goodreads page for the book, the author, the community score, and the overall Goodreads rating. All of these results are printed to a CSV file. Here's a sample of the output:

![book_output](https://user-images.githubusercontent.com/40340806/54774845-08def680-4be3-11e9-9153-a3f91066aa3b.png)

### Project 3: Top News - Quickly get up to speed on the top news stories
*news_scraper.py*

This script aggregates the top 5 results from both The Daily Beast Cheatsheet and the Associated Press Top News. My goals was to create a result that would allow someone to quickly consume the news during a cup of coffee in the morning. The script pulls the date, header & summary for each of the top news articles. The output is presented in a csv file, as shown below:

![news_update](https://user-images.githubusercontent.com/40340806/54775955-6d9b5080-4be5-11e9-923e-e278231db7de.png)

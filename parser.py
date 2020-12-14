from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
beautifulSoup = BeautifulSoup(source, 'lxml')

csvFile = open('post.csv', 'w')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['Title', 'Summary', 'YouTube Link'])

for article in beautifulSoup.find_all('article'):

    headline = article.h2.a.text
    print(headline)
    print()
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    print()

    try:
        videoSource = article.find(
            'iframe', class_='youtube-player')['src'].split('/')[4]

        videoId = videoSource.split('?')[0]

        youtubeLink = 'https://youtube.com/watch?v={}'.format(videoId)

    except Exception as e:
        youtubeLink = None

    print(youtubeLink)

    print()
    print()

    csvWriter.writerow([headline, summary, youtubeLink])

csvFile.close()

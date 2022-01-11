#%%
import requests
import pymysql
from bs4 import BeautifulSoup

# OPEN CONNECTION to SQL
conn = pymysql.connect(host='', user='', password='',
                       db='', charset='')
curs = conn.cursor()

# CREATE URL of BOARDS
boards = []
for i in range(223):
    url = "https://www.emf-portal.org/en/article/search/results?keywords=&logicalOperator=0&authors=&authorMatchingMode=0&journals=&journalMatchingMode=0&years=&topics%5B0%5D=0&frequencyRanges%5B0%5D=0&frequencyRanges%5B1%5D=1&frequencyRanges%5B2%5D=2&frequencyRanges%5B3%5D=3&frequencyRanges%5B4%5D=4&frequencyRanges%5B5%5D=5&timeSpan=0&pageIndex="+ str(i) + "&pageSize=50"
    boards.append(url)

# PARSE BOARDS and SAVE URLs in SQL
for b in boards:
    webpage = requests.get(b)
    soup = BeautifulSoup(webpage.content, "html.parser")
    selected_soup = soup.select('body > div.container > ul > li > div:nth-child(2)')
    for each in selected_soup:
        check = each.select('span:nth-child(1)')
        try:
            if check[0].text == "[details]":
                url = "https://www.emf-portal.org" + each.select('a')[0].attrs['href']
                #sql = "INSERT INTO `emf_portal`.`emf_db_v1` (`url`) VALUES ('%s');"%(url)
                #print(sql)
                #curs.execute(sql)
        except:
            None
conn.close()

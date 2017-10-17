# Fetches data from url then write to file

def get_date(movie1, movie2, movie3):

    import scrapy

    descrip1 = scrapy.spider(movie1)
    descrip2 = scrapy.spider(movie2)
    descrip3 = scrapy.spider(movie3)

    html1 = descrip1.read()
    html2 = descrip2.read()
    html3 = descrip3.read()

    from bs4 import BeautifulSoup

    soup1 = BeautifulSoup(html1, 'html.parser').get_text()
    soup2 = BeautifulSoup(html2, 'html.parser').get_text()
    soup3 = BeautifulSoup(html3, 'html.parser').get_text()

    final = soup1 + soup2 + soup4

    return final

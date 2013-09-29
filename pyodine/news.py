import BeautifulSoup
import ClientCookie


class NewsPost:
    def __init__(self, id):
        show_url = "https://iodine.tjhsst.edu/api/news/show/" + str(id)
        content = ClientCookie.urlopen(show_url).read()
        soup = BeautifulSoup.BeautifulSoup(content)
        self.title = soup.title.string
        self.content = soup.text_strip.string


def get_all_news():
    list_url = "https://iodine.tjhsst.edu/api/news/list"
    content = ClientCookie.urlopen(list_url).read()
    soup = BeautifulSoup.BeautifulSoup(content)
    ids = soup.findAll('id')
    return [NewsPost(i.string) for i in ids]

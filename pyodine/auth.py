import BeautifulSoup
import ClientCookie
import urllib
import urllib2


class Authenticator:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def login(self):
        try:
            login_params = {
                'login_username': self.username,
                'login_password': self.password
                }
            login_params = urllib.urlencode(login_params)
            login_request = urllib2.Request("https://iodine.tjhsst.edu",
                                            login_params)
            login_response = ClientCookie.urlopen(login_request).read()
            webpage = BeautifulSoup.BeautifulSoup(login_response)
            eighth_change_url = webpage.find(id="menu_eighth")["href"]
            uid = eighth_change_url.split("uid/")[1]
            self.uid = uid
            self.is_authenticated = True
        except Exception, e:
            self.uid = None
            self.is_authenticated = False
            print e
            pass

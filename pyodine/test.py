def test_auth():
    import auth
    import getpass
    a = auth.Authenticator("2016fwilson", getpass.getpass())
    a.login()
    print a.uid

def test_news():
    import news
    for i in news.get_all_news():
        print i.content

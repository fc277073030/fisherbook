from http import HTTP

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http:/t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @staticmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        #dict
        return result

    @staticmethod
    def search_by_keyword(cls, keyword):
        url = cls.keyword_url.format(keyword)
        result = HTTP.get(url)
        return result
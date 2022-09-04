from sourcedriver import SourceDriver
from builder import createEbook


class LitPy:
    def __init__(self):
        self._url_lit = None
        self._start_chapter = None
        self._end_chapter = None
        self._delay = 10
        self._book_id = None
        self._book_title = None
        self._book_save = None

    def set_options(self, options):
        for key in options:
            self._url_lit = options.get("url_lit", None)
            self._start_chapter = options.get("start_chapter", None)
            self._end_chapter = options.get("end_chapter", None)
            self._delay = options.get("delay", 10)
            self._book_id = options.get("book_id", None)
            self._book_title = options.get("book_title", None)
            self._book_save = options.get("book_save", None)

    def convert2epub(self):
        sourcedriver = SourceDriver(url_lit=self._url_lit)
        content = sourcedriver.pull_data(
            url_lit=self._url_lit,
            start_chapter=self._start_chapter,
            end_chapter=self._end_chapter,
            delay=self._delay,
        )

        createEbook(
            content=content,
            book_id=self._book_id,
            book_title=self._book_title,
            book_save=self._book_save,
        )


if __name__ == "__main__":
    url_base = "https://www.royalroad.com/fiction/21220/mother-of-learning"

    litpy = LitPy()

    options = {
        "url_lit": "https://www.royalroad.com/fiction/21220/mother-of-learning",
        "start_chapter": 1,
        "end_chapter": 5,
        "delay": 1,
        "book_id": "Test3",
        "book_title": "Test3",
        "book_save": "Test3.epub",
    }
    litpy.set_options(options)

    litpy.convert2epub()
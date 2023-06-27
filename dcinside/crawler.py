from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.by import By

from .exception import *


class Crawler:
    def __init__(self, timeout=60, retry=True):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")

        self.retry = retry
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(timeout)

    def crawl(self, gallery, idx, collect_comment=False):
        while True:
            try:
                self.driver.get(f"https://gall.dcinside.com/board/view/?id={gallery}&no={idx}")

                try:
                    self.driver.find_element(By.CLASS_NAME, "delet")
                except NoSuchElementException:
                    pass
                else:
                    raise DeletedPostException

                if collect_comment:
                    comments = []
                    try:
                        n_comments = self.driver.find_element(By.CLASS_NAME, "cmt_paging")
                        n_comments = n_comments.find_elements(By.TAG_NAME, "a")
                        last_comment_page = len(n_comments) + 1
                    except NoSuchElementException:
                        last_comment_page = 0

                    for i in range(last_comment_page, 0, -1):
                        self.driver.execute_script(f"viewComments({i}, 'D')")
                        page_comments = self.driver.find_elements(By.CLASS_NAME, "usertxt")
                        for comment in page_comments:
                            comments.append(comment.text)

                title = self.driver.find_element(By.CLASS_NAME, "title_subject")
                content = self.driver.find_element(By.CLASS_NAME, "writing_view_box")
                content = content.find_elements(By.TAG_NAME, "div")
                content = content[-1]

                if collect_comment:
                    return {
                        "title": title.text,
                        "content": content.text,
                        "comments": comments
                    }
                else:
                    return {
                        "title": title.text,
                        "content": content.text
                    }

            except DeletedPostException:
                raise DeletedPostException

            except (NoSuchElementException, TimeoutException):
                if not self.retry:
                    raise ServerException

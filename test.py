from dcinside.crawler import Crawler
import json
import os

def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

gallery = "programming"

COLLECT_COMMENT = False

create_directory(gallery)


crawler = Crawler()
for i in range(2519214, 2520340):
    try:
        res = crawler.crawl(gallery, str(i), COLLECT_COMMENT)
        
        with open(f"./{gallery}/{gallery}_{i}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(res, ensure_ascii=False, indent=4))
    except Exception as e:
        print(e)
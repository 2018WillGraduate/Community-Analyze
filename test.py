from dcinside.crawler import Crawler
import json

crawler = Crawler()
for i in range(1, 101):
    try:
        res = crawler.crawl("kartriderdrift", str(i))
        with open(f"data/kartriderdrift_{i}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(res, ensure_ascii=False, indent=4))
    except Exception as e:
        print(e)
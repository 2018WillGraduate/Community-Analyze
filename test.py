from dcinside.crawler import Crawler
import json
import os

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
        if str(e) in exc:
            exc[str(e)].append(i)
        else:
            exc[str(e)] = [i]
print(exc)


# def create_directory(path):
#     try:
#         os.makedirs(path)
#         print(f"Directory '{path}' created.")
#     except FileExistsError:
#         print(f"Directory '{path}' already exists.")
# galleries = ['ktwiz','hanwhaeagles_new','skwyverns_new1','ncdinos','samsunglions_new','doosanbears_new1','giants_new2','sh_new','lgtwins_new','tigers_new']
# final_numbers = {'skwyverns_new1':2911195,'ncdinos':6725381,'samsunglions_new':9650799,
#                  'doosanbears_new1':6857697,'giants_new2':13098578,'sh_new':5046485,
#                  'ktwiz':3022358,'hanwhaeagles_new':7807722,'tigers_new':13073779,
#                  'lgtwins_new':10874698}
# COLLECT_COMMENT = False

# crawler = Crawler()
# for idx in range(len(galleries)):
#     create_directory(galleries[idx])
#     for i in range(final_numbers[galleries[idx]]-3000, final_numbers[galleries[idx]]+1):
#         try:
#             res = crawler.crawl(galleries[idx], str(i), COLLECT_COMMENT)
            
#             with open(f"./{galleries[idx]}/{galleries[idx]}_{i}.json", "w", encoding="utf-8") as f:
#                 f.write(json.dumps(res, ensure_ascii=False, indent=4))
#         except Exception as e:
#             print(e)

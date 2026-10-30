import math
import random
import os


import requests
import hmac
import hashlib
import time


from data_process.data_clean import data_clean
from data_process.data_save import save_job
from spider.jobs_types import keywords
from urllib.parse import quote




#定制请求头，请求访问网页
def request_page(url,header):
    response = requests.get(
        url=url,
        headers=header,
        timeout=20
    )
    # 接口返回JSON数据，使用response.json()
    # 将JSON格式转换为Python字典对象
    #print(response.status_code)
    return response.json()

#解析网页，前后端分离，采用json接口，网页是动态渲染的
def parse_page(data,keyword):
    #使用json方法爬取，因为目标网页是前后端分离，json是无限嵌套字典的一种格式
    #查看返回的字典中的关键字
    #print(data.keys())
    resultbody = data["resultbody"]
    #查看关键字resultbody这个字典的中的关键字
    #print(resultbody.keys())
    #接着找下一层字典joblist
    searchData = resultbody["searchData"]
    joblist = searchData["joblist"]
    total_count = int(joblist["totalCount"])
    #print(joblist.keys())
    #接着找关键字items
    jobs = joblist["items"]

    inserted_count = 0          #插入计数器
    duplicate_count = 0         #重复计数器
    error_count = 0             #失败计数器

    max_page = math.ceil(total_count / 20)

    for job in jobs:
        #print(job)
        cleaned_data = data_clean(job,keyword)
        result = save_job(cleaned_data)
        if result == "inserted":
            inserted_count +=1
        elif result == "duplicate":
            duplicate_count +=1
        elif result == "error":
            error_count +=1
    return len(jobs), inserted_count, duplicate_count, error_count,total_count,max_page

# 根据请求路径自动生成Sign
def generate_sign(url_path, young_sign_key):

    sign = hmac.new(
        young_sign_key.encode("utf-8"),
        url_path.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    return sign

young_sign_key = os.getenv("YOUNG_SIGN_KEY")

if __name__ == "__main__":
    total_get = 0
    total_inserted = 0
    total_duplicate = 0
    total_error = 0
    total_pages = 0

    headers = {
        "accept":"application/json, text/plain, */*",
        "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
        "account-id": os.getenv("ACCOUNT_ID"),
        "from-domain":"yjs_web",
        "origin":"https://q.yingjiesheng.com",
        "referer":"https://q.yingjiesheng.com/",
        "partner":"",
        "property":'{"partner":"","webId":6,"fromdomain":"yjs_web"}',
        "sec-ch-ua":'"Not=A?Brand";v="99", "Microsoft Edge";v="151", "Chromium";v="151"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":'"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-site",
        "user-token":os.getenv("USER_TOKEN"),
        "uuid":os.getenv("UUID"),
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0",
    }


for keyword in keywords:
    pagenum = 1
    while True:
        timestamp = str(int(time.time()))
        url = (
            "https://youngapi.yingjiesheng.com/open/noauth/job/search"
            f"?version=2.3.5"
            f"&api_key={os.getenv('API_KEY')}"
            f"&timestamp={timestamp}"
            f"&keyword={quote(keyword)}"
            f"&jobarea=060000%2C090200"
            f"&landmark="
            f"&metro="
            f"&degree="
            f"&jobterm="
            f"&workYear="
            f"&saltype="
            f"&cotype="
            f"&cosize="
            f"&industry="
            f"&requestId="
            f"&pagesize=20"
            f"&pageno={pagenum}"
            f"&searchType=2"
            f"&scene=7"
        )
        #生成签名路径
        url_path = url.replace(
            "https://youngapi.yingjiesheng.com",
            ""
        )
        #自动生成 Sign
        headers["sign"] = generate_sign(
            url_path,
            young_sign_key
        )
        #请求网页
        data = request_page(url, headers)
        get_count, inserted_count, duplicate_count, error_count,total_count,max_page = parse_page(data,keyword)




        total_get += get_count
        total_inserted += inserted_count
        total_duplicate += duplicate_count
        total_error += error_count
        total_pages += 1

        print(
            f"页数：{total_pages} | "
            f"获取：{total_get} | "
            f"新增：{total_inserted} | "
            f"重复：{total_duplicate} | "
            f"失败：{total_error}"
        )

        pagenum +=1

        if get_count == 0:
            print("不存在数据")
            break
        elif  pagenum > max_page:
           print(f"{keyword}已完成爬取，共{max_page}页")
           break

        time.sleep(random.uniform(8,12))

    time.sleep(random.uniform(3,5))

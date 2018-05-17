import requests, time
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Referer": "https://www.csdn.net/nav/ai",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "www.csdn.net",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",

}
headerss = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Referer": "https://www.csdn.net/nav/ai",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.csdn.net",
    "Upgrade-Insecure-Requests": "1",

}
obj_list = list()
cookiess = list()
for i in range(2880):
    t = time.time()
    url = "https://www.csdn.net/api/articles?type=more&category=ai&shown_offset=%.4f" % t
    if i == 1:
        obj_ = requests.get(url, headers=headerss)
        cookiess.append(obj_.cookies)
        continue
    if cookiess:
        obj_ = requests.get(url, headers=headers, cookies=cookiess[0])
        obj_json = obj_.content.decode()
        obj_dict1 = json.loads(obj_json)
        for j in obj_dict1.get("articles"):
            obj_dict = dict()
            obj_dict["href"] = j.get('url')
            obj_dict["num"] = j.get('views')
            obj_dict["title"] = j.get('title')
            obj_list.append(obj_dict)
            # time.sleep(30)  # 大概30s出现一次内容推荐
print(obj_list)  # 存起来


# 					338
# dc_session_id	10_1526467356377.129413	.csdn.net	/	2025-01-01T00:00:00.000Z	104
# uuid_tt_dd	10_9892587100-1526467356377-596659	.csdn.net	/	2025-01-01T00:00:00.000Z	112
# uuid_tt_dd	4020285388244105550_20180516	csdn.net	/	3650.0 days	122
# Strict-Transport-Security: max-age= 31536000
#
#
#
#
#
# Connection: keep-alive
# Content-Type: application/json
# Date: Wed, 16 May 2018 10:42:36 GMT
# Keep-Alive: timeout=20
# Server: openresty
# Set-Cookie: uuid_tt_dd=10_9892587100-1526467356377-596659; Expires=Thu, 01 Jan 2025 00:00:00 GMT; Path=/; Domain=.csdn.net;
# Set-Cookie: dc_session_id=10_1526467356377.129413; Expires=Thu, 01 Jan 2025 00:00:00 GMT; Path=/; Domain=.csdn.net;
# Set-Cookie: uuid_tt_dd=4020285388244105550_20180516; expires=Sat, 13-May-2028 10:42:36 GMT; Max-Age=315360000; path=/; domain=csdn.net
# Strict-Transport-Security: max-age= 31536000
# Transfer-Encoding: chunked
# X-Powered-By: PHP/5.5.23

# ookie: \
# dc_session_id=10_1526467356377.129413;
# dc_session_id=10_1526467356377.129413;
# uuid_tt_dd=4020285388244105550_20180516
# uuid_tt_dd=4020285388244105550_20180516
#
#
# Host: www.csdn.net

import requests
import json
from time import sleep

from DB.mysql_db import Mysql_db

def get_data1(cookie_header):
    url = "http://api.bilibili.com/x/answer/v3/base"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Referer": "http://account.bilibili.com/answer/base/",
        "Cookie": cookie_header,
    }
    db = Mysql_db()
    content = json.loads(requests.get(url, headers=headers).text)
    print(content)
    if content['code'] == 0:
        for data in content['data']['items']:
            db.query("""INSERT INTO `1` (qs_id,ans_img,qs_h,qs_y,ans1_hash,ans2_hash,ans3_hash,ans4_hash,ans0_h,ans0_y,ans1_h,ans1_y,ans2_h,ans2_y,ans3_h,ans3_y) VALUES ({},'{}',{},{},'{}','{}','{}','{}',{},{},{},{},{},{},{},{})""".format(data['qs_id'],data['ans_img'],data['qs_h'],data['qs_y'],data['ans1_hash'],data['ans2_hash'],data['ans3_hash'],data['ans4_hash'],data['ans0_h'],data['ans0_y'],data['ans1_h'],data['ans1_y'],data['ans2_h'],data['ans2_y'],data['ans3_h'],data['ans3_y']))

def get_data3(cookie_header=None):
    url = "http://api.bilibili.com/x/answer/v3/pro?type_ids=18,23,26"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Referer": "http://account.bilibili.com/answer/base/",
        "Cookie": "buvid3=57F6645E-4ACB-428B-BF8B-E1616F223DB928902infoc; LIVE_BUVID=AUTO4015419970471432; finger=edc6ecda; sid=8ro76kbf; _dfcaptcha=136b24c60eb8bfeccc36c2f734f951bc; im_notify_type_386497530=0; DedeUserID=386518487; DedeUserID__ckMd5=4a1c41ae9974822a; SESSDATA=34bd5a1b%2C1544590609%2C5b462999; bili_jct=2f8cf5e19cd109a2046797c2d64311b3",
    }
    db = Mysql_db()
    content = json.loads(requests.get(url, headers=headers).text)
    print(content)
    if content['code'] == 0:
        for data in content['data']:
            db.query(
                """INSERT INTO `3` (qs_id,ans_img,qs_h,qs_y,ans1_hash,ans2_hash,ans3_hash,ans4_hash,ans0_h,ans0_y,ans1_h,ans1_y,ans2_h,ans2_y,ans3_h,ans3_y) VALUES ({},'{}',{},{},'{}','{}','{}','{}',{},{},{},{},{},{},{},{})""".format(
                    data['qs_id'], data['ans_img'], data['qs_h'], data['qs_y'], data['ans1_hash'], data['ans2_hash'],
                    data['ans3_hash'], data['ans4_hash'], data['ans0_h'], data['ans0_y'], data['ans1_h'],
                    data['ans1_y'], data['ans2_h'], data['ans2_y'], data['ans3_h'], data['ans3_y']))


if __name__ == '__main__':
    cookies = [{"domain": ".bilibili.com", "expiry": 1542037479.918121, "httpOnly": False, "name": "DedeUserID", "path": "/", "secure": False, "value": "386518682"}, {"domain": ".bilibili.com", "expiry": 1573488835.3917, "httpOnly": False, "name": "sid", "path": "/", "secure": False, "value": "imfw3h5t"}, {"domain": ".bilibili.com", "expiry": 1636560835.529005, "httpOnly": False, "name": "buvid3", "path": "/", "secure": False, "value": "A7BD0A54-B366-4ED1-95F2-55B8A81753AF48458infoc"}, {"domain": ".bilibili.com", "expiry": 1544544835, "httpOnly": False, "name": "finger", "path": "/", "secure": False, "value": "edc6ecda"}, {"domain": ".bilibili.com", "expiry": 1542037479.918209, "httpOnly": False, "name": "bili_jct", "path": "/", "secure": False, "value": "044047f795aeee067213062b002a9cfe"}, {"domain": ".bilibili.com", "expiry": 1542037479.91816, "httpOnly": False, "name": "DedeUserID__ckMd5", "path": "/", "secure": False, "value": "4603a31a25c0279c"}, {"domain": ".bilibili.com", "expiry": 1542037479.918185, "httpOnly": True, "name": "SESSDATA", "path": "/", "secure": False, "value": "06717079%2C1542037480%2Cfc388370"}, {"domain": ".bilibili.com", "expiry": 1541956489.640048, "httpOnly": True, "name": "_dfcaptcha", "path": "/", "secure": False, "value": "e2e45718703a7d27bd05cff8a476b8e7"}, {"domain": ".bilibili.com", "expiry": 2177452799.022167, "httpOnly": False, "name": "LIVE_BUVID", "path": "/", "secure": False, "value": "AUTO8415419528828675"}]
    cookie_header = ""
    for cookie in cookies:
        cookie_header += cookie['name'] + "=" + cookie['value'] + "; "
    while(True):
        get_data1(cookie_header)
        # sleep(10)
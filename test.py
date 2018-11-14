import requests
import hashlib

from DB.mysql_db import Mysql_db

def download_pic():
    db = Mysql_db()
    results = db.query("select ans_img from `1` group by qs_id;")
    print(results)
    for i,result in enumerate(results):
        url = result[0]
        print(url)
        with open("R:/q1_img_list/{}".format(str(i)+url[-36:]), "wb") as f:
            f.write(requests.get(url).content)

def getFileMD5(filepath):

    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()


def text_to_db():
    with open("R:/ans1.txt") as f:
        lines = f.readlines()
    db = Mysql_db()
    for line in lines:
        qs_id = line.split(":")[0]
        ans = line.split(":")[1].strip()
        print(qs_id, ans)
        db.query("INSERT INTO `ans1` (qs_id, ans) VALUES ({}, '{}')".format(qs_id, ans))

if __name__ == '__main__':
    # print(getFileMD5("R:/pic/5713/1048e6f854ec755345a6386716ffdfe57.jpg"))
    download_pic()
    # text_to_db()
    # print(getFileMD5("R://d0e47a13f05b3ca35a8d1329a9bac3a6.jpg"))
import hashlib
import os
import requests

from DB.mysql_db import Mysql_db


class Update_md5(object):

    def __init__(self, url):
        self.url = url
        self.filename = url[-36:]
        self.download()

    def download(self):
        print(self.url)
        with open("./pic/{}".format(self.filename), "wb") as f:
            f.write(requests.get(self.url).content)

    def getFileMD5(self):
        f = open("./pic/{}".format(self.filename), 'rb')
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        f.close()
        return str(hash).upper()

    def __del__(self):
        os.remove("./pic/"+self.filename)

if __name__ == '__main__':
    db = Mysql_db()
    while(True):
        results = db.query("SELECT ans_img FROM `1` WHERE  img_md5 IS NULL LIMIT 100;")
        if results:
            for result in results:
                print(result[0])
                md5 = Update_md5(result[0]).getFileMD5()
                db.query("UPDATE `1` SET img_md5='{}' WHERE ans_img='{}'".format(md5, result[0]))
        else:
            exit()

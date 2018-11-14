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
    print(Update_md5("https://i1.hdslb.com/bfs/member/6d1962845f9e37de4066e645e8a2f03b.jpg").getFileMD5())

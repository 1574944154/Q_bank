import requests
import hashlib

from DB.mysql_db import Mysql_db

def download_pic():
    db = Mysql_db()
    results = db.query("SELECT ans_img FROM `dati_rawdata`.`3` WHERE `ans_img` LIKE '%048e6f854ec755345a6386716ffdfe57%';")
    print(results)
    for i,result in enumerate(results):
        url = result[0]
        print(url)

        with open("R:/pic/5713/{}".format(str(i)+url[-36:]), "wb") as f:
            f.write(requests.get(url).content)



def getFileMD5(filepath):

    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()



if __name__ == '__main__':
    print(getFileMD5("R:/pic/5713/1048e6f854ec755345a6386716ffdfe57.jpg"))
    # download_pic()
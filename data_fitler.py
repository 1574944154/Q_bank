
from DB.mysql_db import Mysql_db


db = Mysql_db()

results = db.query("select `1`.qs_id,ans_img,ans1.img_md5,ans1.ans from dati_rawdata.`1`, dati_rawdata.ans1 where ans1.img_md5=`1`.img_md5 group by qs_id;")

for result in results:
    print(result)
    if result[3] == 'A':
        qs_id,img_md5_true = db.query("select qs_id,ans1_hash from `1` where qs_id='{}' and ans_img='{}'".format(result[0],result[1]))[0]
    elif result[3] == 'B':
        qs_id,img_md5_true = db.query(
            "select qs_id,ans1_hash from `1` where qs_id='{}' and ans_img='{}'".format(result[0], result[1]))[0]
    elif result[3] == 'C':
        qs_id,img_md5_true = db.query(
            "select qs_id,ans1_hash from `1` where qs_id='{}' and ans_img='{}'".format(result[0], result[1]))[0]
    elif result[3] == 'D':
        qs_id,img_md5_true = db.query(
            "select qs_id,ans1_hash from `1` where qs_id='{}' and ans_img='{}'".format(result[0], result[1]))[0]

    print(qs_id, img_md5_true)
    db.query("update ans1 set qs_id='{}', img_hash_true='{}' where img_md5='{}'".format(qs_id,img_md5_true,result[2]))
from flask import Flask, render_template, url_for, request, redirect
import os
import hashlib

from DB.mysql_db import Mysql_db


app = Flask(__name__)

db = Mysql_db()

def getFileMD5(path):
    f = open(path, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()


@app.route("/")
def index():
    path = "./static/q1_img_list/"+os.listdir("./static/q1_img_list/")[0]
    print(path)
    return render_template("index.html", path=path)

@app.route("/revice", methods=['POST'])
def revice():
    img = request.form.get("img")
    ans = request.form.get("ans")
    path = "./static/q1_img_list/{}.jpg".format(img)
    md5 = getFileMD5(path)
    os.remove(path)
    db.query("INSERT INTO ans1 (img_md5,ans) VALUES ('{}','{}')".format(md5,ans))
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
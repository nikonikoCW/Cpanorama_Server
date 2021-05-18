from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import uuid
app = Flask(__name__)
xx = 123
@app.route('/')
def hello_world():
    print(xx)
    return 'Hello World!'

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        a = uuid.uuid1()
        a = str(a)
        nowFilePath = os.path.dirname(__file__)
        uuidFile = os.path.join(nowFilePath,"static\\uploads\\"+a)
        print(f)
        os.makedirs(uuidFile)
        print(f.filename.rsplit('.', 1)[1])
        upload_path = os.path.join(uuidFile,f.filename)  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        
        f.save(upload_path)
        b = {"info":'file uploaded successfully',"code":a,"name":f.filename}
    return b
@app.route('/deal/<img>')
def dealImg(img):
    os.system('python test.py')
    nowFilePath = os.path.dirname(__file__)
    uuidFile = os.path.join(nowFilePath,"static\\uploads\\"+img)
    imgUrl = os.path.join(uuidFile,d)
    os.system('python generate.py '+imgURL)
    return '处理完成!'+img

@app.route('/deal',methods=["POST"])
def QiePian():
    if request.method == "POST":
        #fileName是返回的code
        #imaName就是返回的图片名称
        img = request.form['fileName']
        d = request.form['imgName']
        os.system('python test.py')
        nowFilePath = os.path.dirname(__file__)
        uuidFile = os.path.join(nowFilePath,"static\\uploads\\"+img)
        outputUrl = os.path.join(uuidFile,'output')
        imgUrl = os.path.join(uuidFile,d)
        print(uuidFile,imgUrl)
        os.system('python generate.py -o %s %s'%(outputUrl,imgUrl))
        return '处理完成!'

if __name__ == '__main__':
    app.run()

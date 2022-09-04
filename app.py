from flask import Flask, request
from PIL import Image

app=Flask(__name__)

@app.route('/', methods=['GET']) #setting the app route with GET method
def abc():
    return '<h1>Hey</h1>'  #This returns to the API which gives a form of the o/p to the Front end

#creating another route
@app.route('/xyz',methods=['GET'])
def xyz():
    return '<h1>Hola</h1>'    

@app.route('/user',methods=['GET'])
def user():     #input as /user?name=Shamik
    name=request.args['name']
    return f'Hello {name}!!!'

@app.route('/user2',methods=['POST'])
def user2():     #This, we cannot invoke through browser
    name=request.form['name']
    return f'Hello {name}!!!'    

@app.route('/img',methods=['POST'])
def img():
    im=request.files['image']  #taking an image file as input
    im=Image.open(im)
    return str(im.size)   #always return in string cuz its html

if __name__=='__main__':     #will only run if it is called from this method
    app.run(port=8000, debug=True)  #only app.run() will suffice. Port 8000 is for the port number. Debug = True means that it will automatically restarts when anything is updated!
#range of port: 0-65535, ports 8000 and so on aren't reserved for anything, so we can use it for public.

# -*- coding: utf8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Lucas ! Papai !'

@app.route('/ulala')
def funcao_ulala():
    return '''
    <h1>
    000000
     !!</h1>
     <img src="/static/codigo.png"> <br/>
   é muito facil fazer um site
    '''

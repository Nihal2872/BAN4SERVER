import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://Nihal2872:git@github.com/Nihal2872/USERBOT okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m USERserver1 &")

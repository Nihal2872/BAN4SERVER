import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://Nihal2872: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@github.com/Nihal2872/KhushiBot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m main.py &")

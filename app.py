
from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Kushal M G:R21EN112"
    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'Unknown'
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')


    top_output = subprocess.getoutput("top -b -n 1")

    return f'''
    Name: {name}<br>
    User: {username}<br>
    Server Time (IST): {server_time}<br><br>
    TOP output:<br><pre>{top_output}</pre>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
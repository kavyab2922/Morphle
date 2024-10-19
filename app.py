from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "B Kavya"
    
    system_username = os.getlogin()
    
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')
    
    # Return HTML 
    return f"""
    <html>
    <head><title>HTOP</title></head>
    <body>
    <h1>System Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {system_username}</p>
    <p><strong>Server Time:</strong> {server_time}</p>
    <pre>{top_output}</pre>
    </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000)
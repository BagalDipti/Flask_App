from flask import Flask,render_template
import socket
import getpass
import os.path
import uuid


app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        host = socket.gethostbyaddr(socket.gethostname())
        user_name = getpass.getuser()
        homedir = os.path.expanduser("~")
        Uuid=hex(uuid.getnode())

        return render_template('index.html', hostname=host_name, ip=host_ip, host=host, username=user_name, homepath=homedir, Uuid=Uuid )
    except:
        return render_template('error.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5678)

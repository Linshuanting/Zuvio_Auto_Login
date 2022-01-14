import re
import data_save
import threading
import auto_sign_timer
from flask import Flask, url_for, render_template, redirect, request

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.__flask_init__()
        return None

    def __flask_init__(self):
        pass

    def run_server(self):
        while (True):
            self.app.run(host='localhost', threaded=True ,
            port=5000, debug=True)
        return None
        
data = data_save.Data_Service()
sign = auto_sign_timer.signin_timer(data)
server = Server()

@server.app.route('/')
def root():
    return redirect(url_for('setting'))

@server.app.route('/setting', methods = ['GET', 'POST'])
def setting():
    if (request.method == 'POST'):
        # if request.form != None:
            # set_json(request.form)
        start()
    else:
        print("Post Not happened")
    return render_template('setting.html')

@server.app.route('/status', methods=['GET', 'POST'])
def status():
    return render_template('status.html')

def set_json(form):
    name = form['course_name']
    time_list = list()
    account_list = list()
    for i in form:
        if (("time" in i) & (form[i] != '')):
            tmp = {
                "start_time": form[i].split(' ')[0],
                "end_time": form[i].split(' ')[1]
            }
            time_list.append(tmp)
        if (("account" in i) & (form[i] != '')):
            tmp = {
                "uid": form[i].split(' ')[0],
                "passwd": form[i].split(' ')[1]
            }
            account_list.append(tmp)

    data.set_data(name, time_list, account_list)

def start():
    sign.run_timer()



if __name__ == "__main__":
    print("run server")
    threading.Thread(server.run_server()).start()

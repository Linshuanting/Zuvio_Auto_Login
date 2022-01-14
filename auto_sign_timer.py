from datetime import datetime, timedelta
import pytz
import time
import data_save
from runLogin import RunLogin
from apscheduler.schedulers.background  import BackgroundScheduler 

class signin_timer():
    def __init__(self, data_save:data_save.Data_Service):
        # self.TIMEZONE = pytz.timezone('Asia/Taipei')
        self.login = RunLogin()
        self.sched = BackgroundScheduler(timezone = 'Asia/Taipei', daemon=True)
        self.data_save = data_save


    def start_timer(self, task, time, name, account, run_amounts):

        self.sched.add_job(task, 'date', run_date=time, args = [name, account, run_amounts])
        

    def test_timer(self, task, times, name, account, run_amounts):

        self.sched.add_job(task,'date', run_date=datetime.now(), args = [name, account, run_amounts])
        self.sched.add_job(self.execute, run_date=datetime.now())

    def get_execute_time(self, time):
        day = datetime.now().strftime("%Y-%m-%d ")
        needTime = time["start_time"] + ":00"
        return day + needTime

    def get_amount_time(self, time):
        start_time = int(time["start_time"].split(':')[0])*60 + int(time["start_time"].split(':')[1])
        end_time = int(time["end_time"].split(':')[0])*60 + int(time["end_time"].split(':')[1])
        return end_time - start_time

    def run_timer(self):
        times = self.data_save.get_time_data()
        accounts = self.data_save.get_account_data()
        course_name = self.data_save.get_course_name()

        for time in times:
            exe_time = self.get_execute_time(time)
            exe_amount = self.get_amount_time(time)
            for acc in accounts:
                # self.start_timer(self.login.run ,exe_time, course_name, acc, exe_amount)
                self.test_timer(self.login.run, exe_time, course_name, acc, exe_amount)

        self.sched.start()

    def execute(self):
        print("test data:: This is multithread")

if __name__ == "__main__":
    ds = data_save.Data_Service()
    st = signin_timer(ds)
    st.run_timer()
    time.sleep(1000)

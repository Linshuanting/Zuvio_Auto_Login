import codecs
import json
from pathlib import Path


class Data_Service():
    def __init__(self):
        self.ACCOUNT_JSON_FILE_NAME = "./account.json"
        self.STATUS_JSON_FILE_NAME = "./status.json"
        self.TIME_JSON_FILE_NAME = "./time.json"
        self.DATA_JSON_FILE_NAME = "./data.json"
        self.ENCODING = 'utf-8'

    def set_time_data(self, times):
        json.dump(times, codecs.open(self.TIME_JSON_FILE_NAME, 'w', self.ENCODING),
                  ensure_ascii=False, indent=4, sort_keys=False)
        return None

    def get_time_data(self):
        if (Path(self.DATA_JSON_FILE_NAME).is_file() is True):
            file = json.load(open(self.DATA_JSON_FILE_NAME, encoding=self.ENCODING))
            return file["time"]
        else:
            return False

    def set_account_data(self, accounts):
        json.dump(accounts, codecs.open(self.ACCOUNT_JSON_FILE_NAME, 'w',
                                        self.ENCODING), ensure_ascii=False, indent=4, sort_keys=False)
        return None

    def get_account_data(self):
        if (Path(self.DATA_JSON_FILE_NAME).is_file() is True):
            file = json.load(open(self.DATA_JSON_FILE_NAME, encoding=self.ENCODING))
            return file["account"]
        else:
            return False

    def get_course_name(self):
        if (Path(self.DATA_JSON_FILE_NAME).is_file() is True):
            file = json.load(open(self.DATA_JSON_FILE_NAME, encoding=self.ENCODING))
            return file["course_name"]
        else:
            return False

    def set_data(self,course_name,  times_list ,accounts_list):
        data = {
            'course_name': course_name,
            'time': times_list,
            'account': accounts_list
        }
        json.dump(data, codecs.open(self.DATA_JSON_FILE_NAME, 'w',
                                        self.ENCODING), ensure_ascii=False, indent=4, sort_keys=False)
        return None
    
    def get_data(self):
        if (Path(self.DATA_JSON_FILE_NAME).is_file() is True):
            return json.load(open(self.DATA_JSON_FILE_NAME, encoding=self.ENCODING))
        else:
            return False

if __name__=='__main__':
    ds = Data_Service()
    print(ds.get_time_data())

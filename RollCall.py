from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

time_interval = 60

class RC():
    def __init__(self, driver):
        self.driver = driver
        self.state = 0

        return None

    def find_course(self, course_name):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        course_list = soup.find_all('div', class_='i-m-p-c-a-c-l-course-box')
        course_list_button = self.driver.find_elements_by_class_name(
            'i-m-p-c-a-c-l-course-box')

        for course, button in zip(course_list, course_list_button):
            course_name_data = course.find(
                'div', class_='i-m-p-c-a-c-l-c-b-t-course-name')
            if (course_name_data.getText() == course_name):
                return button
            else:
                print("Not Correct Ans")

        return None

    def Button_Click(self, btn):
        btn.click()

    def get_driver(self):
        return self.driver

    def find_RC_Page(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        button_box = soup.find_all('div', class_='g-f-button-box')
        button_box_button = self.driver.find_elements_by_class_name(
            'g-f-button-box')

        for box, button in zip(button_box, button_box_button):
            box_title = box.find('div', class_='g-f-b-b-title')
            if (box_title.getText() == "點名簽到"):
                # print(box_title)
                return button

        return None
    
    def find_RC_Button(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        if (soup.find('div', class_='no-active')):
            return None
        
        id_name = 'submit-make-rollcall"'
        sign = soup.find('div', id=id_name)
        signbtn = self.driver.find_element_by_id(
            id_name)
        
        return signbtn


    def error(self, message):
        print("Error happened: "+message)
        exit(1)

    def toCourses(self, course_name, amount):
        self.state = 1
        for i in range(1, amount):
            if self.toCourse(course_name):
                return True
            print(f'state {self.state} is error')
            time.sleep(time_interval)
        return False

    def toCourse(self, course_name):
        
        if self.state == 1:
            btn = self.find_course(course_name)
            if (btn == None):
                return False
            else:
                self.Button_Click(btn)
                self.state +=1

        if self.state == 2:
            btn = self.find_RC_Page()
            if (btn == None):
                return False
            else:
                self.Button_Click(btn)
                self.state +=1
        
        if self.state == 3:
            btn = self.find_RC_Button()
            if (btn == None):
                return False
            else:
                self.Button_Click(btn)
            
        return True

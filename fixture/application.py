from selenium import webdriver
from fixture.session import SessionHelper
import os

class Application:
    def __init__(self, browser, base_url):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome(executable_path=os.path.abspath(r"C:\dev\web_test_framework\webdrivers\chromedriver.exe"))
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecoglized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.wd.get("about:blank")
        self.baseurl=base_url


    def open_main_page(self):
        wd = self.wd
        wd.maximize_window()
        print("Opening main page")
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_page(self, page_name):
        self.wd.find_element_by_link_text(page_name).click()
        self.wd.implicitly_wait(3)
        #elf.session.wait_for_page_load('https://newventurevisions.com/contact-us/')

    def send_message(self,name, second_name, email, phone, subject, message):
        wd = self.wd
        self.wd.find_element_by_id("wpforms-181-field_3_4").click()
        wd.execute_script("window.scrollTo(0, 200)")
        self.wd.find_element_by_css_selector("#wpforms-181-field_0").send_keys(name)
        self.wd.find_element_by_css_selector("#wpforms-181-field_0-last").send_keys(second_name)
        self.wd.find_element_by_css_selector("#wpforms-181-field_1").send_keys(email)
        self.wd.find_element_by_css_selector("#wpforms-181-field_4").send_keys(phone)
        self.wd.find_element_by_css_selector("#wpforms-181-field_5").send_keys(subject)
        self.wd.find_element_by_css_selector("#wpforms-181-field_2").send_keys(message)




__author__ = 'Alex'

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("submit").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Log out").click()
        alert = wd.switch_to_alert()
        alert.accept()

    def app_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Log out")) > 0

    def insure_logout(self):
        wd = self.app.wd
        if self.app_logged_in():
            self.logout()

    def insure_login(self, username, password):
        wd = self.app.wd
        if self.app_logged_in():
            return
        self.login(username, password)

    def wait_for_page_load(self, url):
        wd = self.app.wd
        wd.implicitly_wait(10)
        new_page = wd.find_element_by_tag_name(url)
        return


from selenium import webdriver
from time import sleep
from info import user, password


class Bot():
    def __init__(self):
        self.login(user, password)

    def login(self, username, password):
        self.driver = webdriver.Edge()
        self.driver.get('https://instagram.com')
        sleep(3)
        usename_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        usename_input.send_keys(username)
        sleep(2)
        password_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]').click()
        sleep(6)
        self.driver.get(
            'https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(5)

        list_of_user = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_user.append(names.text)

        for i in list_of_user:
            self.driver.get(f'https://instagram.com/{i}')
            sleep(3)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button/div').click()
            sleep(5)
            self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            sleep(5)



def main():
    mybot = Bot()


if __name__ == '__main__':
    main()

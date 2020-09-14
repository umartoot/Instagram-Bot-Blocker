from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        PATH = "/Users/tootles/Desktop/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.instagram.com/")

        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()

        sleep(4)

        self.driver.find_element_by_class_name("cmbtv").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("poop")
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").clear()
        sleep(5)


pw = input("Password: ")
InstaBot("umrttl", pw)
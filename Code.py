from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def setDriverandOptions():
    # set options and terms
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Hide Chrome Window

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    return driver


def login(driver):
    linkedinurl = 'https://www.linkedin.com/'

    driver.get(linkedinurl)
    # input username
    username = driver.find_element_by_name('session_key')

    username.send_keys(Keys.CONTROL + "a")
    username.send_keys(Keys.DELETE)
    username.send_keys('Kareemh17@gmail.com')  # enter username here

    # input password
    password = driver.find_element_by_name('session_password')

    password.send_keys(Keys.CONTROL + "a")
    password.send_keys(Keys.DELETE)
    password.send_keys('K4r33m00')  # enter password here

    # login to linkedin account
    submit = driver.find_element_by_id('login-submit')
    submit.click()
    return driver


def search(driver):
    # Enter your message here
    Message = "Dear {0},\n my name is Kareem Hirani and I am currently a freshman at Texas A&M University, College Station " \
              "intending to major in Computer Science. " \
              "I am currently search for an internship for the summer of 2019 and would like to ask if your company " \
              "is offering any internship positions in computer science or software engineering. \n" \
              "Thank you, \n " \
              "Kareem Hirani"
    # enter into search bar
    file = open('Companies.txt', 'r', encoding='utf-8')

    for company in file:
        line = str(company)

        time.sleep(1)

        linkedinsearchbar = driver.find_element_by_tag_name('input')

        linkedinsearchbar.send_keys(Keys.CONTROL + "a")
        linkedinsearchbar.send_keys(Keys.DELETE)

        linkedinsearchbar.send_keys('university recruiter ' + line)  # enter query here

        time.sleep(1)

        # parse linked in profiles associated with search
        namestring = str(driver.find_element_by_css_selector('span.name.actor-name').text)
        name = namestring.split(' ')[0]
        driver.find_element_by_css_selector \
            ('button.search-result__action-button.search-result__actions--primary.button-secondary-medium.m5') \
            .send_keys('\n')  # click first connect

        driver.find_element_by_css_selector('button.button-secondary-large.mr1').send_keys('\n')  # send note

        messagetextbox = driver.find_element_by_name('message')  # toggle message box
        print('Writing message to {0}'.format(name))
        messagetextbox.send_keys(Message.format(name))  # write message
        print('message sent')
        driver.find_element_by_css_selector('button.button-primary-large.ml1').send_keys('\n')  # submit message

        time.sleep(1)


if __name__ == '__main__':
    driver = setDriverandOptions()
    driver = login(driver)
    search(driver)

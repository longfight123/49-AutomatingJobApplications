"""Linkedin Job Application Automation

This script automates applying to jobs on linkedin.

This script requires that 'selenium',
 'python_dotenv' be installed within the Python
environment you are running this script in.
You must also have a linkedin account and upload
your resume into your Linkedin account.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv('.env')
LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PW = os.getenv('LINKEDIN_PW')
PHONE = os.getenv('PHONE')
LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?distance=25&f_L=Calgary%2C%20Alberta%2C%20Canada&f_LF=f_AL&geoId=102199904&keywords=warehouse&location=Calgary%2C%20Alberta%2C%20Canada&sortBy=R'
CHROME_EXECUTABLE_PATH = 'C:\Development\chromedriver.exe'


driver = webdriver.Chrome(CHROME_EXECUTABLE_PATH)
driver.get(LINKEDIN_URL)
time.sleep(3)
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()
time.sleep(3)
email = driver.find_element_by_id('username')
email.send_keys(LINKEDIN_EMAIL)
password = driver.find_element_by_id('password')
password.send_keys(LINKEDIN_PW)
sign_in = driver.find_element_by_css_selector('.login__form_action_container button')
sign_in.click()
time.sleep(6)

# Apply to all jobs

postings_list = driver.find_elements_by_css_selector('.jobs-search-results__list .job-card-list__title')
print(len(postings_list))
for posting in postings_list:
    time.sleep(2)
    posting.click()
    time.sleep(2)
    try:
        easy_apply = driver.find_element_by_css_selector('.jobs-apply-button--top-card .jobs-apply-button')
        easy_apply.click()
    except NoSuchElementException:
        continue
    time.sleep(2)
    try:
        phone = driver.find_element_by_css_selector('.jobs-easy-apply-form-section__grouping .display-flex input')
        phone.send_keys(PHONE)
    except NoSuchElementException:
        exit = driver.find_element_by_css_selector('.artdeco-modal button')
        exit.click()
        time.sleep(3)
        confirm = driver.find_element_by_css_selector('.artdeco-modal__actionbar .artdeco-button--primary')
        confirm.click()
        continue
    submit = driver.find_element_by_css_selector('.justify-flex-end button')
    submit.click()
    exit = driver.find_element_by_css_selector('.artdeco-modal button')
    exit.click()
    time.sleep(3)
    try:
        #This is for the confirm button to discard if the next page is not a submit page
        confirm = driver.find_element_by_css_selector('.artdeco-modal__actionbar .artdeco-button--primary')
        confirm.click()
    except NoSuchElementException:
        try:
            #This is to close the page after a successful submit application
            exit = driver.find_element_by_css_selector('.artdeco-modal button')
            exit.click()
            time.sleep(2)
        except NoSuchElementException:
            continue


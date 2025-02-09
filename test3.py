from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to the EgyptAir website
driver.get("https://expedia.com")
# Use WebDriverWait to wait for the elements to be present and visible
wait = WebDriverWait(driver, 10)
actions =ActionChains(driver)

#Booking Airline


# flight= wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Flights"))).click()
# one_way= wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "One-way"))).click()

# # time.sleep(1000)
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Leaving from']")))
# button.click()
# fromm= wait.until(EC.presence_of_element_located((By.ID, "origin_select"))).send_keys("Alexandria (ALY - All Airports) Egypt",Keys.ENTER)

# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Going to']")))
# button.click()
# fromm= wait.until(EC.presence_of_element_located((By.ID, "destination_select"))).send_keys("Rome (and vicinity), Lazio, Italy",Keys.ENTER)

# search = wait.until(EC.element_to_be_clickable((By.ID, "search_button"))).click()

# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='select-link'].uitk-card-link"))).click()
# select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='select-button'].uitk-button"))).click()




# log in
# ahmedwaelsafwat@gmail.com
# pass = Ahmed_123

# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.uitk-button[href*='/user/signin?ckoflag=0']")))
# button.click()
# # driver.get("https://www.expedia.com/login?ckoflag=0&uurl=e3id%3Dredr%26rurl%3D%2F%3Flogout%3D1")

# email= wait.until(EC.presence_of_element_located((By.ID, "loginFormEmailInput"))).send_keys("ahmedwaelsafwat@gmail.com")
# button = wait.until(EC.element_to_be_clickable((By.ID, "loginFormSubmitButton"))).click()
# pass_option = wait.until(EC.element_to_be_clickable((By.ID, "passwordButton"))).click()
# passw= wait.until(EC.presence_of_element_located((By.ID, "enterPasswordFormPasswordInput"))).send_keys("Ahmed_123")
# time.sleep(5)
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#enterPasswordFormSubmitButton.uitk-button-primary"))).click()
# time.sleep(5)

# skip_for_now_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.uitk-button-tertiary[data-context='uitk-form-context']"))).click()
# time.sleep(5)

# continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-stid='one-key-onboarding-welcome-screen-primary-button'].uitk-button-primary"))).click()



# Payment
# driver.get("https://www.expedia.com/Checkout/V1/FlightCheckout?tripid=c9977cb6-6d03-5409-8150-cbf72fd153e2&c=4ba4fc7d-999d-4864-a26f-0acd27daefd7")
# #Adult no.1
# f_name = wait.until(EC.presence_of_element_located((By.ID, "firstname[0]"))).send_keys("Ahmed ",Keys.ENTER)
# m_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[0].middleName']"))).send_keys("Wael")
# l_name = wait.until(EC.presence_of_element_located((By.ID, "lastname[0]"))).send_keys("safwat ",Keys.ENTER)
# email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email'][type='email']"))).send_keys("Ahmedwael@gmail.com ",Keys.ENTER)
# no1= wait.until(EC.presence_of_element_located((By.ID, "phone-number[0]"))).send_keys("0000000000 ",Keys.ENTER)
# male = wait.until(EC.element_to_be_clickable((By.ID, "gender_male[0]"))).click()
# dropdown_day = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[0].dateOfBirth.day']")))
# wait = WebDriverWait(driver, 20)
# select = Select(dropdown_day)
# select.select_by_value("15")
# wait = WebDriverWait(driver, 20)
# dropdown_month = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[0].dateOfBirth.month']"))) 
# select = Select(dropdown_month)
# select.select_by_value("05") 
# wait = WebDriverWait(driver, 20)
# dropdown_year = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[0].dateOfBirth.year']"))) 
# select = Select(dropdown_year)
# select.select_by_value("2003") 

# #  Adult no2
# f_name = wait.until(EC.presence_of_element_located((By.ID, "firstname[1]"))).send_keys("mohamed ",Keys.ENTER)
# m_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[1].middleName']"))).send_keys("ahmed")
# l_name = wait.until(EC.presence_of_element_located((By.ID, "lastname[1]"))).send_keys("sas ",Keys.ENTER)
# male = wait.until(EC.element_to_be_clickable((By.ID, "gender_male[1]"))).click()
# dropdown_day = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[1].dateOfBirth.day']")))
# wait = WebDriverWait(driver, 20)
# select = Select(dropdown_day)
# select.select_by_value("15")
# wait = WebDriverWait(driver, 20)
# dropdown_month = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[1].dateOfBirth.month']"))) 
# select = Select(dropdown_month)
# select.select_by_value("05") 
# wait = WebDriverWait(driver, 20)
# dropdown_year = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='tripPreferencesRequest.airTripPreferencesRequest.travelerPreferences[1].dateOfBirth.year']")))
# select = Select(dropdown_year)
# select.select_by_value("2003") 


# checkbox = wait.until(EC.element_to_be_clickable((By.ID, "no_insurance"))).click()
# submit = wait.until(EC.element_to_be_clickable((By.ID, "complete-booking"))).click()

   



# The rent car feature

Car = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cars"))).click()
pickup = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Pick-up']"))).click()
time.sleep(1)
pickup_data = wait.until(EC.presence_of_element_located((By.ID, "pick_up_location"))).send_keys("Las Vegas, Nevada, United States of America ",Keys.ENTER)
dropoff = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Same as pick-up']"))).click()
time.sleep(1)
pickup_data = wait.until(EC.presence_of_element_located((By.ID, "drop_off_location"))).send_keys("Salt Lake City, UT, United States of America (SLC-Salt Lake City Intl.)",Keys.ENTER)

dropoff_time = driver.find_element(By.ID, 'drop_off_time')
select = Select(dropoff_time) 
select.select_by_visible_text('5:30pm') 
search = wait.until(EC.element_to_be_clickable((By.ID, "search_button"))).click()
time.sleep(3)
car = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Reserve Item, Midsize SUV from Dollar Rent A Car at $284 total']").click()

time.sleep(1000)
driver.quit()

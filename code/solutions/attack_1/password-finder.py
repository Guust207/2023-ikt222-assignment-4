import string


def password_finder(password_length):
    test = "123456789012ab567"
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
            # Send password with Selenium
            time_check = 0  # Get with Selenium
            if time_check > total_time:
                # Correct character!
                correct_password += character
                filler_password = filler_password[1:]
                total_time += 1
                break

    print(correct_password)

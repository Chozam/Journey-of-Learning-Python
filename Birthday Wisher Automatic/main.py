##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as rdm
import smtplib

my_email = "fourthwall165@gmail.com"
password = "dbna bczr qsol egmv"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
list_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
for index, value_name in data[data.month == now.month]["name"].items():
    if (
        now.day == data[data.name == value_name]["day"].item()
        and now.month == data[data.name == value_name]["month"].item()
    ):
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = rdm.choice(list_letter)
        # Cara yang efisien
        with open(f"./letter_templates/{letter}") as file:
            letter_read = file.read()
            letter_read = letter_read.replace("[NAME]", value_name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data[data.name == value_name]["email"].item(),
                msg=f"Subject:Happy Birthday! \n\n{letter_read}",
            )

        # Bertele-tele
        # with open(f"./letter_templates/{letter}") as file:
        #     letter_read = file.read()
        #     with open(f"./letter_templates/{letter}", "w") as file:
        #         letter_write = file.write(letter_read.replace("[NAME]", value_name))

        # with open(f"./letter_templates/{letter}", "r") as file:
        #     letter_send = file.read()
        # # 4. Send the letter generated in step 3 to that person's email address.
        #     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #         connection.starttls()
        #         connection.login(user=my_email, password=password)
        #         connection.sendmail(
        #             from_addr=my_email,
        #             to_addrs=data[data.name == value_name]["email"].item(),
        #             msg=f"Subject:Happy Birthday! \n\n{letter_send}",
        #         )

        #     with open(f"./letter_templates/{letter}", "w") as file:
        #         letter_write = file.write(letter_send.replace(value_name, "[NAME]"))

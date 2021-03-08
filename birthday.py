import random
import datetime as dt
import smtplib
import pandas


# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)

data = pandas.read_csv("birthdays.csv")


b_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

is_it_birthday = today in b_dict

person = b_dict[today]["name"]

if is_it_birthday:
    rn = random.randint(1, 3)
    with open(f"./letter_templates/letter_{rn}.txt") as letter:
        letter_data = letter.read()
        letter_data = letter_data.replace("[NAME]", person)

    with smtplib.SMTP("smtp.mail..com") as connection:
        connection.starttls()
        connection.login("", "")
        connection.sendmail(
            from_addr="",
            to_addrs="",
            msg=f"Subject:Happy Birthday\n\n{letter_data}"
        )

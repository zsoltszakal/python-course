# import smtplib
#
# my_email = "emaila"
# password = "password"
#
# with smtplib.SMTP("smtp") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="m",
#         msg="Subject:\n\nHello:)"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(now)
#
# date_of_birth = dt.datetime(year=1988 , month=4 , day=1)
# print(date_of_birth)

import random
import datetime as dt
import smtplib

EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes:
        q_list =  quotes.readlines()

    random_quote = random.choice(q_list)

    with smtplib.SMTP("smtp") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="",
            msg=f"Subject:\n\n{random_quote}"
        )

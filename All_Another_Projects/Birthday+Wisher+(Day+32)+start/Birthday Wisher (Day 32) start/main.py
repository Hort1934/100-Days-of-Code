# import smtplib
#
# my_email = "hort19345@gmail.com"
# password = "cdawadrjvfskvbht"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ihormarchenko@yahoo.com",
#                         msg="Subject:Hello\n\nThis s the body of my email/")
import random
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(now.weekday())
#
# date_of_birth = dt.datetime(year=2002, month=6, day=4, hour=18, minute=30, second=30)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
week = now.weekday()
if week == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
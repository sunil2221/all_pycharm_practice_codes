import smtplib
import datetime as dt
import random
my_email = "dummy@gmail.com"
password = "abcd1234"

day = dt.datetime.now()
weekday = day.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("dummy.@gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n")
        connection.close()



# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="dummy2@gmail.com", msg="Hello")
# connection.close()


# now = dt.datetime.now()
# year = now.year
# month = now.month
# date_of_birth = dt.datetime(year=2002, month=1, day=21)
# print(date_of_birth)
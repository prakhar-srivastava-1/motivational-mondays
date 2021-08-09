import smtplib
from quotes import quotes
from subscribers import subscribers
from random import choice
from secrets import email, password
import datetime as dt

# TODO 1: Read the quotes file and select a quote
quote = choice(quotes)
email_quote = f"Subject: Motivational Monday\n\n{quote['quote']}\n- {quote['author']}"

# TODO 2: Run the code only if its a Monday
# datetime.now().weekday() = 0 => Monday
if dt.datetime.now().weekday() == 0:
    # TODO 3: create SMTP connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        # TODO 4: send mail to all subscribers
        for subscriber in subscribers:
            connection.sendmail(from_addr=email,
                                to_addrs=subscriber,
                                msg=email_quote)
            print(f"Mail sent to: {subscriber}")

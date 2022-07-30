# Auto-Email-Teachers-Staff
# by Ma2terB1ast3r
# [WIP CODE]

from exchangelib import Credentials, Account, Configuration, Message, Mailbox # MS Exchange Login
import maskpass  # Password Hiding
import csv # CSV library


# Setting User Info
ExchangeServer = input("Exchange Mail Server: ")
ExchangeEmail = input("Exchange Email: ")
ExchangeUser = input("Exchange Username: ")
ExchangePassword = maskpass.askpass(prompt="Exchange Password: ", mask="#")

# Loginging into exchange
credentials = Credentials(username=str(ExchangeUser), password=str(ExchangePassword))
config = Configuration(server=str(ExchangeServer), credentials=credentials)
UserAccount = Account(primary_smtp_address=ExchangeEmail, credentials=credentials, config=config)

# Reading CSV
# To be replaced with web page scraping
results = []

with open('TestTable.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        results.append(row)

R1 = results[0]
R2 = results[1]
R3 = results[2]

# Emails list of people
# CSV Row 1 = repecient email
# CSV Row 2 = email subject
# CSV Row 3 = email body
for x in R1:
    m = Message(
    account=UserAccount,
    subject=str(R2[R1.index(x)]),
    body=str(R3[R1.index(x)]),
    to_recipients=[
        Mailbox(email_address=str(R1[R1.index(x)])),
    ],
    )
    m.send()
    print("Emailed " + str(R1[R1.index(x)]) + " " + str(R2[R1.index(x)]) + " " + str(R3[R1.index(x)]))
    # Sends the same R2 and R3 if the email occurs multiple times


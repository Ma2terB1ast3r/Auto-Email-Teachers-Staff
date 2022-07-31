## TH
## WIP CODE

import dearpygui.dearpygui as dpg # GUI
from exchangelib import Credentials, Account, Configuration, Message, Mailbox # MS Exchange Login
import maskpass  # Password Hiding
import csv # Temp for reading CSV


# Setting User Info
ExchangeServer = ""
ExchangeEmail = ""
ExchangeUsername = ""
ExchangePassword = ""

# Setting Email Info
EmailSubject = "Missed class: "
EmailBody = ''' 
Hi <recipent>,

I am going to miss <subject> today as I am sick.
Can you please send any work from <subject> that I need to catch up on.

Thanks,
<sender>            
'''
recipent = "Mr A"
subject = "6FAIL9C"
sender = "Myself"


dpg.create_context()

# UI Events
def button_cb(sender, app_data):
    print(ExchangeServer, ExchangeEmail, ExchangeUsername, ("*" * len(ExchangePassword)))

def ti_server_cb(sender, app_data):
    global ExchangeServer
    ExchangeServer = dpg.get_value("ti_server")
    print("Server set to: " + ExchangeServer)

def ti_email_cb(sender, app_data):
    global ExchangeEmail
    ExchangeEmail = dpg.get_value("ti_email")
    print("Email set to: " + ExchangeEmail)

def ti_username_cb(sender, app_data):
    global ExchangeUsername
    ExchangeUsername = dpg.get_value("ti_username")
    print("Username set to: " + ExchangeUsername)

def ti_password_cb(sender, app_data):
    global ExchangePassword
    ExchangePassword = dpg.get_value("ti_password")
    print("Password set to: " + ("*" * len(ExchangePassword)))

def ti_subject_cb(sender, app_data):
    global EmailSubject
    EmailSubject = dpg.get_value("ti_subject")
    print("Email Subject set to: " + EmailSubject)

def ti_body_cb(sender, app_data):
    global EmailBody
    EmailBody = dpg.get_value("ti_body")
    print("Email Body set to: " + EmailBody)

def send_emails(sender, app_data):
    # Loginging into exchange
    credentials = Credentials(username=str(ExchangeUsername), password=str(ExchangePassword))
    config = Configuration(server=str(ExchangeServer), credentials=credentials)
    UserAccount = Account(primary_smtp_address=ExchangeEmail, credentials=credentials, config=config)

    # Reading CSV
    # To be replaced with web page scraping
    results = []

    with open('TestTable.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader: # each row is a list
            results.append(row)

    R1 = results[0]
    R2 = results[1]
    R3 = results[2]

    # Emails list of peoplea
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


def print_me(sender):
    print(f"Menu Item: {sender}")

# Main Window
with dpg.window(tag="Primary Window"):
    # Top Menu
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
                dpg.add_menu_item(label="Setting 2", callback=print_me)

        dpg.add_menu_item(label="Help", callback=print_me)

        with dpg.menu(label="Widget Items"):
            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)
            dpg.add_color_picker(label="Color Me", callback=print_me)

    # First Part
    dpg.add_text("Hello, world")
    button1 = dpg.add_button(label="Press Me!", callback=button_cb)
    dpg.add_text("Exchange mail server:")
    dpg.add_input_text(tag="ti_server", label="",callback=ti_server_cb)
    dpg.add_text("Exchange email:")
    dpg.add_input_text(tag="ti_email", label="",callback=ti_email_cb)
    dpg.add_text("Exchange username:")
    dpg.add_input_text(tag="ti_username", label="",callback=ti_username_cb)
    dpg.add_text("Exchange password:")
    dpg.add_input_text(tag="ti_password", label="", password=True, callback=ti_password_cb)
    dpg.add_text("Message Subject:")
    dpg.add_input_text(tag="ti_subject", label="", default_value="", callback=ti_subject_cb)
    dpg.add_text("Message Body:")
    dpg.add_input_text(tag="ti_body", label="", default_value="", multiline=True, height=200, callback=ti_body_cb)



dpg.create_viewport(title='Auto Email Teachers', width=500, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()




#newemailbody = emailbody
#newemailbody = newemailbody.replace("<recipent>", recipent)
#newemailbody = newemailbody.replace("<subject>", subject)
#newemailbody = newemailbody.replace("<sender>", sender)

#print(newemailbody)
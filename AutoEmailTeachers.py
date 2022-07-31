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
EmailSubject = "Missed class: <class>"
EmailBody = ''' 
Hi <recipient>,

I am going to miss <class> today as I am sick.
Can you please send any work from <class> that I need to catch up on.

Thanks,
<sender>            
'''
recipient = "Mr A"
subject = "6FAIL9C"
EmailSender = "Myself"

results = []

with open('TestTable.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader: # each row is a list
        results.append(row)

# Reading CSV
# To be replaced with web page scraping
RecipientEmail = results[0]
RecipientTitle = results[1]
RecipientName = results[2]
RecipientClass = results[3]


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

    # Emails list of people
    # CSV Row 1 = recipient class
    # CSV Row 2 = recipient class
    # CSV Row 3 = recipient class
    # CSV Row 4 = recipient class
    for x in range(len(RecipientEmail)):
        global EmailSubject
        EmailSubjectUnique = EmailSubject
        EmailSubjectUnique = EmailSubjectUnique.replace("<recipient>", RecipientTitle[x] + " " + RecipientName[x])
        EmailSubjectUnique = EmailSubjectUnique.replace("<class>", RecipientClass[x])
        EmailSubjectUnique = EmailSubjectUnique.replace("<sender>", str(EmailSender))
        global EmailBody
        EmailBodyUnique = EmailBody
        EmailBodyUnique = EmailBodyUnique.replace("<recipient>", RecipientTitle[x] + " " + RecipientName[x])
        EmailBodyUnique = EmailBodyUnique.replace("<class>", RecipientClass[x])
        EmailBodyUnique = EmailBodyUnique.replace("<sender>", str(EmailSender))
        m = Message(
        account=UserAccount,
        subject=str(EmailSubjectUnique),
        body=str(EmailBodyUnique),
        to_recipients=[
            Mailbox(email_address=str(RecipientEmail[x])),
        ],
        )
        m.send()
        print("Emailed " + str(RecipientEmail[x]) + " " + str(RecipientTitle[x]) + " " + str(RecipientName[x]) + " " + str(RecipientClass[x]))
        # Sends the same RecipientTitle and RecipientName if the email occurs multiple times


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

    # Table
    with dpg.table(header_row=False, borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True, policy=dpg.mvTable_SizingFixedFit, resizable=True, no_host_extendX=True):
        dpg.add_table_column(label="Recipient Email")
        dpg.add_table_column(label="Recipient Title")
        dpg.add_table_column(label="Recipient Name")
        dpg.add_table_column(label="Recipient Class")

        for i in range(len(RecipientEmail)):
                with dpg.table_row():
                    for j in range(4):
                        if j == 0:
                            dpg.add_text(RecipientTitle[i])
                        elif j == 1:
                            dpg.add_text(RecipientName[i])
                        elif j == 2:
                            dpg.add_text(RecipientClass[i])
                        elif j == 3:
                            dpg.add_text(RecipientEmail[i])
                        else:
                            continue

    # First Part
    dpg.add_text("Hello, world")
    button1 = dpg.add_button(label="Press Me!", callback=send_emails)

    # Message Contents
    with dpg.tree_node(label="Message Contents", default_open=True):
        dpg.add_text("Subject:")
        dpg.add_input_text(tag="ti_subject", label="", default_value=EmailSubject, callback=ti_subject_cb)
        dpg.add_text("Body:")
        dpg.add_input_text(tag="ti_body", label="", default_value=EmailBody, multiline=True, height=200, width=500, tab_input=True,callback=ti_body_cb)

    # Exchange Settings
    with dpg.tree_node(label="Exchange Settings", default_open=True):
        dpg.add_text("Exchange mail server:")
        dpg.add_input_text(tag="ti_server", label="", default_value=ExchangeServer, hint="mail.<domain>", no_spaces=True, callback=ti_server_cb)
        dpg.add_text("Exchange email:")
        dpg.add_input_text(tag="ti_email", label="", default_value=ExchangeEmail, hint="<name>@<domain>.com", no_spaces=True, callback=ti_email_cb)
        dpg.add_text("Exchange username:")
        dpg.add_input_text(tag="ti_username", label="", default_value=ExchangeUsername, hint="Username", no_spaces=True, callback=ti_username_cb)
        dpg.add_text("Exchange password:")
        dpg.add_input_text(tag="ti_password", label="", default_value=ExchangePassword, hint="Password", no_spaces=True, password=True, callback=ti_password_cb)


# DearPyGUI Create Window
dpg.create_viewport(title='Auto Email Teachers', width=1000, height=1200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()




#EmailBodyUnique = EmailBody
#EmailBodyUnique = EmailBodyUnique.replace("<recipient>", recipient)
#EmailBodyUnique = EmailBodyUnique.replace("<class>", subject)
#EmailBodyUnique = EmailBodyUnique.replace("<sender>", sender)

#print(EmailBodyUnique)
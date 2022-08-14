## TH
## WIP CODE

import dearpygui.dearpygui as dpg # GUI
from exchangelib import Credentials, Account, Configuration, Message, Mailbox # MS Exchange Login
import maskpass  # Password Hiding
import csv # Temp for reading CSV
from os.path import exists


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

# Recipient Info
RecipientEmail = []
RecipientTitle = []
RecipientName = []
RecipientClass = []

# CSV File Read/Write
def read_recipients():
    if exists("TestTable.csv"):
        try:
            results = []
            global RecipientEmail
            global RecipientTitle
            global RecipientName
            global RecipientClass
            with open('TestTable.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader: # each row is a list
                    results.append(row)
            try:
                RecipientEmail = results[0]
                RecipientTitle = results[1]
                RecipientName = results[2]
                RecipientClass = results[3]
            except IndexError:
                pass
        except FileNotFoundError:
            print("error: file doesnt exist")
            pass
    else:
        print("file doesnt exist")

def read_details():
    if exists("Details.csv"):
        try:
            with open('Details.csv', 'r') as file:
                details = []
                reader = csv.reader(file)
                global ExchangeServer
                global ExchangeEmail
                global ExchangeUsername
                for row in reader: # each row is a list
                    details.append(row)
                try:
                    ExchangeServer = str(details[0])
                    ExchangeEmail = str(details[1])
                    ExchangeUsername = str(details[2])
                    ExchangeServer = ExchangeServer.replace("[", "")
                    ExchangeServer = ExchangeServer.replace("'", "")
                    ExchangeServer = ExchangeServer.replace("]", "")
                    ExchangeEmail = ExchangeEmail.replace("[", "")
                    ExchangeEmail = ExchangeEmail.replace("'", "")
                    ExchangeEmail = ExchangeEmail.replace("]", "")
                    ExchangeUsername = ExchangeUsername.replace("[", "")
                    ExchangeUsername = ExchangeUsername.replace("'", "")
                    ExchangeUsername = ExchangeUsername.replace("]", "")
                except IndexError:
                    pass
                return details
        except FileNotFoundError:
            print("error: file doesnt exist")
            pass
    else:
        print("file doesnt exist")

def save_details():
    with open('Details.csv', 'w+') as file:
        global ExchangeServer
        global ExchangeEmail
        global ExchangeUsername
        details = []
        details.append(ExchangeServer)
        details.append(ExchangeEmail)
        details.append(ExchangeUsername)
        reader = csv.writer(file)
        reader.writerow([details[0]])
        reader.writerow([details[1]])
        reader.writerow([details[2]])


read_recipients()
read_details()
dpg.create_context()

# UI Events
def btn_readdetails():
    global ExchangeServer
    global ExchangeEmail
    global ExchangeUsername
    read_details()
    dpg.set_value("ti_server", ExchangeServer)
    dpg.set_value("ti_email", ExchangeEmail)
    dpg.set_value("ti_username", ExchangeUsername)
    print(ExchangeServer, ExchangeEmail, ExchangeUsername)

def btn_savedetails():
    save_details()
    print(ExchangeServer, ExchangeEmail, ExchangeUsername)

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

    # Message Contents
    with dpg.tree_node(label="Message Contents", default_open=True):
        button1 = dpg.add_button(tag="btn_sendemail", label="Send Emails", callback=send_emails)
        dpg.add_text("Subject:")
        dpg.add_input_text(tag="ti_subject", label="", default_value=EmailSubject, callback=ti_subject_cb)
        dpg.add_text("Body:")
        dpg.add_input_text(tag="ti_body", label="", default_value=EmailBody, multiline=True, height=200, width=500, tab_input=True,callback=ti_body_cb)
    
    # Table
    with dpg.tree_node(label="Recipients", default_open=True):
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
        dpg.add_button(tag="btn_save", label="Save Details", callback=btn_savedetails)
        dpg.add_button(tag="btn_load", label="Load Details", callback=btn_readdetails)


# DearPyGUI Create Window
dpg.create_viewport(title='Auto Email Teachers', width=600, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


import dearpygui.dearpygui as dpg

dpg.create_context()

def button_callback(sender, app_data):
    print("button pressed")

def ti_server_callback(sender, app_data):
    print("server set")

def ti_email_callback(sender, app_data):
    print("email set")

def ti_username_callback(sender, app_data):
    print("username set")

def ti_password_callback(sender, app_data):
    print("password set")


def print_me(sender):
    print(f"Menu Item: {sender}")

with dpg.window(tag="Primary Window"):
    # Menu
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
    button1 = dpg.add_button(label="Press Me!", callback=button_callback)
    dpg.add_text("Exchange mail server:")
    dpg.add_input_text(label="", default_value="", callback=ti_server_callback)
    dpg.add_text("Exchange email:")
    dpg.add_input_text(label="", default_value="", callback=ti_email_callback)
    dpg.add_text("Exchange username:")
    dpg.add_input_text(label="", default_value="", callback=ti_username_callback)
    dpg.add_text("Exchange password:")
    dpg.add_input_text(label="", default_value="", password = True, callback=ti_password_callback)



dpg.create_viewport(title='Auto Email Teachers', width=500, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
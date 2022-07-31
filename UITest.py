import dearpygui.dearpygui as dpg

dpg.create_context()

def button_callback(sender, app_data):
    print("button pressed")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    button1 = dpg.add_button(label="Press Me!", callback=button_callback)

dpg.create_viewport(title='Auto Email Teachers', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
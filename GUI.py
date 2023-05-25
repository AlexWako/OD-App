from ShopifyApp import *
from APIScript import *
from Layout import *
import tkinter as tk

activate_session()

window = psg.Window('OD App', get_start_layout())

while True:

    event, values = window.read()

    if event == psg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Fulfill Order":
        window.close()
        window = psg.Window("Fulfill Orders", get_fulfill_layout())
        while True:
            event, values = window.read()
            if event == psg.WINDOW_CLOSED:
                window.close()
            if event == "Go Back":
                break
            if event == "Submit":
                file_path = values["-FILE-"]
                # Creates a new window with the output of the script
                if file_path:
                    # Runs the script first
                    output = update_fulfillment(file_path, headers = headers)
                    window.close()
                    window = psg.Window("Required Fulfillments", get_fulfill_output_layout(output))
                    event, values = window.read()
                    if event == psg.WINDOW_CLOSED or event == "Exit":
                        window.close()
                    if event == "Go Back":
                        window.close()
                        window = psg.Window("Complete DHL Fulfillment", get_fulfill_layout())
                        continue
        window.close()
        window = psg.Window('OD App', get_start_layout())

    # Edit Measurement Window
    if event == "Edit Measurement":
        window.close()
        window = psg.Window('Input Window', get_edit_measurement_layout())
        while True:
            event, values = window.read()
            if event == psg.WINDOW_CLOSED:
                window.close()
            if event == "Go Back":
                break
            if event == "Submit":
                product_name = values['-INPUT-']
                product_id = get_product(product_name, headers = headers)[0]
                html_code = get_product(product_name, headers = headers)[1]
                if html_code:
                    cm_data = get_og_cm_data(html_code)
                    window.close()
                    window = psg.Window('Input Table', get_input_table_layout(cm_data))
                    event, values = window.read()
                    if event == psg.WINDOW_CLOSED:
                        window.close()
                    if event == "Go Back":
                        window.close()
                        window = psg.Window('Input Window', get_edit_measurement_layout())
                        continue
                    if event == "Submit":
                        root = tk.Tk()
                        root.withdraw()
                        clipboard_data = root.clipboard_get()
                        table_data = clipboard_data.split("\n")
                        for i, row in enumerate(table_data):
                            table_data[i] = row.split("\t")
                        status = update_measure_table(product_id, edit_table(html_code, table_data), headers)
                        if status == "Complete":
                            window.close()
                            window = psg.Window('', get_measurement_output_layout())
                            event, values = window.read()
                            if event == psg.WINDOW_CLOSED or event == "Exit":
                                window.close()
        window.close()
        window = psg.Window('OD App', get_start_layout())

close_session()


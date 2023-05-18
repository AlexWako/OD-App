import PySimpleGUI as psg
import ShopifyApp as sa
from Layout import *


window = psg.Window("Fulfill Orders", get_fulfill_layout())
while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    elif event == "Submit":
        file_path = values["-FILE-"]
        # Creates a new window with the output of the script
        if file_path:
            # Runs the script first
            output = sa.fulfill(file_path)
            # Temporary solution
            window.close()
            window = psg.Window("Required Fulfillments", get_output_layout(output))
            event, values = window.read()
            if event == psg.WINDOW_CLOSED or event == "Exit":
                break
            elif event == "Go Back":
                window.close()
                window = psg.Window("Complete DHL Fulfillment", get_fulfill_layout())
                continue
window.close()





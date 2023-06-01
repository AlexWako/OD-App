import PySimpleGUI as psg

# Login Screen
def get_login_layout():

    layout = [
        [psg.Text("API Token:"), psg.InputText()],
        [psg.Button("Submit")]
    ]

    return layout

# Start Screen
def get_start_layout():

    button_layout = [
        [psg.Button('Fulfill Order')],
        [psg.Button('Edit Measurement')],
        [psg.Button('Exit')]
    ]

    layout = [
        [psg.Column(button_layout)]
    ]

    return layout

# Layout when user presses send email
def get_email_layout():
    email_template = [
        [psg.Text('Select an option:')],
        [psg.Combo(['Option 1', 'Option 2', 'Option 3'], default_value = 'Option 1', key = '-COMBO-', size = (20, 1))],
        [psg.Button('Submit')]
    ]
    return email_template

def get_fulfill_layout():
    layout = [
        [psg.Text('Select a CSV file:')],
        [psg.Input(key = '-FILE-', enable_events = True), psg.FileBrowse()],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_fulfill_output_layout(output):
    layout = [
                [psg.Text(output)],
                [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

def get_edit_measurement_layout():
    layout = [
        [psg.Text('Enter product name:')],
        [psg.Input(key='-INPUT-')],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_input_table_layout(data):
    rows = len(data[1])
    input_layout = [[psg.Multiline(size=(25, 10), key='-DATA-')]]
    og_data_layout = [
        [psg.Table(values = data[1], headings = data[0], num_rows = rows, key = '-OUTPUT TABLE-')]
    ]
    button_layout = [
        [psg.Button("Submit")],
        [psg.Button("Go Back")]
    ]
    layout = [
        [psg.Frame('Original Table', og_data_layout), psg.VSeperator(), psg.Column(input_layout), psg.Column(button_layout)]
    ]

    return layout


def get_measurement_output_layout():
    layout = [
        [psg.Text("Complete", justification = 'center')],
        [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout



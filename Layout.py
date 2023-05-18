import PySimpleGUI as psg

# Start Screen
def get_start_layout():
    layout = [
        [psg.Button('Send Email')],
        [psg.Button('Fulfill Order')],
        [psg.Button('Exit')]
    ]
    return layout

# Layout when user presses send email
def get_email_layout():
    email_template = [
        [psg.Text('Select an option:')],
        [psg.Combo(['Option 1', 'Option 2', 'Option 3'], default_value='Option 1', key='-COMBO-', size=(20, 1))],
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

def get_output_layout(output):
    layout = [
                [psg.Text(output)],
                [psg.Button("Go Back", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout


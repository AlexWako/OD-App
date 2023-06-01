def remove_space(string):
    string = string.replace(' ','')
    return string

# Not used
def list_to_html(data):
    html_code = "<table width='100%'>\n"
    for row in data:
        html_code += "<tr>\n"
        for cell in row:
            html_code += f"<td>{cell}</td>\n"
        html_code += "</tr>\n"
    html_code += "</table>"
    return html_code

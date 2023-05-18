from jinja2 import Template

def exchange_render(last_name, track_num):

    with open('template/ExchangeTemplate.html', 'r') as file:
        ET_Template = file.read()

    template = Template(ET_Template)

    body = template.render(last_name = last_name.capitalize(), track_num = track_num)

    return body

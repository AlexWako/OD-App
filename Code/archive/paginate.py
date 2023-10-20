import re

def get_next_page(response):
    matches = re.findall(r'<([^>]+)>; rel="([^"]+)"', response)
    for match in matches:
        if 'next' in match:
            return match[0]
        else:
            continue
    return None
import re

def agregar_host(html_string, host):
    patron = r'src="/media/([^"]*)"'
    nuevo_html = re.sub(patron, r'src="{}/media/\1"'.format(host), html_string)
    return nuevo_html
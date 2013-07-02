# -*- coding: utf-8 -*-
import urllib
import lxml.html
import base64
import re

def get_wallpaper_src():
    page_url = "http://wallbase.cc/random/213/eqeq/1920x1080/0/100/20";

    page = urllib.urlopen(page_url)
    page_html = lxml.html.document_fromstring(page.read())

    first_elem = page_html.cssselect('#thumbs .thdraggable')[0]
    wall_url = str(first_elem.get('href'))
    wall_page = urllib.urlopen(wall_url)

    wall_page_html = lxml.html.document_fromstring(wall_page.read())
    wall_elem = wall_page_html.cssselect("#bigwall script")[0]

    r = re.compile('\w+=?')
    
    src_b64 = r.findall(wall_elem.text)[-1]
    wall_src =  base64.b64decode(src_b64)
    
    return wall_src
    

    
    

if __name__ == "__main__":
    get_wallpaper()

# -*- coding: utf-8 -*-

import urllib
import lxml.html
import base64
import re
import os
import sys

import conf


def get_wallpaper_src():
    page_url = "http://wallbase.cc/random/213/eqeq/"+conf.RESOLUTION+"/0/100/20";
    
    page = urllib.urlopen(page_url)
    page_html = lxml.html.document_fromstring(page.read())

    try:
        first_elem = page_html.cssselect('#thumbs .thdraggable')[0]
    except IndexError:
        print "Not found anything"
        sys.exit(1)
    
    wall_url = str(first_elem.get('href'))
    wall_page = urllib.urlopen(wall_url)
    
    wall_page_html = lxml.html.document_fromstring(wall_page.read())
    wall_elem = wall_page_html.cssselect("#bigwall script")[0]
    r = re.compile('\w+=?')
    
    src_b64 = r.findall(wall_elem.text)[-1]
    wall_src =  base64.b64decode(src_b64)
    return wall_src

def download_wallpaper(wall_src):
    wall_name = wall_src.split('/')[-1]
    full_path = os.path.join(conf.PATH, wall_name)
    print "downloading..."
    try:
        urllib.urlretrieve(wall_src, full_path)
    except:
        print "download error"
    else:
        print "download success"


def setup_wallpaper(path): ### Gnome only. For other system comming soon :)
    if conf.DS == 'Gnome':
        os.system('gsettings set org.gnome.desktop.background picture-uri file://'+path)
    return 0

if __name__ == "__main__":
    wall_src = get_wallpaper_src()
    path = download_wallpaper(wall_src)
    setup_wallpaper(path)

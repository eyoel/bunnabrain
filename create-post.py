#!/usr/bin/python
import calendar
import datetime
import os
from subprocess import call


#--- FUTURE todo:
#   3. add this to bash commands so it can be an easy executable
post_template = '''
---
layout: single
title:  "%s"
date:   %s
author: eyoela
categories: %s
excerpt: "%s"
header:
  overlay_image: /assets/images/some-image.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5
  caption: "<A caption - how cool>"
---

# Title
Some text here ...

![Some image caption]({{site.baseurl}}/assets/images/image.jpg)

<blockquote>
Here is a quote ..
</blockquote>
_something in italics_
** or in BOLD! **

need
any empty line if you want it to be

on the next line
'''

def run():
    title = raw_input("Enter the title of the post: \n >")
    category_name = raw_input("Enter category [tech-brew, travel, slow-drip]: >")
    excerpt = raw_input("Enter excerpt: >")
    # post_date_str = raw_input("Enter post date Eg. DD-MM-YYYY: \n >")
    post_date_str = "01-01-2019"
    post_date = datetime.datetime.strptime(post_date_str, "%d-%m-%y").today()

    if not title or not category_name:
        print("Error while trying to create post. One of the inputs is empty or not valid")
        return
    create_post_file(title, post_date, category, excerpt)
    call(["testWebpage", "no args needed"])  # start up the test server


def create_post_file(title,post_date,category,excerpt):
    title = title.lower()
    title = title.replace(' ', '-')
    filename = "_posts/"+date_string(post_date)+title+".markdown"
    # TODO: put the variables in there
    post_text = template_string.format()
    try:
        if not os.path.isfile(filename):
            with open(filename, 'a+') as newpost_file:
                newpost_file.write(post_text)
        else:
            print('File already exists -  ' + filename)
    except Exception as e:
        print('Exception trying to write to the file:' + filename+ ' exception: ',e)


def date_time_string(date):
    return date.strftime("%d-%m-%y ")

def date_string(date):
    return date.strftime("%d-%m-%y")



run()

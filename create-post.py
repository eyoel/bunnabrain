#!/usr/bin/env python3
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

# %s
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
    title = input("Enter the title of the post: \n >")
    category_name = input("Enter category [tech-brew, travel, slow-drip]: >")
    excerpt = input("Enter excerpt: >")
    post_date = datetime.datetime.now()

    if not title or not category_name:
        print("Error while trying to create post. One of the inputs is empty or not valid")
        return
    create_post_file(title, post_date, category_name, excerpt)
    # The following command is commented out as it may not exist on all systems.
    # call(["testWebpage", "no args needed"])  # start up the test server


def create_post_file(title, post_date, category, excerpt):
    filename_title = title.lower().replace(' ', '-')
    filename = f"_posts/{post_date.strftime('%Y-%m-%d')}-{filename_title}.markdown"
    
    post_text = post_template % (title, post_date.strftime('%Y-%m-%d %H:%M:%S %z'), category, excerpt, title)
    try:
        if not os.path.isfile(filename):
            with open(filename, 'w') as newpost_file:
                newpost_file.write(post_text)
            print(f"New post created: {filename}")
        else:
            print(f"File already exists - {filename}")
    except Exception as e:
        print(f"Exception trying to write to the file: {filename} exception: {e}")


if __name__ == "__main__":
    run()
from makebloglistpage import make_bloglist_page
from generatemostrecentblog import generate_recent_blog
from makeblogpage import make_blog_page
from generateaboutpage import generate_aboutpage
from generateindexpage import generate_indexpage

import os

files = os.listdir("resources/blogsmd")

if len(files) == 0:
    print("There are no blogs.")

for file in files:
    make_blog_page(file)

make_bloglist_page()
generate_recent_blog()

generate_indexpage()
generate_aboutpage()
from os import listdir
from os import path as pathf
from datetime import datetime
from datetime import *
import time

link_template = "<div class=\"bloglinks\"><a href=\"LINK\">NAME DATE</a><br></div>"

template_start = "<div class=\"bloglinks\">\n<table>"

link_temp = "<tr><td class=\"tdname\"><a class=\"name\" href=\"LINK\">NAME</d></td><td class=\"date\">DATE</td></tr>"

template_end = "</table>\n</div>"

def get_date_created(e):
    return pathf.getctime("resources/blogs/" + e)

def make_bloglist_page():
    file_names = [f for f in listdir("resources/blogs") if pathf.isfile(pathf.join("resources/blogs", f))]
    file_names.sort(reverse=True, key=get_date_created)
    paths = ["resources/blogs/" + p for p in file_names]

    links = []

    utc_offset_abbreviation = "UTC" + str(time.timezone /60 /60 * -1).split(".")[0]

    for idx, pathname in enumerate(paths):
        # link = link_template.replace("LINK", pathname).replace("NAME", file_names[idx].split(".")[0].capitalize().replace("_", " ")).replace("DATE", " | Date posted: " + str(datetime.fromtimestamp(pathf.getctime(pathname)).strftime('%m/%d/%Y at %H:%M:%S')))
        link = link_temp.replace("LINK", pathname).replace("NAME", file_names[idx].split(".")[0].capitalize().replace("_", " ")).replace("DATE", str(datetime.fromtimestamp(pathf.getctime(pathname)).strftime('%b %d, %Y %I:%M%p').lstrip(" ").replace(" 0", " ")))
        links.append(link)

    # print(links)
    links_str = " ".join(links)
    if (len(file_names)) == 0:
        links_str = "<p style=\"text-align: center;\">There are currently no blogs.</p><hr>"
    else:
        links_str = template_start + links_str + template_end

    bloglist = open("includes/templatebloglist.html", "r").readlines()
    for idx, line in enumerate(bloglist):
        if line.find("HEADER") != -1:
            bloglist[idx] = line.replace("HEADER", open("includes/headerbloglist.html").read())
            continue
        if line.find("CONTENT") != -1:
            bloglist[idx] = line.replace("CONTENT", links_str)
            continue
        if line.find("FOOTER") != -1:
            bloglist[idx] = line.replace("FOOTER", open("includes/footer.html").read())
            continue

    output = open("bloglist.html", "w")
    output.writelines(bloglist)

# make_bloglist_page()
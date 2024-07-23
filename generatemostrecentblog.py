import os
import marko
from makebloglistpage import get_date_created
from datetime import datetime
from os import path as pathf

def generate_recent_blog():
    file_names = [f for f in os.listdir("resources/blogs") if os.path.isfile(os.path.join("resources/blogs", f))]
    file_names.sort(reverse=True, key=get_date_created)

    if (len(file_names)) == 0:
        output = open("blog.html", "w")
        template = open("includes/templaterecentblog.html", "r").readlines()
        for idx, line in enumerate(template):
            if line.find("HEADER") != -1:
                template[idx] = line.replace("HEADER", open("includes/headerbloglist.html").read())
                continue
            if line.find("CONTENT") != -1:
                template[idx] = line.replace("CONTENT", "<div style=\"text-align: center;\" class=\"information\"><p style=\"text-align: center;\" class=\"titleinfo\">" + "No blogs to show :(" + "</p></div><hr>")
                continue
            if line.find("FOOTER") != -1:
                template[idx] = line.replace("FOOTER", open("includes/footer.html").read())
                continue

        output.writelines(template)
    else:
        newest_blog_md = open("resources/blogsmd/" + file_names[0].split(".")[0] + ".md").read()

        newest_blog = marko.convert(newest_blog_md)
        # print(newest_blog)
        # print(newest_blog.find("<img src=\""))
        source_start = newest_blog.find("<img src=\"")

        letters = []

        if (source_start != -1):
            while newest_blog[source_start] != "\"":
                letters.append(newest_blog[source_start])
                source_start = source_start + 1

        if (letters != []):
            src = src.join(letters)
            # print(src)
            addition = "resources/blogs/"
            newest_blog = newest_blog.replace(src, addition + src)

        output = open("blog.html", "w")
        template = open("includes/templaterecentblog.html", "r").readlines()
        for idx, line in enumerate(template):
            if line.find("HEADER") != -1:
                template[idx] = line.replace("HEADER", open("includes/headerbloglist.html").read())
                continue
            if line.find("CONTENT") != -1:
                if (len(newest_blog) == 0):
                    template[idx] = line.replace("CONTENT", "<div style=\"text-align: center;\" class=\"information\"><p style=\"text-align: center;\" class=\"titleinfo\">" + "No blogs to show :(" + "</p></div><hr>")
                else:
                    template[idx] = line.replace("CONTENT", "<div class=\"information\"><p class=\"titleinfo\">" + file_names[0].split(".")[0].capitalize().replace("_", " ") + "</p><p class=\"dateinfo\">" + str(datetime.fromtimestamp(pathf.getctime("resources/blogs/" + file_names[0])).strftime('%b %d, %Y at %I:%M%p').lstrip(" ").replace(" 0", " ")) + "</p></div><hr>" + newest_blog)
                continue
            if line.find("FOOTER") != -1:
                template[idx] = line.replace("FOOTER", open("includes/footer.html").read())
                continue

        output.writelines(template)
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

        paths_md = [pathf.join("resources/blogsmd/", f.split(".")[0] + ".md") for f in file_names]
        
        for idx, path in enumerate(paths_md):
            if (len(open(paths_md[idx]).read()) == 0):
                file_names[idx] = " "

        print(file_names)

        recent_file_idx = 0

        for idx, path in enumerate(file_names):
            print(file_names[idx])
            if (file_names[idx] == " "):
                continue
            else:
                newest_blog_md = open("resources/blogsmd/" + file_names[idx].split(".")[0] + ".md").read()
                recent_file_idx = idx
            #if (file_names[idx] != " "):
            #    print("yes")
            #    newest_blog_md = open("resources/blogsmd/" + file_names[0].split(".")[0] + ".md").read()
            #else:
            #    newest_blog_md = " "


        newest_blog = marko.convert(newest_blog_md)
        # print(newest_blog)
        # print(newest_blog.find("<img src=\""))
        source_start = newest_blog.find("<img src=\"")

        #print(source_start)
        #print(newest_blog)

        letters = []

        if (source_start != -1):
            source_start = source_start + len("<img src=\"")
            while newest_blog[source_start] != "\"":
                letters.append(newest_blog[source_start])
                source_start = source_start + 1

        if (len(letters) != 0):
            #print(letters)
            src = "".join(letters)
            # print(src)
            addition = "resources/blogs/"
            newest_blog = newest_blog.replace(src, addition + src)

        # print(addition + src)

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
                    template[idx] = line.replace("CONTENT", "<div class=\"information\"><p class=\"titleinfo\"><strong>" + file_names[recent_file_idx].split(".")[0].capitalize().replace("_", " ") + "</strong></p><p class=\"dateinfo\"><strong>" + str(datetime.fromtimestamp(pathf.getctime("resources/blogs/" + file_names[0])).strftime('%b %d, %Y at %I:%M%p').lstrip(" ").replace(" 0", " ")) + "</strong></p></div><hr>" + newest_blog)
                continue
            if line.find("FOOTER") != -1:
                template[idx] = line.replace("FOOTER", open("includes/footer.html").read())
                continue

        output.writelines(template)

generate_recent_blog()
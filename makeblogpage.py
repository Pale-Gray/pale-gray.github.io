from generatebloghtml import gen_html
from datetime import datetime
from os import path as pathf

def make_blog_page(filename):
    template = open("includes/templateblog.html", "r")

    gen_html(filename)

    print("using the generated html to make a full page...")

    file_io = "resources/blogs/" + filename.split(".")[0] + ".html"

    input_blog_text = open(file_io, "r").readlines()
    # print(input_blog_text)
    output = open(file_io, "w")

    for line in template.readlines():
        if line.find("TITLE") != -1:
            output.write("    <title>This is a title test</title>\n")
            continue
        if line.find("HEADER") != -1:
            output.write(open("includes/headerblog.html", "r").read())
            continue
        if line.find("INFORMATION") != -1:
            output.write("<div class=\"information\"><p class=\"titleinfo\">" + filename.split(".")[0].capitalize().replace("_", " ") + "</p><p class=\"dateinfo\">" + str(datetime.fromtimestamp(pathf.getctime(file_io)).strftime('%b %d, %Y at %I:%M%p').lstrip(" ").replace(" 0", " ")) + "</p></div>")
            continue
        if line.find("CONTENT") != -1:
            output.writelines(input_blog_text)
            continue
        if line.find("FOOTER") != -1:
            output.write(open("includes/footer.html", "r").read())
            continue
        output.write(line)
    
    print("made full page at " + file_io)

# make_blog_page("blog1.md")
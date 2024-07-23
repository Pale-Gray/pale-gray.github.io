import marko

def gen_html(file):
    file_input = "resources/blogsmd/" + file
    file_output = "resources/blogs/" + file.split(".")[0] + ".html"
    
    print("converting the markdown to an html file...")

    try:
        html = marko.convert(open(file_input, "r").read())
        writeto = open(file_output, "w")
        writeto.write(html)
        print("Converted " + file + " to html at " + file_output )
    except:
        print("Couldn't load file '" + file + "'")
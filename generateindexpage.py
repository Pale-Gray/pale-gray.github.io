import marko

def generate_indexpage():
    index_page = open("index.html", "w")

    template = open("includes/template.html", "r").readlines()

    header = open("includes/header.html", "r").read()
    footer = open("includes/footer.html", "r").read()

    for idx, line in enumerate(template):
        if line.find("TITLE") != -1:
            template[idx] = "<title>Home</title>"
        if line.find("HEADER") != -1:
            template[idx] = header
            continue
        if line.find("INFORMATION") != -1:
            template[idx] = marko.convert(open("resources/md/index.md").read())
            continue
        if line.find("FOOTER") != -1:
            template[idx] = footer
            continue

    index_page.writelines(template)
    index_page.close()
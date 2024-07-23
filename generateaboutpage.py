import marko

def generate_aboutpage():
    about_page = open("about.html", "w")

    template = open("includes/template.html", "r").readlines()

    header = open("includes/header.html", "r").read()
    footer = open("includes/footer.html", "r").read()

    for idx, line in enumerate(template):
        if line.find("TITLE") != -1:
            template[idx] = "<title>About</title>"
        if line.find("HEADER") != -1:
            template[idx] = header
            continue
        if line.find("INFORMATION") != -1:
            template[idx] = marko.convert(open("resources/md/about.md").read())
            continue
        if line.find("FOOTER") != -1:
            template[idx] = footer
            continue

    about_page.writelines(template)
    about_page.close()
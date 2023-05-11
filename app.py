import yaml

with open("config.yaml") as f:
    configdata = yaml.load(f.read())

args = {}

if configdata["sbshtmlcomment"]:
    args["sbscomment"] = "<!-- Generated with Static Button Site by CTCL 2023 -->"
else:
    args["sbscomment"] = ""

args["title"] = configdata["title"]    
args["footertext"] = configdata["footertext"]
    
with open("base.css") as f:
    args["styling"] = f.read()
    
buttons = ""
for i in configdata["buttons"]:
    plink = configdata["buttons"][i]["link"]
    ptext = configdata["buttons"][i]["text"]
    pbtfg = configdata["buttons"][i]["fgcolor"]
    pbtbg = configdata["buttons"][i]["bgcolor"]
    
    buttons += f"       <a href=\"{plink}\"><button style=\"background-color: {pbtbg}; color: {pbtfg}\">{ptext}</button></a>\n"
args["buttons"] = buttons    

        
document = """<!DOCTYPE html>
<html>
    <head lang="en">
        <!-- Windows meta tags -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!-- Main tags -->
        <meta charset="UTF-8">
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Include CSS here -->
        <style>
{styling}
        </style>
    </head>
    <body>
        {sbscomment}
        <h1 class="center">{title}</h1>
    <div class="btn-group-rlmenu">
{buttons}</div>
    <br>
    <h4 class="center">{footertext}
</html>
""".format(**args)


with open("output.html", "w") as f:
    f.write(document)

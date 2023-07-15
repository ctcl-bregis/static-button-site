# Static Button Site - CTCL 2023
# May 11, 2023 - July 15, 2023

__version__ = "0.2.0"

from csscompressor import compress
from yaml import load, dump
from datetime import datetime, timezone
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open("config.yaml") as f:
    # "Loader" is safe here as the data comes from a config file
    configdata = load(f.read(), Loader = Loader)

fmtdate = datetime.now(timezone.utc).strftime(configdata["strftime"])

args = {}

if configdata["sbshtmlcomment"]:
    args["sbscomment"] = f"<!-- Generated with Static Button Site {__version__} - {fmtdate} -->"
else:
    args["sbscomment"] = ""

args["title"] = configdata["title"]    
args["footertext"] = configdata["footertext"]
    
with open("base.css") as f:
    args["styling"] = compress(f.read())
    
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
    <h4 class="center">{footertext}</h4>
</html>
""".format(**args)


with open("output.html", "w") as f:
    f.write(document)

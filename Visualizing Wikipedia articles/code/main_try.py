import time

from Obsidian import *
from wikiWEB import *


KEYWORD = "Harvard Square"
origin = WIKI_WEB(KEYWORD)
if origin.ifPageExists():
    createObsidianOriginFile(KEYWORD, origin)
else:
    print("Please use a better keyword.")


externalLinks = origin.get_links()
firstLink = externalLinks[0]

while not "philosophy" in firstLink.lower():
    firstLinkObj = WIKI_WEB(firstLink)
    createObsidianChildFiles(firstLink, KEYWORD, firstLinkObj)
    firstLink = firstLinkObj.get_links()[0]

firstLinkObj = WIKI_WEB(firstLink)
createObsidianChildFiles(firstLink, KEYWORD, firstLinkObj)
firstLink = firstLinkObj.get_links()[0]
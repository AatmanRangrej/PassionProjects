import time

from Obsidian import *
from wikiWEB import *


KEYWORD = "Love"
origin = WIKI_WEB(KEYWORD)
if origin.ifPageExists():
    createObsidianOriginFile(KEYWORD, origin)
else:
    print("Please use a better keyword.")


subArticles = origin.get_links()
size = len(subArticles)
newSubArticles = []
print("Originally length: There are about ", size, " many page.")
for i in range(int(size)):
    newSubArticles.append(subArticles[i])

print("There are about ",len(newSubArticles), " many page to parse through. Be patient.")
time_req = (len(newSubArticles)*0.02)/60
print("Total Estimated time required for computation. ", time_req)

try:
    for childArticle in newSubArticles:
        child = WIKI_WEB(childArticle)
        if child.ifPageExists():
            createObsidianChildFiles(childArticle, KEYWORD, child)
        time.sleep(0.02)

        childLinks = child.get_links()

        for link in childLinks:
            if link in newSubArticles:
                grandChild = WIKI_WEB(childArticle)

    print("Task Completed successfully...")
    exit()
except:
    print("Error occurred. Task Terminated")
    exit()
from wikiWEB import WIKI_WEB
import os



def createObsidianOriginFile(KEYWORD, originObj):


    #test.printObsidianText()
    #test.printPageText()
    #test.print_links()
    # Directory
    directory = KEYWORD

    # Parent Directory path
    parent_dir = "C:/Users/kashm/Documents/wikiWEB"

    #path
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

    f = open(path+"/"+ KEYWORD+".MD", "w", encoding="utf-8")
    f.write(originObj.getObsidianText())
    f.close()



def createObsidianChildFiles(childArticle, origin, childArticleObj):
    # test.printObsidianText()
    # test.printPageText()
    # test.print_links()
    # Directory
    #directory = childArticle


    # Parent Directory path
    parent_dir = "C:/Users/kashm/Documents/wikiWEB/" + origin + "/"

    #path
    #path = os.path.join(parent_dir, directory)
    childArticle = childArticle.lstrip("\"")
    childArticle = childArticle.rstrip("\"")

    if not os.path.isfile(parent_dir + str(childArticle) + ".MD"):
        f = open(parent_dir + str(childArticle) + ".MD", "w", encoding="utf-8")
        f.write(childArticleObj.getObsidianText())
        f.close()







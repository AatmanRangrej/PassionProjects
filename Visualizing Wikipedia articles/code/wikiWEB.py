

class  WIKI_WEB:

            def __init__(self, keyword):
                wikiAPI = self.initiateWikiAPI()
                self._keywordPage = wikiAPI.page(keyword)
                self._title = keyword

            def ifPageExists(self):
                return self._keywordPage.exists()

            def printPageText(self):
                print(self._keywordPage.text)

            def initiateWikiAPI(self):
                import wikipediaapi
                wiki_wiki = wikipediaapi.Wikipedia(
                    language='en',
                    extract_format=wikipediaapi.ExtractFormat.WIKI
                )
                return wiki_wiki

            def get_links(self):
                self._pageLinks = []
                links = self._keywordPage.links
                i = 0
                for title in links.keys():
                    if ":" not in title and not None:
                        self._pageLinks.append(title)
                        i += 1
                if self._pageLinks != None:
                    return self._pageLinks
                else:
                    print("Page null")
            def print_links(self):
                self._pageLinks = []
                links = self._keywordPage.links
                i = 0
                for title in sorted(links.keys()):
                    if ":" not in title and not None:
                        self._pageLinks.append(title)
                        print("%d: %s" % (i, title))
                        i += 1

            # This function is to insert "[[" and "]]" around subString in long string (articles).
            # @main_text (mostly long strings), place (index) where the substring have be found
            def addChar(self, page, substring):
                if "(" in substring and ")" in substring:
                    bracketOpen = substring.find("(")  # remove any text after brackets, ie within brackets.
                    substring = substring[: bracketOpen]


                place = page.find(substring)
                text = page[:place] + "[[" + page[place:]
                place = place + 2 + len(substring)
                newText = text[:place] + "]]" + text[place:]
                return newText

            def convertToObsidianText(self):  #convert page text in Obsidian MarkDown format. Any hyperLink has to be enclosed withen Square brackets.
                linkList = self.get_links()
                self._pageText = self._keywordPage.text

                for link in linkList:
                    if link in self._pageText:
                        self._pageText = self.addChar(self._pageText, link)
                return "# " + self._title + "     "+ self._pageText


            def printObsidianText(self):
                print(self._pageText)

            def getObsidianText(self):
                return self.convertToObsidianText()


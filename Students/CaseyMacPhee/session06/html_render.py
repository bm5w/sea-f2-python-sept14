#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = 'html'
    indent = '\t'

    def __init__(self, content = None):
        if content is None:
            self.content_list = []
        else:
            self.content_list = [content]

    def render(self, file_out, ind = ""):
        """render the content to file object"""

        file_out.write(self.indent + ind + "<" + self.tag + ">\n" + self.indent + ind)

        for i in range(len(self.content_list)):
            try:
                file_out.write(self.content_list[i] + ("\n\t" + self.indent + ind))
            except:
                self.content_list[i].render(file_out, "    ")

        file_out.write("\n" + self.indent + ind + "</" + self.tag +">\n")


    def append(self, newcontent):
        """ add something within the html element"""
        self.content_list.append(newcontent)

class Html(Element):
    tag = 'html'
class Body(Element):
    tag = 'body'
class P(Element):
    tag = 'p'



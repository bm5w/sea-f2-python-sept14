#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = 'html'
    indent = '\t'
    kwargs = None
    def __init__(self, content = None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.content_list = []
        else:
            self.content_list = [content]

    def render(self, file_out, ind = 1):
        """render the content to file object"""
        attributes = ""

        if self.kwargs == None:
            file_out.write(self.indent * ind + "<" + self.tag +">\n")
        else:
            for i in self.kwargs:
                attributes += " " + i + '="' + str(self.kwargs.get(i)) + '" '
            file_out.write(self.indent * ind + "<" + self.tag + attributes +">\n")

        for i in range(len(self.content_list)):
            try:
                file_out.write(self.indent * (ind + 1) + self.content_list[i] + "\n")
            except:
                self.content_list[i].render(file_out, ind + 1)

        file_out.write(self.indent * ind + "</" + self.tag +">\n")


    def append(self, newcontent):
        """ add something within the html element"""
        self.content_list.append(newcontent)

class Html(Element):
    tag = 'html'
class Body(Element):
    tag = 'body'
class P(Element):
    tag = 'p'
class Head(Element):
    tag = 'head'
class OneLineTag(Element):
    def render(self, file_out, ind = 1):
        file_out.write(self.indent * ind + "<" + self.tag + "> ")
        file_out.write(" ".join(self.content_list))
        file_out.write(" </" + self.tag +">\n")
class Title(OneLineTag):
    tag = 'title'





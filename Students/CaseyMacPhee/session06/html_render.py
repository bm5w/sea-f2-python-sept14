#!/usr/bin/env python
# import from future unicode...
# import pytest
# from circle import Circle
"""
Python class example.
"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = 'html'
    indent = '    '
    kwargs = None
    def __init__(self, content = None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.content_list = []
        else:
            self.content_list = [content]

    def render(self, file_out, ind = 0):
        """render the content to file object"""
        attributes = ""

        if self.kwargs == None:
            file_out.write(self.indent * ind + "<" + self.tag +">\n")
        else:
            for i in self.kwargs:
                attributes += " " + i + '="' + str(self.kwargs.get(i)) + '"'
            file_out.write(self.indent * ind + "<" + self.tag + attributes +">\n")

        for i in range(len(self.content_list)):

            """Here the element is implicitly tested for a content list by attempting a write,
             else each element's render method is called."""
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
    def render(self, file_out, ind = 0):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, ind)


class Body(Element):
    tag = 'body'
class P(Element):
    tag = 'p'
class Head(Element):
    tag = 'head'
class OneLineTag(Element):
    def render(self, file_out, ind = 0):
        attributes = ""
        if self.kwargs == None:
            file_out.write(self.indent * ind + "<" + self.tag + ">")
            file_out.write(" ".join(self.content_list))
            file_out.write("</" + self.tag +">\n")
        else:
            for i in self.kwargs:
                attributes += " " + i + '="' + str(self.kwargs.get(i)) + '"'
            file_out.write(self.indent * ind + "<" + self.tag + attributes +">")
            file_out.write(" ".join(self.content_list))
            file_out.write("</" + self.tag +">\n")

class Title(OneLineTag):
    tag = 'title'
class SelfClosingTag(Element):

    def render(self, file_out, ind = 0):
        attributes = ""
        if self.kwargs == None:
            file_out.write(self.indent * ind + "<" + self.tag +" />\n")
        else:
            for i in self.kwargs:
                attributes += " " + i + '="' + str(self.kwargs.get(i)) + '"'
            file_out.write(self.indent * ind + "<" + self.tag + attributes +" />\n")
class Hr(SelfClosingTag):
    tag = 'hr'
class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content = None):
        linkdict = {"href":link}
        Element.__init__(self, content, **linkdict)
class Ul(Element):
    tag = 'ul'
class Li(Element):
    tag = 'li'
class H(OneLineTag):
    tag = 'h'
    def __init__(self, num, content = None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = self.tag + str(num)
class Meta(SelfClosingTag):
    tag = 'meta'


        









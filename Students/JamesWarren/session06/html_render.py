#!/usr/bin/env python

class Element(object):
    tag = "html"
    ind = ""
    
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs


    def append(self,append_content):
        """ append new content to element """
        self.content.append(append_content)


    def render(self, file_out, ind=""):
        """ render the content to the given file """
        cind = ind
        if len(self.attributes) == 0:
            file_out.write("\n%s<%s>" % (ind, self.tag))
        else:
            attributepair = self.attributes.items()
            file_out.write("\n%s<%s %s=%s>" % (ind, self.tag, attributepair[0][0], attributepair[0][1]))
        ind += "    "
        for item in self.content:
            try:
                item.render(file_out, ind)
            except AttributeError:
                file_out.write("\n"+ind+self.content[0])
        file_out.write("\n%s</%s>" % (cind, self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("\n%s<%s>%s</%s>" % (ind, self.tag, self.content[0], self.tag))

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("\n%s<%s />" % (ind, self.tag))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"
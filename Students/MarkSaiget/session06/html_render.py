#! /usr/bin/env python
"""do session 6 hw, HTML render"""

# all future strings are u''  is assumed
from __future__ import unicode_literals


class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.attributes = kwargs

    def append(self, new_input):
        """add into string"""
        self.content.append(new_input)

    def render(self, file_out, ind=""):
        file_out.write("\n{ind}<{tag}".format(ind=ind, tag=self.tag))
        for key, value in self.attributes.items():
            file_out.write(" {key}=\"{value}\"".format(key=key, value=value))
        file_out.write(">")
        for con in self.content:
            try:
                con.render(file_out, self.indent+ind)
            except AttributeError:
                file_out.write("\n{ind}{indent}{con}".
                               format(ind=ind, indent=self.indent, con=con))
        file_out.write("\n{ind}</{tag}>".format(ind=ind, tag=self.tag))


class Html(Element):
    tag = 'html'

    def render(self, file_out, ind=""):
        Element.render(self, file_out, "")


class Body(Element):
    tag = 'body'


class P(Body):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("\n{ind}<{tag}".format(ind=ind, tag=self.tag))
        for key, value in self.attributes.items():
            file_out.write(" {key}=\"{value}\"".format(key=key, value=value))
        file_out.write(">")
        for con in self.content:
            try:
                con.render(file_out)
            except AttributeError:
                file_out.write("{con}".format(con=con))
        file_out.write("</{tag}>".format(ind=ind, tag=self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("\n{ind}<{tag}>".format(ind=ind, tag=self.tag))


class Hr(SelfClosingTag):
    tag = "hr /"


class Br(SelfClosingTag):
    tag = "br /"


class A(OneLineTag):
    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)
        # or
        # self.content = "<a href=\"{link}\">{content}</a>".\
        #     format(link=link, content=content)

class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = 'h'
    def __init__(self, num, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.tag = self.tag + str(num)


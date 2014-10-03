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
            attributestr = ""
            for key, value in self.attributes.items():
                attributestr = attributestr + ' %s="%s"' % (key, value)
            file_out.write("\n%s<%s%s>" % (ind, self.tag, attributestr))
        ind += "    "
        for item in self.content:
            try:
                item.render(file_out, ind)
            except AttributeError:
                file_out.write("\n%s%s" % (ind, item))
        file_out.write("\n%s</%s>" % (cind, self.tag))


class Html(Element):
    tag = "html"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super(Html, self).render(file_out=file_out, ind=ind)


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
        if len(self.attributes) == 0:
            file_out.write("\n%s<%s />" % (ind, self.tag))
        else:
            attributestr = ""
            for key, value in self.attributes.items():
                attributestr = attributestr + ' %s="%s"' % (key, value)
            file_out.write('\n%s<%s%s />' % (ind, self.tag, attributestr))
#        file_out.write("\n%s<%s />" % (ind, self.tag))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link=None, content=None):
        if link is not None:
            self.link = ' href="%s"' % link
        super(A, self).__init__(content)

    def render(self, file_out, ind=""):
        file_out.write("\n%s<%s%s>%s</%s>" % (ind, self.tag, self.link, self.content[0], self.tag))


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    def __init__(self, level, content=None):
        self.tag = "h%s" % level
        super(H, self).__init__(content)


class Meta(SelfClosingTag):
    tag = "meta"

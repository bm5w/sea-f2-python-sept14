from __future__ import unicode_literals

class Element(object):
    tag_name = "GENERIC ELEMENT"
    tabstring = "    "

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, s):
        """Append s to self.content (list)"""
        self.content.append(s)

    def render(self, file_out, indent_level=0):
        """Write an Element and its content to file_out"""
        if self.attributes:
            attribute_format_string = " ".join(['{key}="{{{key}}}"'.format(key=key) for key in self.attributes])
            tag_open = "<" + self.tag_name + " " + attribute_format_string.format(**self.attributes) + ">"
        else:
            tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        ind = Element.tabstring * indent_level
        if not self.content:
            file_out.write(ind + tag_open + tag_close + "\n")
            return
        if len(self.content) == 1 and (isinstance(self.content[0], str)\
                                        or isinstance(self.content[0], unicode))\
                                  and len(self.content[0]) < 10:
            file_out.write(ind + tag_open + self.content[0] + tag_close + "\n")
            return
        file_out.write(ind + tag_open + "\n")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, indent_level + 1)
            else:
                file_out.write(ind + Element.tabstring + item + "\n")
        file_out.write(ind + tag_close + "\n")

class Html(Element):
    tag_name = "html"

    def render(self, file_out, indent_level=0):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, indent_level)

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

class Head(Element):
    tag_name = "head"

class OneLineTag(Element):
    def render(self, file_out, indent_level=0):
        if self.attributes:
            attribute_format_string = " ".join(['{key}="{{{key}}}"'.format(key=key) for key in self.attributes])
            tag_open = "<" + self.tag_name + " " + attribute_format_string.format(**self.attributes) + ">"
        else:
            tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        ind = Element.tabstring * indent_level
        if not self.content:
            file_out.write(ind + tag_open + tag_close + "\n")
        else:
            file_out.write(ind + tag_open + self.content[0] + tag_close + "\n")
        #anything other than the first content won't render: be careful. It has to be a string

class Title(OneLineTag):
    tag_name = "title"

class SelfClosingTag(Element):
    def render(self, file_out, indent_level=0):
        ind = Element.tabstring * indent_level
        if self.attributes:
            attribute_format_string = " ".join(['{key}="{{{key}}}"'.format(key=key) for key in self.attributes])
            file_out.write(ind + "<" + self.tag_name + " " + attribute_format_string.format(**self.attributes) + " />\n")
        else:
            file_out.write(ind + "<" + self.tag_name + " />\n")

class Hr(SelfClosingTag):
    tag_name = "hr"

class Br(SelfClosingTag):
    tag_name = "br"

class A(Element):
    tag_name = "a"

    def __init__(self, link=None, content=None):
        Element.__init__(self, content, href=link)

class Ul(Element):
    tag_name = "ul"

class Li(Element):
    tag_name = "li"

class H(OneLineTag):
    def __init__(self, level=1, content=None, **kwargs):
        self.tag_name = "h" + str(level)
        OneLineTag.__init__(self, content, **kwargs)

class Meta(SelfClosingTag):
    tag_name = "meta"




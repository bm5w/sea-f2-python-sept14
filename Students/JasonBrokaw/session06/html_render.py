from __future__ import unicode_literals

class Element(object):
    tag_name = "GENERIC ELEMENT"
    tabstring = "  "

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, s):
        """Append s to self.content (list)"""
        self.content.append(s)

    def addtabs(self, line_list):
        """Return a list with a tab before all items (strings) in line_list"""
        tabbed_list = [Element.tabstring + line for line in line_list]
        return tabbed_list

    def render_list(self):
        """Return a 'properly tabbed' list of strings for Element and its content"""
        if self.attributes:
            attribute_format_string = " ".join(['{key}="{{{key}}}"'.format(key=key) for key in self.attributes])
            tag_open = "<" + self.tag_name + " " + attribute_format_string.format(**self.attributes) + ">"
        else:
            tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        if not self.content:
            return [tag_open + tag_close]
        if len(self.content) == 1 and (isinstance(self.content[0], str)\
                                        or isinstance(self.content[0], unicode)):
            return [tag_open + self.content[0] + tag_close]
        line_list = [tag_open]
        for item in self.content:
            if isinstance(item, Element):
                line_list.extend(self.addtabs(item.render_list()))
            else:
                line_list.append(Element.tabstring + item)
        line_list.append(tag_close)
        return line_list

    def render(self, file_out):
        """Write self and all its contents to file_out"""
        output_string = "\n".join(self.render_list())
        file_out.write(output_string)

class Html(Element):
    tag_name = "html"

    def render_list(self):
        line_list = ["<!DOCTYPE html>"]
        line_list.extend(Element.render_list(self))
        return line_list

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

class Head(Element):
    tag_name = "head"

class OneLineTag(Element):
    def render_list(self):
        tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        if not self.content:
            return [tag_open + tag_close]
        return [tag_open + self.content[0] + tag_close]
        #anything other than the first content won't render: be careful.

class Title(OneLineTag):
    tag_name = "title"

class SelfClosingTag(Element):
    def render_list(self):
        if self.attributes:
            attribute_format_string = " ".join(['{key}="{{{key}}}"'.format(key=key) for key in self.attributes])
            return ["<" + self.tag_name + " " + attribute_format_string.format(**self.attributes) + " />"]
        return ["<" + self.tag_name + " />"]

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




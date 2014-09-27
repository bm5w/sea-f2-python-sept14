from __future__ import unicode_literals

class Element(object):
    tag_name = "GENERIC ELEMENT"
    tabstring = "  "

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, s):
        self.content.append(s)

    def addtabs(self, line_list):
        tabbed_list = [Element.tabstring + line for line in line_list]
        return tabbed_list

    def render_list(self):
        """Return a 'properly tabbed' list of strings for Element and its content"""
        tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        if not self.content:
            return [tag_open + tag_close]
        if len(self.content) == 1 and isinstance(self.content[0], unicode):
            return [tag_open + self.content[0] + tag_close]
        else:
            line_list = [tag_open]
            for item in self.content:
                if isinstance(item, Element):
                    line_list.extend(self.addtabs(item.render_list()))
                else:
                    line_list.append(Element.tabstring + item)
            line_list.append(tag_close)
            return line_list

    def render(self, file_out):
        output_string = "\n".join(self.render_list())
        file_out.write(output_string)

class Html(Element):
    tag_name = "html"

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

class Element(object):
    tag_name = u"html"
    indentation_level = 0
    tabstring = u"  "

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, s):
        self.content.append(s)

    def addtabs(self, line_list, level=0):
        tabbed_list = [level * Element.tabstring + line for line in line_list]
        return tabbed_list

    def render(self, file_out):
        tag_open = "<" + self.tag_name + ">"
        tag_close = "</" + self.tag_name + ">"
        if not self.content:
            output_string = Element.tabstring * self.indentation_level + \
                            tag_open + tag_close
        elif len(self.content) == 1:
            output_string = Element.tabstring * self.indentation_level + \
                            tag_open + self.content[0] + tag_close
        else:
            tabbed_content = self.addtabs(self.content, 1)
            line_list = [tag_open] + tabbed_content + [tag_close]
            line_list = self.addtabs(line_list, self.indentation_level)
            output_string = "\n".join(line_list)
        file_out.write(output_string)

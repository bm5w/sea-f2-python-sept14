from __future__ import unicode_literals

class Element():
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if content is not None:
            self.content = [str(content)]
        else:
            self.content = []

    def append(self, new_input):
        """add in to string"""
        self.content.append(new_input)

    def render(self, file_out, ind=""):
        file_out.write("{ind1}<{tag}>\n{ind1}{indent1}".
                       format(ind1=ind, indent1=self.indent, tag=self.tag))
        file_out.write("\n{ind}{indent}".format(ind=ind, indent=self.indent)
                       .join(self.content))
        file_out.write("\n{ind}</{tag}>".format(ind=ind, tag=self.tag))


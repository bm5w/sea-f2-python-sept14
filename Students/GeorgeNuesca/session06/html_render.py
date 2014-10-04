class Element(object):

    tag = u'html'

    def __init__(self, content = None, **kwargs): #initializer
        if content is not None:  #Check for none
            self.content = [str(content)]  # Making a list to append (knowing append in future)
        else:
            self.content = []  #
        self.styling = []
        for elem in kwargs.keys():
            self.styling.append(' ' + elem + '=' + '"' + kwargs[elem] + '"')

    def append(self, new_content, **kwargs):
        ''' Add some new content to the element '''
        self.content.append(new_content)  # Now you can append content using this method

    def render(self, file_out, ind = u'', **kwargs):
        ''' render the contet to the given file like object '''
        if kwargs == []:
            file_out.write(ind + u"<" + self.tag + u">" + u"\n")  # Places beginning tags
        else:
            file_out.write(ind + u"<" + self.tag + ' '.join(self.styling) + u">" + u"\n")

        mind = (ind)

        ind += '    '

        for elem in self.content:
            if isinstance(elem, basestring):
                file_out.write(ind + elem  + u"\n")
            else:
                elem.render(file_out, ind)

        file_out.write(mind + u"</" + self.tag + u">" + u"\n")# + u"\n")  #Places closing tags

class Html(Element):
    tag = u'html'

    def render(self, file_out, ind = ''):
        file_out.write(u'<!DOCTYPE html>\n')
        Element.render(self, file_out, ind = '')

class Body(Element):
    tag = u'body'

class P(Element):
    tag = u'p'

class Head(Element):
    tag = u'head'

class Title(Element):
    tag = u'title'

    def render(self, file_out, ind = u''):
        file_out.write(ind + u"<" + self.tag + u">" +
            u''.join(self.content) + u"</" + self.tag + u">" + u"\n")

class Hr(Element):
    tag = u'hr'
    def render(self, file_out, ind = u''):
        file_out.write(ind + u"<" + self.tag + " />" + u"\n")

class Br(Element):
    def render(self, file_out, ind = u''):
        file_out.write(ind + u"<br />" + u"\n")

class A(Element):
    tag = u'a'

    def __init__(self, *args):
        self.styling = str(u' href = ' + args[0])
        self.content = [args[1]]

    def render(self, file_out, ind = u''):
        file_out.write(ind + u"<" + self.tag + self.styling + u">" +
            u''.join(self.content) + u"</" + self.tag + u">" + u"\n")

class Ul(Element):
    tag = u'ul'

class Li(Element):
    tag = u'li'

class H(Title):
    def __init__(self, *args):
        self.tag = u'h' + str(args[0])
        self.content = args[1]

class Meta(Hr):
    def __init__(self, **kwargs):
        self.tag = u'meta ' + kwargs.keys()[0] + u'=' + u'"' + kwargs.values()[0] + u'"'
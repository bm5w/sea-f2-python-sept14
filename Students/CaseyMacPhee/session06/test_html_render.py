import codecs
import cStringIO
import pytest
import html_render as hr
reload(hr)
## writing the file out:

def test_html():
	def render(page, filename):
	   """
	   render the tree of elements

	   This uses cSstringIO to renderto memory, then dump to console and
	   write to file -- very handy!
	   """

	   f = cStringIO.StringIO()
	   page.render(f)

	   f.reset()

	   print f.read()

	   f.reset()
	   codecs.open(filename, 'w', encoding="utf-8").write( f.read() )

	# # Step 8
	# ########

	page = hr.Html()


	head = hr.Head()
	head.append( hr.Meta(charset=u"UTF-8") )
	head.append(hr.Title(u"PythonClass = Revision 1087:"))

	page.append(head)

	body = hr.Body()

	body.append( hr.H(2, u"PythonClass - Class 6 example") )

	body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
	              style=u"text-align: center; font-style: oblique;"))

	body.append(hr.Hr())

	list = hr.Ul(id=u"TheList", style=u"line-height:200%")

	list.append( hr.Li(u"The first item in a list") )
	list.append( hr.Li(u"This is the second item", style="color: red") )

	item = hr.Li()
	item.append(u"And this is a ")
	item.append( hr.A(u"http://google.com", "link") )
	item.append(u"to google")

	list.append(item)

	body.append(list)

	page.append(body)

	render(page, u"test_html_output8.html")
	thefile = open("test_html_output8.html", 'r')
	text = thefile.read()	
	thefile.close()
	comptext = \
"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <h2>PythonClass - Class 6 example</h2>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
        <ul style="line-height:200%" id="TheList">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
            <li>
                And this is a 
                <a href="http://google.com">link</a>
                to google
            </li>
        </ul>
    </body>
</html>"""
	assert text == comptext




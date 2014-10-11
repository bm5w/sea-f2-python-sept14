#!/usr/bin/env python

"""
code that tests the html_render classes defined in html_render.py

can be run with py.test
"""

from __future__ import unicode_literals
import html_render as h
import cStringIO


def test_tagconstruction():
    """Test that the content is set on construction"""
    c = h.Element("Boogaboo")
    assert "Boogaboo" in c.content


def test_append():
    """Test that we can properly append a string to the element"""
    page = h.Element("A first string")
    page.append("A different string")
    assert "A first string" in page.content
    assert "A different string" in page.content


def test_render():
    """Test that the page can properly render a string in a tag"""
    f = cStringIO.StringIO()
    page = h.Element("String 1")
    page.append("String 2")

    page.render(f)

    f.reset()
    expected_output = "<GENERIC ELEMENT>\n" + h.Element.tabstring + \
        "String 1\n" + h.Element.tabstring + "String 2\n" +\
        "</GENERIC ELEMENT>\n"

    assert f.read() == expected_output


def test_body_p():
    """Test that body and p have the correct names and render"""
    assert h.Body().tag_name == "body"
    assert h.P().tag_name == "p"
    f = cStringIO.StringIO()
    h.P().render(f)
    f.reset()
    assert f.read() == "<p></p>\n"
    f.reset()
    h.Body().render(f)
    f.reset()
    assert f.read() == "<body></body>\n"


def test_title_oneline():
    """Test that the title tag displays on one line (implicitly tests inline performance)"""
    t = h.Title("PythonClass - Session 6 example blah blah I'm so long blaaaaaaah")
    f = cStringIO.StringIO()
    t.render(f)
    f.reset()
    assert f.read() == "<title>PythonClass - Session 6 example blah blah I'm so long blaaaaaaah</title>\n"


def test_attributes():
    """Test that attributes an be set on construction and render properly"""
    p = h.P("text", id="p1", style="color: red;")
    f = cStringIO.StringIO()
    p.render(f)
    f.reset()
    assert f.read() == '<p style="color: red;" id="p1">text</p>\n'


def test_self_closing():
    """Test that self-closing tags display as expected"""
    br = h.Br(id="br1")
    f = cStringIO.StringIO()
    br.render(f)
    f.reset()
    assert f.read() == '<br id="br1" />\n'


def test_a():
    """Test that link tags are constructed and render as expected"""
    a = h.A("http://google.com", "link to google")
    f = cStringIO.StringIO()
    a.render(f)
    f.reset()
    assert f.read() == '<a href="http://google.com">\n' +\
        h.Element.tabstring + "link to google\n" + "</a>\n"


def test_header():
    """Test headers are constructed and rendered as expected"""
    h2 = h.H(2,"Second-level-heading")
    f = cStringIO.StringIO()
    h2.render(f)
    f.reset()
    assert f.read() == "<h2>Second-level-heading</h2>\n"


def test_html():
    """Test that the html tag displays the DOCTYPE line"""
    html = h.Html()
    f = cStringIO.StringIO()
    html.render(f)
    f.reset()
    assert f.read() == "<!DOCTYPE html>\n<html></html>\n"

def test_meta():
    """Test that the meta tag is constructed and renders"""
    meta = h.Meta(charset="UTF-8")
    f = cStringIO.StringIO()
    meta.render(f)
    f.reset()
    assert f.read() == '<meta charset="UTF-8" />\n'

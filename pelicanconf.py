#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "André P. Santos"
SITENAME = "__ztz__"
SITEURL = "."

PATH = "content"

TIMEZONE = "America/Sao_Paulo"

DEFAULT_LANG = "pt_BR"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "http://getpelican.com/"),
#     ("Python.org", "http://python.org/"),
#     ("Jinja2", "http://jinja.pocoo.org/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images", "extra"]
ICONS_PATH = "images/icons"

PLUGIN_PATHS = ["plugins/"]
PLUGINS = ["assets", "neighbors"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/pure-single"


### pure-single ###


MENUITEMS = (
    ("Archives", "/archives.html"),
    # ("About", "/pages/about"),
    # ("Blog", "/blog.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    # ("Test", "/pages/test"),
)


SOCIAL = (
    ("facebook", "https://www.facebook.com/ztzandre"),
    ("github", "https://github.com/andreztz"),
    ("twitter", "https://twitter.com/andreztz"),
    ("instagram", "https://www.instagram.com/andreztz/"),
    ("strava", "https://www.strava.com/athletes/27260098"),
    ("rss", "/feeds/all.atom.xml"),
)

# Set the sidebar image (Optional).
COVER_IMG_URL = "images/cover.jpg"
# Set the image for the top circle cutout
PROFILE_IMG_URL = "images/icons/avatar.png"
#  Used for the page titles and some meta tags.
TAGLINE = "High tech, Low life."
#  Set the favicon image
FAVICON_URL = ""
# Set this to enable disqus comments in articles.
DISQUS_SITENAME = "andreztz"
# Set this to True to enable disqus comments in pages.
DISQUS_ON_PAGES = ""
# Set the Google Analytics code (eg. "UA-000000-00")
GOOGLE_ANALYTICS = ""


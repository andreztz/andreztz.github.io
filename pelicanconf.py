#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

BASE = os.path.dirname(__file__)

AUTHOR = 'André Santos'
AUTHOR_EMAIL = 'andreztz@gmail.com'
SITENAME = 'André Santos - Blog'
SITEURL = 'https://andreztz.github.io'
TIMEZONE = 'America/Sao_Paulo'

PATH = 'content'
STATIC_PATHS = ['images']


TIMEZONE = 'America/Sao_Paulo'
LOCALE = ('pt_BR.utf8',)
DEFAULT_LANG = 'pt'

THEME = "themes/puro"
USE_PAGER = 'True'

SITELOGO = 'http://i.imgbox.com/71jbSiuD.jpg'
COVER_IMG_URL='http://i.imgbox.com/LXH5WQux.jpeg'
AVATAR = '4d420075a242b2c9b470b23ec2a914a0.png'
# PROFILE_IMAGE_URL = 'http://i.imgbox.com/71jbSiuD.jpg'
PROFILE_IMAGE_URL = 'https://www.gravatar.com/avatar/' + AVATAR



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Home', '/'),
    ('Arquivo', 'archives.html'),
    ('Sobre', 'pages/about.html'),
)


# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/ztzandre'),
    ('github', 'https://github.com/andreztz'),
    ('youtube', 'https://www.youtube.com/channel/UCAwZjRyaUvoVu2thZBoGO8w'),
    ('google-plus', 'https://plus.google.com/u/0/+AndréSantosztz'),
    ('twitter', 'https://twitter.com/rootztz')
)


STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt']# , 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    # 'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'},
    # 'extras/favicon.ico': {'path': 'favicon.ico'}
}


FAVICON = 'extras/favicon.ico'

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
    'optimize_images',
    'representative_image',
    'pelican_youtube',
    'pelican_vimeo',
    'sitemap',
    'better_codeblock_line_numbering',
    'better_figures_and_images',
]

MD_EXTENSIONS = [
    'codehilite(css_class=highlight,linenums=True)', 'extra']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


DEFAULT_PAGINATION = 5

# DISQUS_SITENAME = 'andreztz'

SUMMARY_MAX_LENGTH = 25

GOOGLE_ANALYTICS = 'UA-61458769-1'

RESPONSIVE_IMAGES = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

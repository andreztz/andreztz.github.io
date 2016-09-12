#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

BASE = os.path.dirname(__file__)

AUTHOR = 'andreztz@gmail.com'
SITENAME = 'Andre ZTZ - Blog'
SITEURL = 'https://andreztz.github.io'
TIMEZONE = 'America/Sao_Paulo'
SITELOGO = 'http://i.imgbox.com/71jbSiuD.jpg'
AVATAR = '4d420075a242b2c9b470b23ec2a914a0.png'
# PROFILE_IMAGE_URL = 'http://i.imgbox.com/71jbSiuD.jpg'
PROFILE_IMAGE_URL = 'http://www.gravatar.com/avatar/' + AVATAR


PATH = 'content'
STATIC_PATHS = ['images']


TIMEZONE = 'America/Sao_Paulo'
LOCALE = ('pt_BR.utf8',)
DEFAULT_LANG = 'pt'

THEME = "themes/pure"
USE_PAGER = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Arquivo', 'archives.html'),
    ('Sobre', 'pages/about.html'),
    # ('Videos', 'pages/videos.html')
    # ('Autores', 'authors.html'),
    # ('Categorias', 'categories.html'),
    # ('Tags', 'tags.html'),
    # ('Videos', 'pages/videos.html'),
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


STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt']

EXTRA_PATH_METADATA = {
    # 'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
    'optimize_images',
    'pelican_youtube',
    'pelican_vimeo',
    'googleplus_comments',
    'representative_image',
    'gravatar',
    'sitemap'
]
# , 'share_post', , ,'better_figures_and_images',

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

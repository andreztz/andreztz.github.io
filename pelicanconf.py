# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = "André P. Santos"
# SITEURL = "http://localhost:5000"
SITEURL = "."
SITENAME = "__ztz__"
SITETITLE = "__ztz__"
SITESUBTITLE = "André P. Santos blog"
SITEDESCRIPTION = "Anotações"
SITELOGO = "http://i.imgbox.com/71jbSiuD.jpg"
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

# USE_PAGER = "True" ???

ROBOTS = "index, follow"

THEME = "themes/Flex"
PATH = "content"
# OUTPUT_PATH = "blog/"
TIMEZONE = "America/Sao_Paulo"

LOCALE = ("pt_BR.utf8",)


DATE_FORMATS = {"en": "%B %d, %Y", "pt_BR.utf-8": " %d/%m/%Y"}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = (
    True
)  # BUG Quando habilitado no menu de navegação superior ao clicar sobre andre santos
HOME_HIDE_TAGS = True

SOCIAL = (
    ("facebook", "https://www.facebook.com/ztzandre"),
    ("github", "https://github.com/andreztz"),
    ("twitter", "https://twitter.com/andreztz"),
    ("rss", "/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    ("About", "/pages/about"),
    # ("Test", "/pages/test"),
)

PLUGIN_PATHS = ["./pelican-plugins"]

# Enable i18n plugin.
PLUGINS = ["i18n_subsites", "pelican_youtube"]
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

DEFAULT_LANG = "pt_BR"
OG_LOCALE = "pt_BR"
I18N_TEMPLATES_LANG = "en"


COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 5

DISQUS_SITENAME = "andreztz"
ADD_THIS_ID = "ra-55adbb025d4f7e55"


EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    # 'images/favicon.ico': {'path': 'favicon.ico'}
    "extra/custom.css": {"path": "static/custom.css"},
}
# https://stackoverflow.com/questions/44209165/hosting-raw-html-pages-in-a-pelican-static-website
# diretorios e arquivos que são incluidos no output a partir do content
# diretorios vazios não são incluidos.
STATIC_PATHS = ["images", "extra"]
CUSTOM_CSS = "static/custom.css"
USE_LESS = True


SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.6, "indexes": 0.6, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

USE_GOOGLE_FONTS = True
THEME_STATIC_DIR = "static"

DISABLE_URL_HASH = True

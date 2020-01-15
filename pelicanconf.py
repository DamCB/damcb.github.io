#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Guillaume Gay"
SITENAME = "Morphogénie Logiciels"
SITEURL = "http://morphogenie.fr"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/glyg"


# Blogroll
LINKS = (("Scipy", "http://scipy.org/"), ("Python.org", "http://python.org/"))

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/DamCB"),
    ("Twitter", "https://twitter.com/MorphoLG"),
)

DEFAULT_PAGINATION = 10

# GITHUB_USER = 'DamCB'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("About Morphogénie", "/pages/aboutus.html"),
    ("Projects", "/pages/projects.html"),
    ("Services", "/pages/what-we-do.html"),
    ("Tools", "/pages/tools.html"),
    ("Contact", "/pages/contact.html"),
)

# BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_THEME = "cosmo"

SITELOGO = "images/logo_blackbg.png"
HIDE_SITENAME = True

DISPLAY_TAGS_ON_SIDEBAR = True

STATIC_PATHS = ["images"]
TYPOGRIFY = True

CODE_DIR = "downloads/code"
NOTEBOOK_DIR = "downloads/notebooks"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "summary",
    "liquid_tags.img",
    "liquid_tags.video",
    "liquid_tags.vimeo",
    "liquid_tags.youtube",
    "liquid_tags.include_code",
    "liquid_tags.notebook",
    "liquid_tags.literal",
    "render_math",
]

ABOUT_ME = """Data analysis and modeling for Cell Biology\n
We offer free and open source software services to help biologists get the most out of their experiments."""

### Those are displayed on the index page, with one image, a title and a link
DISPLAY_HEROITEMS = True
HEROITEMS = (
    ("images/logo_modeling.png", "Projects", "/pages/projects.html"),
    ("images/logo_python.png", "Tools", "/pages/tools.html"),
    ("images/logo_data.png", "Services", "/pages/what-we-do.html"),
)

AVATAR = False  #'images/logo_blackbg.png'

FAVICON = "images/favicon.png"
# FAVICON_IE = 'images/favicon.png'


FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
NEWEST_FIRST_ARCHIVES = True
SUMMARY_END_MARKER = "<!-- TEASER_END -->"


# Following items are often useful when publishing
DISQUS_SITENAME = "damcellbiology"


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

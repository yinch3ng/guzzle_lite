guzzle_lite Sphinx Theme
========================

Inspired by Guzzle Sphinx theme from <https://github.com/guzzle/guzzle_sphinx_theme> :)

Installation
------------

-   Need to install [Git](<https://git-scm.com>) firstly.

Install via pip:

    $ pip install git+https://github.com/yinch3ng/guzzle_lite.git

or

    $ pip install git+ssh://github.com/yinch3ng/guzzle_lite.git

Configuration
-------------

Add the following to your conf.py:

``` python
import guzzle_lite

html_theme_path = guzzle_lite.html_theme_path()
html_theme = 'guzzle_lite'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_lite")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "Project Name like Homeee,or Docs...",
}
```

There are a lot more ways to customize this theme, as this more
comprehensive example shows:

``` python
import guzzle_lite

html_theme_path = guzzle_lite.html_theme_path()
html_theme = 'guzzle_lite'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_lite")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {

    # Set the path to a special layout to include for the homepage
    "index_template": "special_index.html",

    # Set the name of the project to appear in the left sidebar.
    "project_nav_name": "Project Name",

    # Set your Disqus short name to enable comments
    "disqus_comments_shortname": "my_disqus_comments_short_name",

    # Set you GA account ID to enable tracking
    "google_analytics_account": "my_ga_account",

    # Path to a touch icon
    "touch_icon": "",

    # Specify a base_url used to generate sitemap.xml links. If not
    # specified, then no sitemap will be built.
    "base_url": ""

    # Allow a separate homepage from the master_doc
    "homepage": "index",

    # Allow the project link to be overriden to a custom URL.
    "projectlink": "http://myproject.url",
}
```

Customizing the layout
----------------------

You can customize the theme by overriding Jinja template blocks. For
example, \"layout.html\" contains several blocks that can be overridden
or extended.

Place a \"layout.html\" file in your project\'s \"/\_templates\"
directory.

``` bash
mkdir source/_templates
touch source/_templates/layout.html
```

Then, configure your \"conf.py\":

``` python
templates_path = ['_templates']
```

Finally, edit your override file \"source/\_templates/layout.html\":

    {# Import the theme's layout. #}
    {% extends "!layout.html" %}

    {%- block extra_head %}
    {# Add custom things to the head HTML tag #}
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}

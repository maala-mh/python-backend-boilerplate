import re
import logging
import jinja2


logger = logging.getLogger(__name__)


def get_env():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("/src/content"),
        extensions=["jinja2.ext.i18n", "jinja2.ext.loopcontrols"],
    )
    env.policies["ext.i18n.trimmed"] = True
    env.install_null_translations(newstyle=True)
    return env


def get_jinja_template_by_filename(filename):
    # ends with ext?
    if filename.endswith(".html"):
        lookup_filename = filename
    else: # add html default suffix
        lookup_filename = filename + ".html"
    return get_env().get_template("{}".format(lookup_filename))

import logging
import random

from . import jinja


logger = logging.getLogger(__name__)

COIN_FACE_MAPPING = {
    0: "heads",
    1: "tails"
}

COIN_IMAGE_MAPPING = {
    0: "https://media.geeksforgeeks.org/wp-content/uploads/20231016151817/heads.png",
    1: "https://media.geeksforgeeks.org/wp-content/uploads/20231016151806/tails.png"
}


def flip_heads_or_tails():
    number = random.randrange(0, 2)
    html_ctx = {
        "coin_face": COIN_FACE_MAPPING[number],
        "coin_image": COIN_IMAGE_MAPPING[number],
    }
    template = jinja.get_jinja_template_by_filename("headsortails.html")
    return template.render(**html_ctx)

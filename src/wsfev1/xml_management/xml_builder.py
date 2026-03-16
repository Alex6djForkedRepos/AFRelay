

from lxml import etree

from src.shared.paths_config import paths
from src.shared.utils.logger import logger


def extract_token_and_sign_from_xml() -> tuple[str, str]:

    path = paths.get_afip_paths().login_response
    tree = etree.parse(path)
    root = tree.getroot()

    token_label = root.find(".//token")
    sign_label = root.find(".//sign")

    token = token_label.text
    sign = sign_label.text

    return token, sign
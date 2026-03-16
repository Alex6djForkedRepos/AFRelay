from src.wsfev1.xml_management.xml_builder import \
    extract_token_and_sign_from_xml


def test_extract_token_and_sign_from_xml():

    token, sign = extract_token_and_sign_from_xml()

    assert token == "fake_token"
    assert sign == "fake_sign"
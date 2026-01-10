from service.xml_management.xml_builder import (
    build_login_ticket_request, extract_token_and_sign_from_xml)


def test_build_login_ticket_request():

    def fake_time_provider():
        return (
            1767764408,
            "2026-01-07T05:40:08Z",
            "2026-01-07T05:50:08Z",
        )

    root = build_login_ticket_request(fake_time_provider)

    assert root.find("header/uniqueId").text == "1767764408"


def test_extract_token_and_sign_from_xml():

    token, sign = extract_token_and_sign_from_xml()

    assert token == "fake_token"
    assert sign == "fake_sign"
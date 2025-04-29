from lxml import etree
from datetime import date
from typing import List
import pytest
from src.scraper import get_spain_boe, get_spain_boe_element_with_text


def test_scraper_fetch_url():
    boe: ElementTree = get_spain_boe(date(2025, 4, 18))

    assert boe.find(".//sumario_diario/identificador").text == "BOE-S-2025-94"


def test_get_right_node():
    boe: etree._ElementTree = etree.parse("boe.xml")

    element: List[etree._ElementTree] = get_spain_boe_element_with_text(
        boe, ["Mercedes Guerrero Romeo"]
    )
    assert element is not None
    assert len(element) == 1
    assert element[0].find("./identificador").text == "BOE-A-2025-7874"


def test_get_more_than_one_node():
    boe: etree._ElementTree = etree.parse("boe.xml")

    element: List[etree._ElementTree] = get_spain_boe_element_with_text(
        boe, ["Mercedes Guerrero Romeo", "prácticas académicas"]
    )
    assert element is not None
    assert len(element) == 3
    assert element[0].find("./identificador").text == "BOE-A-2025-7874"
    assert element[1].find("./identificador").text == "BOE-A-2025-7945"
    assert element[2].find("./identificador").text == "BOE-A-2025-7947"

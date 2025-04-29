import requests
import datetime
from lxml import etree
from typing import List


def get_spain_boe(date: datetime.date) -> etree.ElementTree:
    """
    Get the BOE from the official website of the Spanish government.
    Url is like http://boe.es/datosabiertos/api/boe/sumario/20250418
    :param date: Date to get the BOE from.
    :return: The BOE as a string.
    """
    url = f"http://boe.es/datosabiertos/api/boe/sumario/{date.strftime('%Y%m%d')}"
    headers = {"Accept": "application/xml"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return etree.fromstring(response.content)
    else:
        raise Exception(
            f"Error getting BOE with error {response.status_code}: {response.text}"
        )


def get_spain_boe_element_with_text(
    xml: etree.ElementTree, texts: List[str]
) -> List[etree.ElementTree]:
    """
    Get the first element with the given text.
    :param xml: The XML to search.
    :param text: The text to search for.
    :return: The first element with the given text.
    """
    result = []
    for text in texts:
        result.extend(xml.xpath(f".//titulo[contains(text(), '{text}')]/.."))
    return result

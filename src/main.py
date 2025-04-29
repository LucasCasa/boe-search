import datetime
from time import sleep

from scraper import get_spain_boe_element_with_text, get_spain_boe


# for the last 30 days
today = datetime.date.today()
for i in range(30):
    date = today - datetime.timedelta(days=i)
    # if its a sunday, do nothing
    if date.weekday() == 6:
        continue
    boe = get_spain_boe(date)
    nodes = get_spain_boe_element_with_text(boe, ["Museo"])
    for node in nodes:
        print(
            f"Date: {date}, Title: {node.find('./titulo').text}, ID: {node.find('./identificador').text}, url: {node.find('./url_html').text}"
        )
    sleep(5)
    print("Sleeping for 5 seconds...")

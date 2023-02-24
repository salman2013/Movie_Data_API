from scrapy.selector.unified import SelectorList


def clean(list_or_str):
    if isinstance(list_or_str, str):
        return list_or_str.strip()

    if isinstance(list_or_str, SelectorList):
        list_or_str = list_or_str.getall()

    return [text.strip() for text in list_or_str or [] if text and text.strip()]


def soupify(soup, delimeter=' '):
    if isinstance(soup, str):
        return soup.lower()

    return delimeter.join(soup).lower()

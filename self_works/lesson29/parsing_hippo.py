from lxml import html
from requests import get

ROOT_URL = 'https://gippo-market.by/'
CATALOG = 'https://gippo-market.by/catalog/'

response = get(CATALOG)
products = []

reg_link_categories = '//a[@class="catalog-start__item"]/@href'
dom_catalog = html.fromstring(response.text)
categories = dom_catalog.xpath(reg_link_categories)
print(categories)

while categories:
    category = categories.pop()
    response = get(f'{ROOT_URL}{category}')

    req_under_categories = '//div[@class="link-arrow link-arrow--green"]/a/@href'
    under_category_dom = html.fromstring(response.text)
    under_category = under_category_dom.xpath(req_under_categories)

    if under_category:
        print(f'{category} - {under_category}')
        categories.extend(under_category)
    else:
        req_products = '//a[@class="product-card__img-wrap"]/@href'
        products.extend(under_category_dom.xpath(req_products))

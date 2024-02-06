from lxml import html

with open('index.html', 'r') as f:
    tree = html.fromstring(f.read())
    # req = '//div[@class="container"]/text()'
    # print(tree.xpath(req))
    # req2 ='//div[@class="container"]/div[@class="description"]/text()'
    # print(tree.xpath(req2))
    # req3 = '//div[@class="items"]/div[@class="description"]/text()'
    # print(tree.xpath(req3))
    req4 = '//div[@class="items"]/a/@href'
    print(tree.xpath(req4))
    req5 = '//div[@class="items"]/a[contains(@class,"red")]/@href'
    print(tree.xpath(req5))
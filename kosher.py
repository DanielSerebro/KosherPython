from lxml import html

import requests

page = requests.get('http://www.ka.org.au/index.php/component/option,com_kosherdb/Itemid,61/')

tree = html.fromstring(page.content)

web = tree.xpath("//tr/td/b/a/@href")

products = tree.xpath("//tr/td/b/a/text()")



fullList = []

for i,j in zip(web,products):

    fullList.append([i,j])

    

for x in fullList:

    print(x)
    

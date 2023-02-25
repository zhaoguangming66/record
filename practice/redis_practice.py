import json
import re

import requests
from lxml import etree

headers = {
    "authority": "www.lamontagne.fr",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
cookies = {
    # "didomi_token": "eyJ1c2VyX2lkIjoiMTg2NmNjZGQtYmJlZC02MjE4LTgzNDEtNjAwMzQyYTlkYjc5IiwiY3JlYXRlZCI6IjIwMjMtMDItMjBUMDM6MTE6MjMuNzY1WiIsInVwZGF0ZWQiOiIyMDIzLTAyLTIwVDAzOjExOjIzLjc2NVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsidHdpdHRlciIsImdvb2dsZSIsImM6eW91dHViZSIsImM6aG90amFyIiwiYzpzYW9vdGktQVVZUG5SckQiLCJjOndpbmR5LVVjVGlrdExEIiwiYzpvd25wYWdlIiwiYzphY3BtIiwiYzpzZW5kaW5ibHVlLW5WOXRUZjJGIiwiYzppb3RlY2giLCJjOnRpa3Rvay1LWkFVUUxaOSIsImM6YXRpbnRlcm5lLWNXUUtIZUpaIiwiYzpmYWNlYm9vayIsImM6Z29vZ2xlYW5hLTRUWG5KaWdSIiwiYzpiYXRjaC1WZUhrQWpZOSIsImM6cG9vb2wiLCJjOmFyZW5hIiwiYzptYXplLUI3bjd0RXJ6Il19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImRhTGNxTmtIIiwiYXVkaWVuY2VtLXhlZGVVMmdRIiwiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiXX0sInZlcnNpb24iOjIsImFjIjoiQ25XQUVBa3NGT29BLkNuV0FFQWtzRk9vQSJ9",
    # "euconsent-v2": "CPnezAAPnezAAAHABBENC3CsAP_AAH_AAAAAJQtf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H8-CTYBJhq3EAXYljgTbRhFAiBGFYSFUCgAooBhaIDCB1cFOyuAn1hEgAQCgCMCIEOAKMGAQAAAQBIREBIEeCAQAEQCAAEACoRCAAjYBBQAWBgEAAoBoWKMUAQgSEGRARFKYEBEiQUE9lQglB_oaYQh1lgBQaP-KhARKAEKwIhIWDkOCJAS8WSBZijfIARgBQCiVCtQSemgAAAA.f_gAD_gAAAAA"
}
url = "https://www.lamontagne.fr/clermont-ferrand-63000/sports/le-match-de-belleau-les-fautes-betes-des-clermontois-decouvrez-les-tops-et-les-flops-de-la-defaite-de-l-asm-a-bordeaux-begles_14265007/"
response = requests.get(url, headers=headers, cookies=cookies,timeout=10)

htm=etree.HTML(response.text)
title=htm.xpath("//div[@id='content-inner']//h1//text()")
content=htm.xpath("//div[@class='contenu']/div[@class='c-soustitre']//text()|//div[@class='contenu']//p//text()")
content = ''.join(content)
times = htm.xpath('//meta[@property="article:published_time"]/@content')
print(times)
# print(title,content.replace("Recevez par mail notre newsletter éco et retrouvez l'actualité des acteurs économiques de votre région.",""))
# /theme/ubb-asm-2023/
# /theme/reforme-retraites/
# /theme/fusillade-lagauthiere/
# /theme/accident-pierre-palmade/
# /theme/carte-scolaire-2023/

# /theme/allier/
# /theme/cantal/
# /theme/correze/
# /theme/creuse/
# /theme/haute-loire/
# /theme/puy-de-dome/
# /theme/sports/


# /theme/loisirs/spectacles-festivals-concerts
# /theme/loisirs/sport-nature
# /theme/loisirs/culture-patrimoine
# /theme/loisirs/gastronomie-terroir-vins
# /theme/loisirs/brocantes-salons-foires
# /theme/loisirs/bals-fetes
# /theme/loisirs/television-medias

# /theme/economie/
# /theme/commerce/
# /theme/emploi/
# /theme/agriculture/
# /theme/btp-industrie/
# /theme/innovation/


# dat=re.search("var headerJsonEssentiel = (.*?);", response.text, re.S).group(1)
# da = json.loads(dat)
# for label in da:
#     print(label['link'])
# urls_list=htm.xpath("//li/a[@class='cf-link item-link']/@href")
# print(["theme/loisirs/"+i for i in urls_list])

ss = """
# /theme/ubb-asm-2023/
# /theme/reforme-retraites/
# /theme/fusillade-lagauthiere/
# /theme/accident-pierre-palmade/
# /theme/carte-scolaire-2023/

# /theme/allier/
# /theme/cantal/
# /theme/correze/
# /theme/creuse/
# /theme/haute-loire/
# /theme/puy-de-dome/
# /theme/sports/


# /theme/loisirs/spectacles-festivals-concerts
# /theme/loisirs/sport-nature
# /theme/loisirs/culture-patrimoine
# /theme/loisirs/gastronomie-terroir-vins
# /theme/loisirs/brocantes-salons-foires
# /theme/loisirs/bals-fetes
# /theme/loisirs/television-medias

# /theme/economie/
# /theme/commerce/
# /theme/emploi/
# /theme/agriculture/
# /theme/btp-industrie/
# /theme/innovation/
"""
# print([s.replace("# ",'') for s in ss.split("\n") if s.strip()])
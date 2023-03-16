from bs4 import BeautifulSoup
#
# import requests
#
# url_pj = 'https://promokodoff.ru/promokody-papa-johns/'
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
#
# req = requests.get(url_pj, headers=headers)
# src = req.text
#
# pj_site_w = open('pj_site.html', 'w', encoding='utf-8')
# pj_site_w.write(src)

pj_site = open('pj_site.html', encoding='utf-8')
src = pj_site.read()

soup = BeautifulSoup(src, 'lxml')


def pj_promo_code():
    headers_3_all = soup.find_all(class_='modal modal-template-open-offer modal in')
    d = {}
    for headers in headers_3_all:
        d[headers.find('h3').text + ' (' + headers.find(class_='template-open-offer-description-container')
        .text.rstrip() + ')'] = headers.find(class_='form-control input-lg').get('value')
    return d


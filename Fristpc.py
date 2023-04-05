import requests
from lxml import etree
import sys
import os


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url,headers=headers)
for j in hero_list_resp.json():
    enanme = j.get('ename')
    cname = j.get('cname')
    if not os.path.exists(cname):
        os.makedirs(cname)
# 爬取图片的名字

    hero_url = f'https://pvp.qq.com/web201605/herodetail/{enanme}.shtml'
    hero_rep = requests.get(hero_url,headers=headers)
    hero_rep.encoding='gbk'
    e = etree.HTML(hero_rep.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname',)[0]

    names = [name[0:name.index('&')] for name in names.split('|')]


# 爬取图片
    for i,n in enumerate(names):
        url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{enanme}/{enanme}-bigskin-{i+1}.jpg'
        rep = requests.get(url,headers=headers)
        with open(f'{n}.jpg','wb') as f:
            f.write(rep.content)
        print(f'已下载：{n}的皮肤')

# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request, FormRequest
from scrapy.shell import inspect_response
import urllib


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    # start_urls = ['http://www.lagou.com/']

    # Referer User-Agent 很重要
    header = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.lagou.com/jobs/list_%s',  # 这个参数很重要
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': 'user_trace_token=20170710115630-79cdc6d6-bdac-4884-84d8-9cb6e6d902e3; LGUID=20170710115633-c3a261b1-6523-11e7-a702-5254005c3644; _ga=GA1.2.1508121544.1499658994; index_location_city=%E6%B7%B1%E5%9C%B3; WEBTJ-ID=20180326224106-16262c16c51332-00f4ce8bb652a3-33627805-1024000-16262c16c5252e; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520089463,1520254616,1522075266,1522075272; X_HTTP_TOKEN=b42b665b53c8cdd38bba91b6470531c7; LG_LOGIN_USER_ID=d6c5c68eea5e043c0342d6bf6eb7aecc5f52d2802feeb200; _putrc=4E3AAE3654D553D2; JSESSIONID=ABAAABAACEBACDGAF5CB142326B28CB6C33FE8F1771518E; login=true; unick=%E5%90%91%E5%8A%A8; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=84; _gid=GA1.2.878119735.1522504878; _gat=1; LGSID=20180331220117-fba92b0a-34eb-11e8-b6a4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_php%3Fcity%3D%25E6%25B7%25B1%25E5%259C%25B3%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_php%3Fpx%3Ddefault%26city%3D%25E5%2585%25A8%25E5%259B%25BD; gate_login_token=94d43a167a304ac0a9225c8995f25fc1f7e8baafbe6ff256; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522504922; LGRID=20180331220201-15e2e0ed-34ec-11e8-a9ad-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=0e8c6c906b0e44dd930a08aa4abb0998',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    position = ''
    city = ''
    url = 'https://www.lagou.com/jobs/positionAjax.json?%sneedAddtionalResult=false'

    def __init__(self, position='', city=''):
        if position == '':
            position = 'PHP'
        self.position = position
        ref_param = self.position
        url_param = ''
        if city != '':
            self.city = urllib.quote(city)
            ref_param += '?city='+self.city
            url_param = 'city='+self.city+'&'
        else:
            url_param = 'px=default&'
        self.header['Referer'] = self.header['Referer'] % ref_param
        self.url = self.url % url_param

    def start_requests(self):
        #采集前20页数据
        # for pn in range(20):

        meta = dict({'first': 'false', 'pn': '2', 'kd': self.position})
        print(meta)
        yield FormRequest(url=self.url, headers=self.header, formdata=meta, callback=self.parse)

    def parse(self, response):
        # inspect_response(response, self)
        print(response.text)
        # print(response.body)
        pass

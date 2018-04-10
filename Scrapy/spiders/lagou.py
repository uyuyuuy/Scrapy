# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request, FormRequest
from scrapy.shell import inspect_response
import urllib, json, time, random
from Scrapy.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    # start_urls = ['http://www.lagou.com/']
    custom_settings = {
        'ITEM_PIPELINES' : {
            'Scrapy.pipelines.LagouPipline': 300,
        }
    }
    # Referer User-Agent 很重要
    header = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.lagou.com/jobs/list_%s',  # 这个参数很重要
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=ABAAABAAAGFABEF4B8B4CCEE44025CD06335C627C7312E4; user_trace_token=20180409112244-8fe08c1c-df4b-4e7e-a9d6-11146da0b326; _ga=GA1.2.786081063.1523244165; _gid=GA1.2.891565441.1523244165; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523244165; LGUID=20180409112246-461c7794-3ba5-11e8-b766-525400f775ce; LGSID=20180409172217-7f2f3bf0-3bd7-11e8-b7b4-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel; X_HTTP_TOKEN=e7e70ba689b47a1f73e1fad25019bd84; _gat=1; LG_LOGIN_USER_ID=38246da922d638b8e803866d0fcf16776fcb6ce18e76099b; _putrc=4E3AAE3654D553D2; login=true; unick=%E5%90%91%E5%8A%A8; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=84; gate_login_token=c7775714c7e4b0a8f38d776d28ab128a2fa618a8f9d8d54f; SEARCH_ID=ad0ac2f6792f40dcb7a76a987470c825; index_location_city=%E6%B7%B1%E5%9C%B3; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523267277; LGRID=20180409174757-15376cf2-3bdb-11e8-b741-5254005c3644',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }


    position = ''
    city = ''
    list_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&%sneedAddtionalResult=false'
    details_url = 'https://www.lagou.com/jobs/%d.html'

    def get_header(self):
        user_agent = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko']

        self.header['User-Agent'] = random.randint(0, 3)


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
        self.header['Referer'] = self.header['Referer'] % ref_param
        self.list_url = self.list_url % url_param

    def start_requests(self):
        #采集前20页数据
        # for pn in range(20):
        meta = dict({'first': 'true', 'pn': '1', 'kd': self.position})
        # print(meta)
        self.get_header()
        yield FormRequest(url=self.list_url, headers=self.header, formdata=meta, callback=self.list_parse)


    def list_parse(self, response):
        response_data = json.loads(response.text)
        position_result = response_data['content']['positionResult']['result']
        positionId_list = []
        for position in position_result:
            positionId_list.append(position['positionId'])

            item = LagouItem()
            item['city'] = position['city']
            item['companyFullName'] = position['companyFullName']
            item['companyId'] = position['companyId']
            item['companyLabelList'] = position['companyLabelList']
            item['companyShortName'] = position['companyShortName']
            item['companySize'] = position['companySize']
            item['createTime'] = position['createTime']
            item['district'] = position['district']
            item['education'] = position['education']
            item['financeStage'] = position['financeStage']
            item['firstType'] = position['firstType']
            item['imState'] = position['imState']
            item['industryField'] = position['industryField']
            item['industryLables'] = position['industryLables']
            item['jobNature'] = position['jobNature']
            item['lastLogin'] = position['lastLogin']
            item['latitude'] = position['latitude']
            item['linestaion'] = position['linestaion']
            item['longitude'] = position['longitude']
            item['positionAdvantage'] = position['positionAdvantage']
            item['positionId'] = position['positionId']
            item['positionLables'] = position['positionLables']
            item['positionName'] = position['positionName']
            item['salary'] = position['salary']
            item['salary'] = position['salary']
            item['publisherId'] = position['publisherId']

            item['secondType'] = position['secondType']
            item['stationname'] = position['stationname']
            item['subwayline'] = position['subwayline']
            item['workYear'] = position['workYear']

            yield item

        print(positionId_list)
        for positionId in positionId_list:
            time.sleep(10)
            details_url = self.details_url % positionId
            self.get_header()
            yield Request(url=details_url, method='GET', headers=self.header, callback=self.details_parse, meta={'positionId':positionId})


    def details_parse(self, response):
        description = ''.join(response.xpath("//dd[@class='job_bt']/div/node()").extract())
        print(response.meta['positionId'])
        item = LagouItem()
        item['positionId'] = response.meta['positionId']
        item['description'] = description
        yield item

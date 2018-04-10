# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LagouItem(scrapy.Item):
    city = scrapy.Field() #城市
    companyFullName = scrapy.Field() #公司全称
    companyId = scrapy.Field() #公司id
    companyLabelList = scrapy.Field() #公司标签
    companyShortName = scrapy.Field() #公司简称
    companySize = scrapy.Field()  #公司人数
    createTime = scrapy.Field() #创建时间
    district = scrapy.Field()   #地区
    education = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    imState = scrapy.Field()
    industryField = scrapy.Field()
    industryLables = scrapy.Field()
    jobNature = scrapy.Field()
    lastLogin = scrapy.Field()
    latitude = scrapy.Field()
    linestaion = scrapy.Field()
    longitude = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionId = scrapy.Field()
    positionLables = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()
    publisherId = scrapy.Field()
    secondType = scrapy.Field()
    stationname = scrapy.Field()
    subwayline = scrapy.Field()
    workYear = scrapy.Field()

    description = scrapy.Field()

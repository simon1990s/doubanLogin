# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/accounts/login']

    # 重写start_requests方法
    def start_requests(self):
        # 将请求参数封装到字典
        data = {
            'source': 'index_nav',
            'form_email': '18896541085',
            'form_password': 'jianer8023sun.'
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    # 针对个人主页页面数据进行解析操作
    def parseBySecondPage(self, response):
        fp = open('second.html', 'w', encoding='utf-8')
        fp.write(response.text)

        # 可以对当前用户的个人主页页面数据进行指定解析操作

    def parse(self, response):
        # 登录成功后的页面数据进行存储
        fp = open('main.html', 'w', encoding='utf-8')
        fp.write(response.text)

        # 获取当前用户的个人主页
        url = 'https://www.douban.com/people/70079801/'
        yield scrapy.Request(url=url, callback=self.parseBySecondPage)

import scrapy  # scrapy版本2.62, python版本3.8.13
import sys
import re
import os
from datetime import datetime, timedelta
from scrapy.utils.project import get_project_settings

# 下面报红色没有关系， 编译器的路径识别有点问题
from weibo.utils import util
from weibo.items import WeiboItem




class WeiboSearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['weibo.com']
    settings = get_project_settings()
    keyword_list = settings.get('KEYWORD_LIST')

    base_url = 'https://s.weibo.com/'

    # 获取设置的起始和结束的日期， 如果没有设置该选项，将用现在的时间代替
    start_date = settings.get('START_DATE', datetime.now().strftime('%Y-%m-%d'))
    end_date = settings.get('END_DATE', datetime.now().strftime('%Y-%m-%d'))
    # 之后可能会需要增加判断日期是否正确的语句

    # 设置页面比较的值，可以从45到50之间实验，观察哪个值会使程序抓的更多
    page_compare = settings.get('PAGE_COMPARE', 46)

    # 暂时只能通过list的方式来进行来添加关键词, 后面会通过txt的方式来进行添加
    if not isinstance(keyword_list, list):
        if not os.path.isabs(keyword_list):
            keyword_list = os.getcwd() + os.sep + keyword_list
        if not os.path.isfile(keyword_list):
            sys.exit('不存在%s文件' % keyword_list)
        keyword_list = util.get_keyword_list(keyword_list)

    def start_requests(self):
        for keyword in self.keyword_list:
            keyword_url = (self.base_url + 'weibo?q=%s') % keyword
            url = keyword_url + '&timescope=custom:{}:{}'.format(self.start_date, self.end_date)
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 meta={
                                     'base_url':  keyword_url,
                                     'keyword': keyword
                                 })

    def parse(self, response, *args):
        base_url = response.meta.get('base_url')
        keyword = response.meta.get('base_url')

        is_empty = response.xpath(
            '//div[@class="card card-no-result s-pt20b40"]')
        page_count = len(response.xpath('//ul[@class="s-scroll"]/li'))

        if is_empty:
            print('没有关键词的相关内容')

        if self.page_compare > 0:  # 暂时只让其抓50页
            for weibo in self.parse_weibo(response):
                print(weibo)
            next_url = response.xpath('//a[@class="next"]/@href').get()
            if next_url:
                next_url = self.base_url + next_url

    def parse_weibo(self, response):
        keyword = response.meta.get('keyword')
        # 获得一页的博文的信息
        blogs = response.xpath('//div[@action-type="feed_list_item" and @class="card-wrap"]')
        for every_blog in blogs:
            # 定义存储数据的字典
            weibo = WeiboItem()
            # 获取博文的文字内容
            text_raw = every_blog.xpath('.//div[@class="card"]//p[@class="txt"]').get()
            text = re.sub('<.*?>', '', text_raw).replace('\u200b', '').replace(
                '\ue627', '').strip()  # 后期可能考虑换成re.compile
            # text = re.sub('\\w*?', '', text)
            social_info = every_blog.xpath('.//div[@class="card-act"]')

            # 这里使用'string(.)'的原因是得到的转发数字是有多级嵌套标签，这样能够直接提取到数字
            reposts_count = social_info.xpath('.//ul/li[1]/a').xpath('string(.)').get().strip()
            if reposts_count == '转发':
                reposts_count = 0
            else:
                reposts_count = int(reposts_count)
            weibo['reposts_count'] = reposts_count
            comments_count = social_info.xpath('.//ul/li[2]/a').xpath('string(.)').get().strip()
            if comments_count == '评论':
                comments_count = 0
            else:
                comments_count = int(comments_count)
            weibo['comments_count'] = comments_count
            attitudes_count = social_info.xpath('.//ul/li[3]/a').xpath('string(.)').get().strip()
            if attitudes_count == '赞':
                attitudes_count = 0
            else:
                attitudes_count = int(attitudes_count)
            weibo['attitudes_count'] = attitudes_count
            weibo['text'] = text
            yield weibo

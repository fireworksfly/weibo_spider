import scrapy # scrapy版本2.62, python版本3.8.13
import sys
import re
import os
from scrapy.utils.project import get_project_settings
from weibo.utils import util
BASE_URL = 'https://s.weibo.com/weibo?q=%s'


class WeiboSearchSpider(scrapy.Spider):
    name = 'weibo_search'
    allowed_domains = ['weibo.com']
    settings = get_project_settings()
    keyword_list = settings.get('KEYWORD_LIST')

    # 暂时只能通过list的方式来进行来添加关键词, 后面会通过txt的方式来进行添加
    if not isinstance(keyword_list, list):
        if not os.path.isabs(keyword_list):
            keyword_list = os.getcwd() + os.sep + keyword_list
        if not os.path.isfile(keyword_list):
            sys.exit('不存在%s文件' % keyword_list)
        keyword_list = util.get_keyword_list(keyword_list)

    def start_requests(self):
        for keyword in self.keyword_list:
            url = BASE_URL % keyword
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 meta={
                                     'base_url': BASE_URL,
                                     'keyword': keyword
                                 })

    def parse(self, response, *args):
        base_url = response.meta.get('base_url')
        keyword = response.meta.get('base_url')
        # 获得一页的博文的信息
        blogs = response.xpath('//div[@action-type="feed_list_item" and @class="card-wrap"]')
        for every_blog in blogs:
            # 获取博文的文字内容
            content = every_blog.xpath('.//div[@class="card"]//p[@class="txt"]').get()
            content_filter = re.sub('<.*?>', '', content).strip()   # 后期可能考虑换成re.compile
            social_info = every_blog.xpath('.//div[@class="card-act"]')
            repost = social_info.xpath('.//ul/li[1]/a').xpath('string(.)').get().strip()
            if repost == '转发':
                repost = 0
            comment = social_info.xpath('.//ul/li[2]/a').xpath('string(.)').get().strip()
            if comment == '评论':
                comment = 0
            like = social_info.xpath('.//ul/li[3]/a').xpath('string(.)').get().strip()
            if like == '赞':
                like = 0
            print(content_filter)
            print('转发：', repost)
            print('评论：', comment)
            print('点赞：', like)
            print('#############################')


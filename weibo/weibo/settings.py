# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'

DEFAULT_REQUEST_HEADERS = {

    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 ",
    "Cookie": 'SINAGLOBAL=6680457046308.304.1662132659025; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhmbK51ne4MvVyncpuMV5Y-5JpX5KMhUgL.Foq01hz41K.Xehe2dJLoI7fKMs8EINSsdG._Mc_4; PC_TOKEN=01853dcd07; ALF=1679312729; SSOLoginState=1676720730; SCF=AiwrpbAOmZ8gs5e3aAt0FgekBOCWtgjpWUD1Ik4zmoEuaJzcXqgVlLkHCHDf8Ozv2PqQNq45oToRlCvoUb9DtwE.; SUB=_2A25O9MoKDeRhGeBN41AY-SfIyz-IHXVtg7zCrDV8PUNbmtAGLWfRkW9NRDwJDoQETVbv1BNXGJvibjpInF9k14g4; _s_tentry=login.sina.com.cn; Apache=4091242875055.7715.1676720732966; ULV=1676720732981:10:2:1:4091242875055.7715.1676720732966:1675314758482; webim_unReadCount=%7B%22time%22%3A1676720745511%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A37%2C%22msgbox%22%3A0%7D'

}
# 需要搜索的关键词
KEYWORD_LIST = ['许嵩']
# KEYWORD_LIST = 'E:\code\weibo_spider\关键词.txt'

# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2023-02-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2023-02-02'

# 从45到50之间选择，哪个抓的数据多选择哪个
PAGE_COMPARE = 46


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 这个参数记得给个false不然在
COOKIES_ENABLED = False

LOG_LEVEL = "WARNING"
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': 543,
    # 'weibo.middlewares.UserAgentMiddleware': 500
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'weibo.pipelines.WeiboPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

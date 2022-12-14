# Scrapy settings for wangModel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangModel'

SPIDER_MODULES = ['wangModel.spiders']
NEWSPIDER_MODULE = 'wangModel.spiders'
DOWNLOAD_DELAY = 3  #下载延迟3秒
DOWNLOAD_TIMEOUT = 60 #超时下载
#请求头列表

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
#请求头列表
USER_AGENT_LIST=[
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE/13.0.2256.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19041',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',

   "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Trident/6.0)",
   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2752.40 Safari/537.36",
   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; WOW64; Trident/5.0)",
   "Mozilla/5.0 (Windows NT 5.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
]
# Obey robots.txt rules
# ROBOTSTXT_OBEY = False
PROXY_LIST=[
   {"ip_port":"49.87.250.13:4325"},
   {"ip_port":"114.106.173.42:4313"},
   {"ip_port":"115.239.16.241:4314"},
   {"ip_port":"183.165.249.249:4310"},
   {"ip_port":"182.128.45.57:4315"},
   {"ip_port":"183.154.221.57:4356"},
   {"ip_port":"114.233.169.249:4313"},
   {"ip_port":"124.161.212.165:4358"},
   {"ip_port":"114.239.29.114:4345"},
   {"ip_port":"220.201.85.63:4331"},
   {"ip_port":"113.243.33.56:4343"},
   {"ip_port":"113.65.125.60:4386"},
   {"ip_port":"114.103.89.96:4354"},
   {"ip_port":"115.209.123.141:4326"},
   {"ip_port":"42.56.3.70:4361"},


]

URLLENGTH_LIMIT = 5000  #设置请求url最大长度
HTTPERROR_ALLOWED_CODES = [521]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wangModel.middlewares.WangmodelSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'wangModel.middlewares.RandowProxy': 543,  #随机代理中间件
   'wangModel.middlewares.RandowSpiderMiddleware': 543, #随机请求头中间件
   'wangModel.middlewares.RandomDelayMiddleware': 150, #设置延时
}
custom_settings = {
        "RANDOM_DELAY": 3,
        "DOWNLOADER_MIDDLEWARES": {
            'wangModel.middlewares.RandomDelayMiddleware': 150, #设置延时
        }
    }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'wangModel.pipelines.tuniuHBasePipeline': 300,
   'wangModel.pipelines.DuplicatesPipeline': 280,
}
FEED_EXPORT_ENCODING='utf-8'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

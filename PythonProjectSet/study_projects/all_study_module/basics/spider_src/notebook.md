# CrawlSpider 全站数据爬取
CrawlSpider: 类 Spider的一个子类  
- 实现全站数据爬取 将某一个板块下面页码的所有数据进行爬取  
  - 基于 Spider 手动请求
  - 基于CrawlSpider  
- 使用  
  - 创建一个工程  
  - cd xxx  
  - 创建爬虫文件（CrawlSpider）   
    - scrapy genspider -t crawl 名称 网址
    - 加入我们新建了个爬虫文件 text.py文件
    - 导入了下面这两个类：from scrapy.linkextractors import LinkExtractor / from scrapy.spiders import CrawlSpider, Rule
    - rules:
      - Rule()函数： 规则解析器 将链接提取器提取到的链接进行指定规则（callback）的解析
      - LinkExtractor 链接提取器 —— 对链接进行提取（去起始url提取） 取出指定的链接
        - 根据指定的规则 —— allow参数 （正则表达式）
      - follow=true 和 follow = FALSE的区别： 如果为true：则点击下面页码的“下一页”

***

# 分布式爬虫

分布式：
  - 概念： 需要 搭建分布式集群 —— 多台电脑 让分布式集群对一组资源进行分布联合爬取、
  - 作用： 大大提升爬取数据的效率
  - 实现分布式爬虫
    - 安装一个scrapy-redis组件 pip install scrapy-redis
    - 原生的 scrapy 不能实现 分布式 要和scrapy-redis组合使用
    - 原生的scrapy —— 调度器不能共享 管道不可以共享
    - scrapy-redis： 给原生的scrapy提供可共享的管道和调度器
    - 实现流程：
      - 创建一个工程
      - 创建一个基于CrawlSpider的爬虫文件
      - 修改当前的爬虫文件 
        - from scrapy_redis.spiders import RedisCrawlSpider
        - 将start_urls和allowed_domains进行注释
        - start_urls将被redis_key = 'Quan' 替代 指可以被代替的调度器队列的名称 起始url可以放里面
        - 编写数据解析相关操作 将当前爬虫类的父类改为RedisCrawlSpider
        - 配置文件中添加管道类：
        ```python3
            # 可以被共享的管道 写进redis
            ITEM_PIPELINES = {
                'scrapy_redis.pipelines.RedisPipeline': 400,
            }
        
            # 指定调度器
            # 增加了一个去重容器类的配置 租用使用redis的set集合来存储请求的指纹数据
            # 从而实现请求去重的持久化操作
        
            # 指定调度器
            # 过滤器
            DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
        
            # 调度器
            # 队列
            SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
            # 可有可无 但是加上最好 如果某一台机器宕机了 开始后 从没有爬过的数据
            SCHEDULER_PERSIST = True 
            # 指定redis服务器
            REDIS_HOST = 'redis服务的ip地址'  # 写真正的ip地址 redis远程服务器的ip
            REDIS_PORT = 6379
        ```
        - redis相关配置
          - redis配置文件：
            - linux或者Mac：redis.conf
            - Windows下：redis.windows.conf
            - 打开配置文件 修改两个地方
              - bind 127.0.0.1 此行要注释掉
              - 关闭保护模式 protected-mode yes 中的yes改成no
            - 保存
          - 结合redis文件开启服务
            - redis-severe 配置文件 —— 启动
          - 启动客户端
            - redis-cli
        - 启动工程
          - 执行 scrapy runspider 爬虫源文件.py（首先要进入spiders目录）
        - 向调度器的队列中放一个起始url
          - 调度器的队列在redis的客户端中
            - lpush xxx(调度器名称) www.xxx.com
        - 最终爬取到的数据存在redis的proName:items 这个数据结构中

# 增量式爬虫

增量式爬虫
  - 监测网站数据更新情况 只会爬取网站最新更新出来的数据
  - start_url = 'https://www.4567kp.com/frim/index2-1.html'
  - 提供初始url
  - 基于spidercrawl获取其他链接
  - 基于Rule将其页码链接进行请求
  - 从每一个页码对应的的页面源码中解析出每一个电影详情页的url
  - 和兴_**检测电影详情页的url之前有没有被请求过**_
    - 将爬过的详情页的url存起来 -- 存到 redis的set数据结构
  - 对详情页的url发起请求 然后解析出电影的名称和简介
  - 持久化存储



单线程串行：

import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
}

urls = [
    'https://www.icourse163.org/course/BIT-268001?from=searchPage&outVendor=zw_mooc_pcssjg_',
    'https://www.icourse163.org/course/NKU-1205696807?from=searchPage&outVendor=zw_mooc_pcssjg_',
    'https://www.icourse163.org/course/NJU-1001571005?from=searchPage&outVendor=zw_mooc_pcssjg_'
]


def get_content(url: str = None) -> any:
    print('正在爬，别着急！！！')
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print(type(response.content))
        print(type(response))
        return response.content


def parse_content(content) -> None:
    print('响应数据的长度为： ', len(content))


def main() -> int:
    for url in urls:
        content = get_content(url)
        parse_content(content=content)
    return 0


if __name__ == '__main__':
    main()

scrapy框架

安装：
    pip install wheel (0.40.0)
    下载twisted http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    安装twisted pip install Twisted-*******.whl
    pip install pywin32
    pip install scrapy
创建工程：
    terminal 里面：scrapy startproject 工程名称
    创建工程 firstblood以后，会有目录结构：
    ScrapyFrame：最开始创建的scrapy文件项目集
        - __init__.py ====== 初始化文件
        - firstblood ====== 我们创建的工程文件
            - scrapy.cfg ====== 一个配置文件 姑且先不管
            - firstblood ====== 一个文件夹
                - __init__.py
                - items.py
                - middlewares.py
                - pipelines.py
                - setting.py ====== 放相关配置文件
                - spiders ====== 爬虫目录，爬虫文件夹 里面必须放置一个爬虫源文件
                    - __init__.py
    spiders文件夹：爬虫目录，爬虫文件夹 里面必须放置一个爬虫源文件
创建工程后，
    先cd 我们创建的工程目录 ，进入目录
    再在spiders子目录中创建一个爬虫源文件，只需要 scrapy genspider 文件名 起始url 即可
    于是 此时会创建一个 文件名.py 的文件 注意 "scrapy genspider 文件名 起始url" 只需要写文件名 不需要写.py
执行工程：
    - scrapy crawl 爬虫文件名（也就是scrapy genspider 文件名 起始url的文件名）
    打开 setting.py 将 ROBOTSTXT_OBEY = True 改为 False  不遵守robots协议
    另外 使用scrapy crawl 文件名 --nolog 不打印日志  # 不建议使用此方法
    在setting里面 任意位置加一行 LOG_LEVEL = 'ERROR'
    setting文件里面 USER-AGENT: UA伪装 必须做
持久化存储：
    - 基于终端指令 只可以将parse方法的返回值存储到本地文本文件中 并不可以存数据库
        - scrapy crawl embarrass -o test.csv  执行并且存储 后面必须加： -o 文件名
        - 只能存： 'json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle'
        - 好处 简洁 高效 便捷  简单
        - 坏处 局限性太大
    - 基于管道
        - 编码流程：
            - 数据解析 parse
            - item类中定义相关属性
                - 下面的是封装好的 只需要按照格式写
                - # define the fields for your item here like:
                - # name = scrapy.Field()
                - author = scrapy.Field()
                - content = scrapy.Field()
            - 解析的数据封装存储到item类型的对象 —— 手动实例化   items.py
            - 将item对象提交给管道 进行持久化存储 pipelines.py
            - 在管道类的process_item() 中将其接收到的item存储的对象进行存储
            - 在配置文件中开启管道 取消注释 ITEM_PIPELINES 300表示优先级 数值越小 优先级越高 类越早执行
        - 通用性强
        - 若要存到数据库？？？同时存到本地？？？ ——定义多个管道类
            - ITEM_PIPELINES = {"embarrassment.pipelines.EmbarrassmentPipeline": 300,
                                "embarrassment.pipelines.MySQLPipeLine": 301
              }
             - 在 爬虫文件里 提交一个item 那这个item 提交给哪个管道类呢？？？
                —— 先提交给优先级较高的一个（先执行的）
                *** 必须 : 先执行的管道类的process_item()必须 return item
                养成良好的习惯——每个管道类都执行 return item

        - 需要注意的细节：
            - 管道文件中的一个管道类对应的是将数据存到一种载体
            - 爬虫文件提交的item只会给管道文件中第一个被执行的管道类 需要process_item 函数中 return item


    - scrapy 基于 Spider的 全站数据爬取
        - 全站数据爬取——将网站某板块全部页码对应下的数据爬取
        - 爬图片
        - 手动复制url 不推荐
        - 自动手动请求发送:
            - yield scrapy.Request(url, call_back=self.parse) call_back专门用作数据解析

- 五大核心组件
    - 调度器 包括过滤器、队列 首先过滤器——去重 --》加入到队列中  从队列中调度请求对象给引擎
    - 引擎 将请求对象发给调度器
        - 数据流处理
        - 触发事务 -- 拿到不同的数据流 触发什么事务
    - 管道 持久化存储
    - 下载器 下载器从互联网下载数据 返回response 给引擎 twisted模块
    - 爬虫的开始 —— spider url-->解析产生其他url
        请求发送 生成请求对象 给引擎
        引擎把调度器送来的请求对象给下载器
        引擎给spider spider的parse方法拿到response 在parse方法解析后发给引擎 引擎发给管道存储
- 请求传参
    - 使用很广
    - 使用场景： 爬取解析的数据不在同一张页面中（深度爬取）
    - 怎么使用——例如 爬取BOSS直聘的岗位名称和岗位描述

- scrapy 图片爬取——ImagesPipeline
    - 和爬取字符串数据的区别：
        - 字符串——只需要基于xpath解析且提交管道存储即可
        - 图片——xpath解析出图片地址 单独对图片地址请求获取二进制地址
    - ImagePipeline:
        - 只需要将image的src属性值解析 提交到管道 管道就可以获取、存储
    - 使用： 爬取图片
        - 流程：
            - 首先 from scrapy.pipelines.images import ImagesPipeline  import scrapy
            - 自定义管道类——ImagesPipeLine(继承自ImagesPipeline)
            - 重写父类
            - 重写父类函数：
                """
                class ImagesPipeLine(ImagesPipeline):
                    # 重写父类方法
                    # 根据图片地址进行数据请求
                    def get_media_requests(self, item, info):
                        yield scrapy.Request(url=item['src'])

                    # 指定图片存储路径 request是手动发送的请求对象
                    def file_path(self, request, response=None, info=None):
                        image_name = request.url.split('/')[-1]
                        return image_name
                    
                    def item_completed(self, results, item, info):
                        return item  # 返回给下一个即将使用的管道类
                """
            - setting.py 加上 IMAGES_STORE = '../result' 文件保存目录

- 中间件
    - 下载中间件
        - 位于引擎和下载器之间
        - 作用 批量拦截整个工程的所有请求和响应
        - 拦截请求：
            - UA伪装 process_request
            - 代理IP process_exception
        - 拦截响应：
            - 篡改响应数据 、 响应对象
    - middlewares.py 中间件文件
        - class MiddleDownloaderMiddleware: 下载中间件
- 爬取网易新闻
    - 爬取内容： 标题 内容
    - 各大板块（国内 国际等）是静态的 而每个板块下面的名称是动态的  而每个新闻都是静态的
    - 要获取动态加载的页面数据 —— 下载中间件 将动态加载的页面数据加载出来
        - 修改process_response
            - middlewares 导入包 from scrapy.http import HtmlResponse
            """
                def process_response(self, request, response, spider):
                    # spider 表示爬虫对象
                    # 拦截五大板块的响应数据 对数据进行改动 改成符合需求的响应对象
                    # 本函数可以兰街到所有响应对象

                    # 挑选出指定的响应对象 进行改动 —— 通过url
                    if request.url in spider.module_url:
                        # 五大板块对应的响应对象
                        # 针对定位到的对象进行改动
                        # 实例化一个新的响应对象（动态加载出的） 替代旧的响应对象
                        new_response = HtmlResponse(url, body, encoding, request)
                        returnn new_response
                    return response
            """

data structure 数据结构
Linked list 链表
offset 偏移



### 爬虫学习

- 爬虫在法律中是不被禁止
- 具有违法风险
- 时常优化自己的程序 避免干扰被访问网站的运行
- 避免爬取涉及到个人隐私的时候，需要小心

一、 爬虫的分类
    1. 通用爬虫：
        1.1 抓取系统重要组成部分
        1.2 抓取的是互联网中的一整张的页面
    2. 聚焦爬虫
        2.1 建立在通用爬虫的基础之上
        2.2 抓取的是页面中特定的局部内容
    3. 增量式爬虫
        3.1 监测网站中数据更新的情况
        3.2 只会抓取网站中最行新更新的程序

二、 爬虫的矛与盾

三、 反爬机制
    1. 门户网站可以通过制定相关的策略或者技术手段，防止爬虫程序爬虫进行网站数据的爬取

四、 反反爬策略
    1. 爬虫程序可以通过制定相关的策略或者技术手段，破解门户网站的反爬策略，从而获取门户网站的信息

五、 robots.txt 协议
    君子协议，规定网站具有规定哪些网站信息可以被爬虫，哪些数据不可以被爬虫。
    查看网站哪些内容是可以被爬取的，哪些不可以被爬起的方法：在浏览器域名后面输入 /robots.txt

========================================================================================================================
一、 http协议
    1. 概念：服务器和客户端进行数据交互的一种形式

二、 常用请求头信息
    1. User-Agent:

三、 https协议

四、 加密方式


pycharm快捷键：
设置里面的一些常用设置：
    1. code completion 设置自动匹配的英文单词对大小写不敏感
快捷键：
    1. 变量搜索、替换 ctrl + F 、 Ctrl + R
    2. PEP8 代码自动排版 Ctrl + Alt + L
    3. Ctrl + B 或者 Ctrl + 鼠标左键点击 跳转到变量的声明以及方法的定义还有参数 Ctrl + Alt + 方向键左键跳回去
    4. 对象的扩展选择：Ctrl + W 选外层的变量或者语句都选中
    5. Ctrl + Shift + - 代码压缩（全部代码）  如果不是全部代码，那么是光标所在行的那个语句块（含有相同格式的语句，比如两行注释就是一个语句块，一个if 语句就是一个语句块）
    6. Ctrl + Shift + + 代码展开（全部代码）  如果不是全部代码，那么是光标所在行的那个语句块（含有相同格式的语句，比如两行注释就是一个语句块，一个if 语句就是一个语句块）
    7. 代码重塑： Ctrl + D 复制一行        Ctrl + Y  删除一行       shift + 方向键 ：上下移动代码### 比如说这条语句和上两条语句就是这样！！！
    8. 代码分块： Ctrl + Alt + Z### 比如说这条语句和上两条语句就是这样！！！
    9. 多行光标控制： Alt + 鼠标点击某一个或几个地方，同时修改### 比如说这条语句和上两条语句就是这样！！！
    10. Alt + Shift + 鼠标选中某一列区域，可以同时选中某一列及其相关的列
    11. 将代码块变成一个函数： 选中区域 -- 点击右键 -- Refactor -- Extract 其中有 变量Variable(Ctrl + Alt + V)、常量Constant(Ctrl + Alt + C)、
        域Field(Ctrl + Alt + F)、参数Parameter(Ctrl + Alt + P)、Method(Ctrl + Alt + M) 然后写上名字 还可以选中一个想要设置参数的变量，将其变成Parameter(Ctrl + Alt + P)
    12. 容错处理：Ctrl + Alt + Z（代码分块） 选中except或者其他的代码，可以做循环等    就是try except处理（异常处理）
    13.  运行： Ctrl + Shift + F10

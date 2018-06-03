#-------用户配置部分--------
aim_tieba = '填入目标贴吧' #目标贴吧
cookie = '''填入有管理权限的贴吧账户Cookie'''
thread_level_limit = 5 #删除楼主为这个等级以下的主题贴，不包括该等级
threading_num = 2 #爬取贴子与楼中楼分别开启的线程数，推荐2，数值越大速度越快，不推荐超过3，可能会带来未知错误或导致触发贴吧反爬机制
spider_sleeptime = 100/threading_num #爬取贴吧首页列表线程的休眠时间间隔，推荐为100/threading_num，若带宽充足可适当减小。如20秒
once_scan_num = 20 #扫描首页前几贴，推荐20
same_author_limit = [4,3]#第一个表示首页50贴中相同用户的容许最大贴数，第二个表示触发后删除几个（按回复数量从低到高排序删除）,不需要请设置为[50,0]
same_topic_limit = True #发现相似撞车主题并只留下回复数最多的
smiley_limit = 10 #超过这个表情数量删封，用于应对无意义刷表情 10以上为关闭
enable_login_model = False #默认关闭登陆模块，手动填写cookie，若启用请自行配制好 selenium
username = ''#输入用户名
password = ''#密码
#------------------------

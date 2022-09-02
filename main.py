# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/























#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time ：2022/8/19 10:20
@Auth ：小呆瓜
@File ：main.py
@IDE ：PyCharm
@Description：微信公众号发送消息主文件
"""


import requests
import random
from send_message import SendMessage
import time
import datetime
from datetime import timedelta

a = 0
TOUSER = ['o-kLm6OySXaJHztFPHmzMb9uobE4',     #peter
          'o-kLm6KvU4BSuxiKz3tEwszYrSzo',     #潮弟
          'o-kLm6AW-Q9V9wHFiZjBmH2E0koM',     #安儿子
          'o-kLm6NW13Og_V3fxfCqFWlEQDOo',     #锦城小黄  3
          'o-kLm6CNSyEvuWkXIhpBvOEJZM7g',     #男神     4
          'o-kLm6Kbbb1694nlt4nyrzRbOO9I',     #小不点   5
          'o-kLm6JMczPEg622U2NAdXHMX5D8',     #佟颖     6
          'o-kLm6JGIh7b6mrDij1rhtg-7CRw',     #老张
          'o-kLm6OCrDQjWaWcDwf32-JXDal0']     #测试



class Main(object):
    def __init__(self) -> None:
        """
        构造函数
        """
        pass


    def main(self) -> None:
        # 实例SendMessage
        qgy = ['不要有趣，要有用。',
               '灰飞灰落，你也倒下。',
               '一板一眼，就会滋生弱点。',
               '自立自主，总胜过俯首为奴。',
               '谎言不会伤人，真相才是快刀。',
               '胜出，意味着变强。',
               '自满，会孕育死亡。',
               '友善，是如此乏味。',
               '结果比宣言更有力。',
               '懦弱比懒惰更可怕。',
               '慈悲，是一种我无法承担的奢侈。',
               '效率，是成功的核心关键。',
               '等待，会带来丰厚的奖赏。',
               '精准，是唯一重要的标准。',
               '野心，需要事实的约束。',
               '暴力，是了结的手段。',
               '粗鲁，保证能换来极其难看的死亡。',
               '进化，胜过痛苦。',
               '自负，会让每个人都屈膝下跪。',
               '英雄，是最好不过的目标。',
               '平庸，就是所有邪恶的根本。',
               '优雅，永不过时。',
               '工业，永远不败。',
               '秩序，因我而存在。',
               '恐惧，磨快了每一把刀刃。',
               '世界既不黑也不白，而是一道精致的灰。',
               '不要去寻找那些你不想遇到的东西。',
               '值得做的事情，就是值得做对的事情。',
               '地基一旦腐朽，城墙也就长久不了了。',
               '只要耐心等待，裂缝总会出现的。',
               '成功与失败的分别在于适应能力的高低。',
               '窍门就是脑袋机灵手脚麻利。',
               '好的礼节要通过耐心来测试。',
               '机会只会眷顾等待的人。',
               '如果你没有目的，就什么也不做。',
               '法律需要维护，才能维护人民。',
               '识时务者为俊杰。',
               '后悔的苦果总比死亡的结局更容易接受。',
               '你的徒劳让人失望。',
               '人人都有自己的位置，忘乎所以就危险了。',
               '社会需要规范。',
               '自力更生的女性应该更加流行。',
               '权利的维持必须不计代价。',
               '致人死地和自寻死路可要分清楚了。',
               '假扮无辜真是浪费时间。',
               '要么打，要么跑，优柔寡断让人厌恶。',
               '那一招顶多算是中等水平。',
               '注意了，看清你要去的地方，提防你的周围。',
               '你得先看中你自己，否则别人就认为你一钱不值。',
               '为仆则忠，为主则殆，这便是道德。',
               '过往的残酷回忆不会随着年岁而消减。',
               '悔恨会磨平我们灵魂中的棱角。',
               '合适的话语胜过锋利的刀子。',
               '只有懦夫才会逃跑。',
               '如果生活还没能改变，那你已经失败了。',
               '如果你没有战斗的本领，那你也要有赴死的意识。',
               '如果你赢不了，就不要动手。',
               '我不玩游戏，我来定规则。',
               '定义你的不是武器本身，而是你使用它的方式。',
               '我们都有底线，而我也许已经越过了自己呢。',
               '这件事结束时，你也许会感谢我。',
               '孩子，希望你下次转身会有好运。',
               '精准与否就是屠宰和手术的区别。',
               '你得先看中自己，否则别人会当你一钱不值。',
               '金钱总是万能的，好工具总是属于钱包最厚的人。',
               '耐心不是一种品德，而是唯一的品德。']
        # print(len(qgy))
        sm = SendMessage(touser=TOUSER[a])
        # print(time.strftime('%H-%M-%S',time.localtime(time.time())))
        # 获取接口返回数据
        api = 'http://t.weather.itboy.net/api/weather/city/'  # API地址，必须配合城市代码使用
        city_code = '101270101'  #成都
            # '101270101'  # 进入https://where.heweather.com/index.html查询你的城市代码
        if a == 3:    #锦城小黄所在的城市
            city_code = '101270701'   #遂宁
        if a == 4:    #男神所在的城市
            city_code = '101090201'   #保定
        if a == 5:    #小不点所在的城市
            city_code = '101280901'   #肇庆
        if a == 6:    #佟颖所在的城市
            city_code = '101090501'   #唐山
        tqurl = api + city_code
        response = requests.get(tqurl)
        d = response.json()  # 将数据以json形式返回，这个d就是返回的json数据
        n = random.randint(0, len(qgy)-1)
        time = datetime.datetime.now() + timedelta(hours=8)
        json_data = {"city": d["cityInfo"]["parent"] + '省' + d["cityInfo"]["city"], #+ d["cityInfo"]["county"],#省市
                     "data": d["data"]["forecast"][0]["ymd"],  #日期
                     "time": time.strftime("%H:%M:%S"),  #当前时间
                     "updata_time": d["time"],                         #更新时间
                     "week": d["data"]["forecast"][0]["week"],         #星期
                     "weather_type": d["data"]["forecast"][0]["type"], #天气
                     "wendu_high": d["data"]["forecast"][0]["high"],   #最高温度
                     "wendu_low": d["data"]["forecast"][0]["low"],     #最低温度
                     "shidu": d["data"]["shidu"],                      #湿度
                     "pm25": str(d["data"]["pm25"]),                   #PM2.5
                     "pm10": str(d["data"]["pm10"]),                   #PM10
                     "quality": d["data"]["quality"],                  #天气质量
                     "fx": d["data"]["forecast"][0]["fx"],             #方向
                     "fl": d["data"]["forecast"][0]["fl"],             #风力
                     "ganmao": d["data"]["ganmao"],                    #感冒指数
                     "tips": d["data"]["forecast"][0]["notice"],       #温馨提示
                     "qgy": qgy[n]}                                    #胶泥坐人
        # 发送消息
        sm.send_message(json_data=json_data)




if __name__ == '__main__':
    main = Main()
    main.main()
    # access_token.a = access_token.a + 1
    for a in range(1,len(TOUSER)):
        # print(TOUSER[a])
        main = Main()
        main.main()

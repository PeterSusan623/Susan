#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time ：2022/8/19 10:20
@Auth ：小呆瓜
@File ：send_message.py
@IDE ：PyCharm
@Description：发送微信公众号消息
"""

import json
import requests

import send_message
from access_token import AccessToken


TOUSER = ['o-kLm6OySXaJHztFPHmzMb9uobE4',     #peter
          'o-kLm6KvU4BSuxiKz3tEwszYrSzo',     #潮弟
          'o-kLm6AW-Q9V9wHFiZjBmH2E0koM',     #安儿子
          'o-kLm6NW13Og_V3fxfCqFWlEQDOo',     #锦城小黄  3
          'o-kLm6CNSyEvuWkXIhpBvOEJZM7g',     #男神     4
          'o-kLm6Kbbb1694nlt4nyrzRbOO9I',     #小不点   5
          'o-kLm6JMczPEg622U2NAdXHMX5D8',     #佟颖     6
          'o-kLm6JGIh7b6mrDij1rhtg-7CRw',     #老张
          'o-kLm6Da1B1XcbrufuUWmaL4Zi84',     #香香
          'o-kLm6G4MaMuW7kVYgXGKrPMJhf8',     #绿道项目负责人
          'o-kLm6OCrDQjWaWcDwf32-JXDal0']     #测试


a = 0

class SendMessage(object):
    # print("a=",a)
    # 消息接收者
TOUSER = ['o-kLm6OySXaJHztFPHmzMb9uobE4',     #peter
          'o-kLm6KvU4BSuxiKz3tEwszYrSzo',     #潮弟
          'o-kLm6AW-Q9V9wHFiZjBmH2E0koM',     #安儿子
          'o-kLm6NW13Og_V3fxfCqFWlEQDOo',     #锦城小黄  3
          'o-kLm6CNSyEvuWkXIhpBvOEJZM7g',     #男神     4
          'o-kLm6Kbbb1694nlt4nyrzRbOO9I',     #小不点   5
          'o-kLm6JMczPEg622U2NAdXHMX5D8',     #佟颖     6
          'o-kLm6JGIh7b6mrDij1rhtg-7CRw',     #老张
          'o-kLm6Da1B1XcbrufuUWmaL4Zi84',     #香香
          'o-kLm6G4MaMuW7kVYgXGKrPMJhf8',     #绿道项目负责人
          'o-kLm6OCrDQjWaWcDwf32-JXDal0']     #测试

    # 消息模板id
    TEMPLATE_ID = 'i--KZsfRnhuLqKclGnAJoSyfrFlPwxAa1wyksPBAwF0'
    # 点击跳转链接（可无）
    CLICK_URL = ' '
    len(TOUSER)
    # for n in range (0,len(TOUSER)):
    # print(TOUSER[send_message.a])

    def __init__(self, touser=TOUSER[send_message.a], template_id=TEMPLATE_ID, click_url=CLICK_URL) -> None:
        print("touser=",touser)
        """
        构造函数
        :param touser: o-kLm6OCrDQjWaWcDwf32-JXDal0
        :param template_id: s73nSdvXO5wOAOYiDAIO4IfvqztCLq9rZUMeDBmruQc
        :param click_url: ' '
        """
        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id
        self.click_url = click_url


    def get_send_data(self, json_data) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": self.click_url,
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "city": {
                    "value": json_data["city"],
                    # 字体颜色
                    "color": "#FF0000"
                },
                "data": {
                    "value": json_data["data"],
                    "color": "#0000FF"
                },
                "time": {
                    "value": json_data["time"],
                    "color": "#FF00FF"
                },
                "updata_time": {
                    "value": json_data["updata_time"],
                    "color": "#8B008B"
                },
                "week": {
                    "value": json_data["week"],
                    "color": "#00BFFF"
                },
                "weather_type": {
                    "value": json_data["weather_type"],
                    "color": "#00FFFF"
                },
                "wendu_high": {
                    "value": json_data["wendu_high"],
                    "color": "#00FFFF"
                },
                "wendu_low": {
                    "value": json_data["wendu_low"],
                    "color": "#00FA9A"
                },
                "shidu": {
                    "value": json_data["shidu"],
                    "color": "#00FA9A"
                },
                "pm25": {
                    "value": json_data["pm25"],
                    "color": "#ADFF2F"
                },
                "pm10": {
                    "value": json_data["pm10"],
                    "color": "#FFFF00"
                },
                "quality": {
                    "value": json_data["quality"],
                    "color": "#F0E68C"
                },
                "fx": {
                    "value": json_data["fx"],
                    "color": "#DAA520"
                },
                "fl": {
                    "value": json_data["fl"],
                    "color": "#FFA500"
                },
                "ganmao": {
                    "value": json_data["ganmao"],
                    "color": "#FFA07A"
                },
                "tips": {
                    "value": json_data["tips"],
                    "color": "#800000"
                },
                "qgy": {
                    "value": json_data["qgy"],
                    "color": "#A9A9A9"
                }
            }
        }

    def send_message(self, json_data) -> None:
        """
        发送消息
        :param json_data: json数据
        :return:
        """
        # 模板消息请求地址
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()
        # 有关响应结果，我有整理成xml文档（官方全1833条），免费下载：https://download.csdn.net/download/sxdgy_/86263090
        if result["errcode"] == 0:
            print("消息发送成功")
            send_message.a = send_message.a + 1
        else:
           print(result)
        return send_message.a

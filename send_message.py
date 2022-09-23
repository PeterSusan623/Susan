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
          'o-kLm6EcQ7dYCZ73i5bDfFA8ytGk',     #周金平     
          'o-kLm6Kbbb1694nlt4nyrzRbOO9I',     #小不点   5
          'o-kLm6JMczPEg622U2NAdXHMX5D8',     #佟颖     6
          'o-kLm6MqCc-UPRjYGpEvk_tZMcOo',     #彝族姑娘  7
          'o-kLm6JA7oFY4vKqlPyFZZ8rnHuc',     #孙莉     8
          'o-kLm6DiU7LLDa53mnWzD6WaOVVk',     #蒋老板   9
          'o-kLm6IyW1gKeBHFECLyCVr3K6j4',     #抖音小董 10
          'o-kLm6JGIh7b6mrDij1rhtg-7CRw',     #老张
          'o-kLm6Da1B1XcbrufuUWmaL4Zi84',     #香香
          'o-kLm6G4MaMuW7kVYgXGKrPMJhf8',     #绿道项目负责人
          'o-kLm6GP1jz6rdnz5uDXpxIQD6yo',     #李雨珂
          'o-kLm6CmTKNl0otcTCm_AMM2ok_c',     #卓桑
          'o-kLm6Njl_v4tfFci1aa-8ADO0qQ',     #komorebi
          'o-kLm6OCrDQjWaWcDwf32-JXDal0',     #测试
          'o-kLm6OySXaJHztFPHmzMb9uobE4']     #peter     

a = 0
a = 0
s = 0
cg = 0
sb = 0
lb = []

class SendMessage(object):
    # print("a=",a)
    # 消息接收者
    TOUSER = ['o-kLm6OySXaJHztFPHmzMb9uobE4',     #peter
              'o-kLm6KvU4BSuxiKz3tEwszYrSzo',     #潮弟
              'o-kLm6AW-Q9V9wHFiZjBmH2E0koM',     #安儿子
              'o-kLm6NW13Og_V3fxfCqFWlEQDOo',     #锦城小黄  3
              'o-kLm6EcQ7dYCZ73i5bDfFA8ytGk',     #周金平     
              'o-kLm6Kbbb1694nlt4nyrzRbOO9I',     #小不点   5
              'o-kLm6JMczPEg622U2NAdXHMX5D8',     #佟颖     6
              'o-kLm6MqCc-UPRjYGpEvk_tZMcOo',     #彝族姑娘  7
              'o-kLm6JA7oFY4vKqlPyFZZ8rnHuc',     #孙莉     8
              'o-kLm6DiU7LLDa53mnWzD6WaOVVk',     #蒋老板   9
              'o-kLm6IyW1gKeBHFECLyCVr3K6j4',     #抖音小董 10
              'o-kLm6JGIh7b6mrDij1rhtg-7CRw',     #老张
              'o-kLm6Da1B1XcbrufuUWmaL4Zi84',     #香香
              'o-kLm6G4MaMuW7kVYgXGKrPMJhf8',     #绿道项目负责人
              'o-kLm6GP1jz6rdnz5uDXpxIQD6yo',     #李雨珂
              'o-kLm6CmTKNl0otcTCm_AMM2ok_c',     #卓桑
              'o-kLm6Njl_v4tfFci1aa-8ADO0qQ',     #komorebi
              'o-kLm6OCrDQjWaWcDwf32-JXDal0',     #测试
              'o-kLm6OySXaJHztFPHmzMb9uobE4']     #peter

    # 消息模板id
    TEMPLATE_ID = ['i--KZsfRnhuLqKclGnAJoSyfrFlPwxAa1wyksPBAwF0','XtRQo8LToHFSduhvegZWCjk-Gco1NOSOkg6LSEg_x6w']
    # 点击跳转链接（可无）
    CLICK_URL = 'https://m.baidu.com/sf?pd=life_compare_weather&openapi=1&dspName=iphone&from_sf=1&resource_id=4495&word=%E5%85%A8%E5%9B%BD%E5%A4%A9%E6%B0%94&title=%E7%9C%81%E5%B8%82%E5%A4%A9%E6%B0%94%E6%9F%A5%E8%AF%A2&srcid=4983&fromSite=pc'
    len(TOUSER)
    # for n in range (0,len(TOUSER)):
    # print(TOUSER[send_message.a])

    def __init__(self, touser=TOUSER[send_message.a], template_id=TEMPLATE_ID[send_message.s], click_url=CLICK_URL) -> None:
        # print("template_id =",template_id)
        # print("send_message.s = ", send_message.s)
        # print("send_message.a = ",send_message.a)
        # print("len(TOUSER) = ",len(TOUSER) - 1)
        if send_message.a == (len(TOUSER) - 1):
            template_id = 'XtRQo8LToHFSduhvegZWCjk-Gco1NOSOkg6LSEg_x6w'
        # print(template_id)
        # print("touser=",touser)
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
            send_message.cg = send_message.cg + 1
            if send_message.a == len(TOUSER) - 1:
                print("11111111111")
                send_message.s = send_message.s + 1
        else:

           print(result)
           print("消息发生失败")
           lb.append(TOUSER[send_message.a])
           send_message.a = send_message.a + 1
           send_message.sb = send_message.sb + 1
           if send_message.a == len(TOUSER) - 1:
               print("11111111111")
               send_message.s = send_message.s + 1
        return send_message.a,send_message.s,send_message.sb,send_message.cg,lb





        def get_send_datass(self, json_datas) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": 'https://github.com/PeterSusan623/Susan',
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "peter": {
                    "value": json_datas["peter"],
                    # 字体颜色
                    "color": "#FF0000"
                },
                "all": {
                    "value": json_datas["all"],
                    "color": "#0000FF"
                },
                "cg": {
                    "value": json_datas["cg"],
                    "color": "#FF00FF"
                },
                "sb": {
                    "value": json_datas["sb"],
                    "color": "#8B008B"
                }
            }
        }

        def send_messagess(self, json_datas) -> None:
            """
            发送消息
            :param json_data: json数据
            :return:
            """
            # 模板消息请求地址
            url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
            data = json.dumps(self.get_send_datass(json_datas))
            resp = requests.post(url, data=data)
            result = resp.json()
            if result["errcode"] == 0:
                print("消息发送成功")
            else:
                print(result)

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
import temp
from access_token import AccessToken







class SendMessage(object):
    # print("a=",a)
    # 消息接收者

    # 消息模板id
    TEMPLATE_ID = ['i--KZsfRnhuLqKclGnAJoSyfrFlPwxAa1wyksPBAwF0','XtRQo8LToHFSduhvegZWCjk-Gco1NOSOkg6LSEg_x6w']
    # 点击跳转链接（可无）
    CLICK_URL = 'https://m.baidu.com/sf?pd=life_compare_weather&openapi=1&dspName=iphone&from_sf=1&resource_id=4495&word=%E5%85%A8%E5%9B%BD%E5%A4%A9%E6%B0%94&title=%E7%9C%81%E5%B8%82%E5%A4%A9%E6%B0%94%E6%9F%A5%E8%AF%A2&srcid=4983&fromSite=pc'
    # for n in range (0,len(TOUSER)):
    # print(TOUSER[send_message.a])

    def __init__(self, touser=temp.TOUSER[temp.a], template_id=TEMPLATE_ID[temp.s], click_url=CLICK_URL) -> None:
        # print("template_id =",template_id)
        # print("send_message.s = ", send_message.s)
        # print("send_message.a = ",send_message.a)
        # print("len(TOUSER) = ",len(TOUSER) - 1)
        if temp.a == (len(temp.TOUSER) - 1):
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
            "topcolor": "#27B900",
            # json数据对应模板
            "data": {
                "city": {
                    "value": json_data["city"],
                    # 字体颜色
                    "color": "#27B900"
                },
                "data": {
                    "value": json_data["data"],
                    "color": "#27B900"
                },
                "time": {
                    "value": json_data["time"],
                    "color": "#27B900"
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
            temp.a = temp.a + 1
            temp.cg = temp.cg + 1
            if temp.a == len(temp.TOUSER) - 1:
                temp.s = temp.s + 1
        else:

           print(result)
           print("消息发生失败")
           temp.lb.append(temp.TOUSER[temp.a])
           temp.a = temp.a + 1
           temp.sb = temp.sb + 1
           if temp.a == len(temp.TOUSER) - 1:
               temp.s = temp.s + 1




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

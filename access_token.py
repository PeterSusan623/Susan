#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time ：2022/8/19 10:20
@Auth ：呆瓜
@File ：access_token.py
@IDE ：PyCharm
@Description：获取access_token
"""

import requests



class AccessToken(object):
    # 微信公众测试号账号（填写自己的）
    APPID = "wxdeaceb483cc60525"
    # 微信公众测试号密钥（填写自己的）
    APPSECRET = "0e6e63ef398d8987eca1525da7011b7d"

    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:
        """
        获取access_token凭证
        :return: access_token
        """
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)

"""
全局鉴权
"""
import requests
from flask import request

import config
from exception import MyServiceException

SOA_TOKEN_STR = "soa_token"


def query_token_by_remote(token):
    # 请求授权接口
    oauth_url = config.app_conf["oauth"]["url"]
    resp = requests.get(oauth_url, {
        "token": token
    })
    result = resp.json()
    if not result or len(result) < 1:
        raise MyServiceException("请求令牌查询失败, 请重新登录")


def do_auth():
    if SOA_TOKEN_STR not in request.headers:
        raise MyServiceException("未登录的请求")
    token = request.headers[SOA_TOKEN_STR]
    # url_root = request.url_root # 请求的根路径, 包含请求协议、域名、端口
    # TODO 这里可以优化性能
    query_token_by_remote(token)


def wrap_authentication():
    do_auth()

# -*- coding: utf-8 -*-

def createUrl(base_url, cnt):
    urls = []
    s = cnt
    interval = 1
    url = base_url + "&page=" + str(s + interval)
    return url



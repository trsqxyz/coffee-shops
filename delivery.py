#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import webbrowser

class Barista():
    def __init__(self):
        with open('README.md') as beans:
            shops = [shop.split(" ") for shop in beans.readlines() if shop[0] == '-']
            names = [" ".join(shop[1:-1]) for shop in shops]
            urls = [shop[-1].split('\n')[0] for shop in shops]
            self.shops = dict(zip(names, urls))
    def selects(self):
        url = random.choice(list(self.shops.values()))
        return webbrowser.open(url)

if __name__ == '__main__':
    b = Barista()
    b.selects()

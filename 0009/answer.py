#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def main():
    with open('index.html') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(soup.findAll('a'))


if __name__ == "__main__":
    main()

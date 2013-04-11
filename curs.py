#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json
import urllib
import time
from datetime import date, timedelta, datetime
import os
import logging

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

def get_exchange(the_date, currency):
    url = 'http://openapi.ro/api/exchange/%s.json?%s'
    formatted = the_date.strftime('%Y-%m-%d')
    full_url = url % (currency, urllib.urlencode({'date' : formatted}))
    return json.load(urllib.urlopen(full_url))


def download(file_name, start_date=None, end_date=None, currency=None):
    logging.info("-----------------")
    logging.info("inceput download pe %s" % date.today())
    try:
        exchange = json.load(open(file_name, 'r+'))
    except IOError:
        exchange = []
    if start_date is None:
        if len(exchange) == 0:
            start_date = date(2005, 1, 3)
        else:
            start_date = date.fromtimestamp(
                max(e[0] for e in exchange) / 1000)
    if end_date is None:
        end_date = date.today()
    if currency is None:
        currency = 'eur'

    new_vals = {}
    for d in daterange(start_date, end_date):
        logging.info(d)
        res = get_exchange(d, currency)
        timestamp = int(time.mktime(time.strptime(res['date'],
            "%Y-%m-%d"))) * 1000
        rate = float(res['rate'].replace(',', '.'))
        new_vals[timestamp] = rate
    exchange.extend(sorted((k, v) for (k, v) in new_vals.iteritems()))
    json.dump(exchange, open(file_name, 'w'))
    
def main():
    my_dir = os.path.dirname(__file__)
    if my_dir:
        os.chdir(my_dir)
    logging.basicConfig(filename='curs.log',level=logging.DEBUG)
    download(file_name='curs.json', currency='eur')
    return 0

if __name__ == '__main__':
    main()

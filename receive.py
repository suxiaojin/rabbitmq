# -*- coding: utf-8 -*-
__author__ = 'suxiaojin'
__date__ = '2019/7/25 0025 下午 16:08'
import pika
credentials=pika.PlainCredentials('sxj','7150231')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.55.165',port=5672,virtual_host='test',credentials=credentials))
channel=connection.channel()
channel.queue_declare(queue='hello')
print('[*] Waiting for message....')
def callback(ch,method,properties,body):
    print('[x] Receive %s' %(body,))
channel.basic_consume('hello',callback)
channel.start_consuming()

# -*- coding: utf-8 -*-
__author__ = 'suxiaojin'
__date__ = '2019/7/25 0025 下午 16:08'
import pika
credentials=pika.PlainCredentials('sxj','7150231')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.55.165',port=5672,virtual_host='test',credentials=credentials))
channel=connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body="你好！")
print("[x] Send messages")
connection.close()

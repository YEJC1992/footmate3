# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import csv
import pandas as pd
import numpy as np
import time
import os
class FoodmateScrapyPipeline(object):
    """ 
        功能：保存item数据 
    """
    
    def __init__(self):
        logging.info("FoodmateScrapyPipeline init...")
        self.jy_file = open('调味品.csv','a+',encoding='utf-8',newline='')
        self.header = ["产品分类","产品名称","被抽样企业名称","通报单位","抽检结果","通报时间","通报文号","规格","商标","生产企业名称","生产企业地址","被抽样企业名称","被抽样企业地址","通报单位","生产省份","通报时间","不合格原因","检测结果","标准/法规限值","措施","判定结果","备注","伙伴网链接","抽检层级","网站"]

        

    def process_item(self, item, spider):
        logging.info("FoodmateScrapyPipeline process_item...")
        csv_writer = csv.writer(self.jy_file)
        row = []
        for col in self.header:
            if col in item:
                row.append(item[col])
            else:
                row.append("")
        csv_writer.writerow(row)
        return item

    def close_spider(self, spider):
        logging.info("FoodmateScrapyPipeline close...")
        self.jy_file.close
        # time.sleep(5)
        # csvf = pd.read_csv('调味品.csv', encoding='utf-8')
        # if os.path.isfile('调味品.xlsx') == True:
        #     os.remove('调味品.xlsx')
        # time.sleep(1)
        # csvf.to_excel('调味品.xlsx', sheet_name='data')
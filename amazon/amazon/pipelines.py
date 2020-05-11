# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter

class AmazonPipeline(object):
    def __init__(self):
        self.fp = open('amazon.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,indent=4)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spide(self,spider):
        self.fp.close()
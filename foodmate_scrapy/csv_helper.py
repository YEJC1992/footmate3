import csv

    
def writeJiangYouTemplate():
    f = open('调味品-酱油.csv','w',encoding='utf-8',newline='')
    csv_writer = csv.writer(f)
    header = ["产品分类","产品名称","被抽样企业名称","通报单位","抽检结果","通报时间","通报文号","规格","商标","生产企业名称","生产企业地址","被抽样企业名称","被抽样企业地址","通报单位","生产省份","通报时间","不合格原因","检测结果","标准/法规限值","措施","判定结果","备注","伙伴网链接","抽检层级","网站"]
    csv_writer.writerow(header)
    f.close()

writeJiangYouTemplate()
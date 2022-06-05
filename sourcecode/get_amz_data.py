# -*- coding: utf-8 -*-
import ast
import bs4
import requests
import re
import xlwt
import datetime
import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import random
import time
from datetime import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
previous_time = "0"
def find_header():
    user_agent_pool=[ # User-Agent池
        # Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', # 2021.10
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', # 2021.11
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36', # 2021.12
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', # 2022.01
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36', # 2022.02
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36', # 2022.03
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    ]

    import random

    headers={}
    headers['User-Agent']=random.choice(user_agent_pool)
    headers["Cookie"] = "session-id=133-4501310-2921869; ubid-main=131-9836357-5834452; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=pre-register; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19045%7CMCMID%7C68646955416687569732127159353160900196%7CMCAAMLH-1646024969%7C7%7CMCAAMB-1646024969%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1645427369s%7CNONE%7CMCAID%7C30DC8A2F6B76D3AD-6000020BA9586794%7CvVersion%7C4.4.0; aws-target-visitor-id=1645420169059-984501.34_0; session-token=QtqxSZunlWCkb8mlUKc+7iLfa3UPCP+wqsTGyqN8t/qBPZmErmDEiTma/qLmT+py9mo5frn07mDjkUE9aoXCFpJI3JpxIzONUDSqH+OjoDJ8VArDp5s2eauoOKLDaSKIsZJGKJPItaXA2vpir04LkRiubpXdEkV00eR90dxArL5f6WBT64KsGDmrBtqrJBRS; csm-hit=tb:EBJA13JD6DHPEFPCRCHJ+s-85EAC7X7XNYYKPFPMFFM|1645760130351&t:1645760130351&adb:adblk_nodownlink: 10"
    return headers
# test: https://www.amazon.com/Carhartt-Cuffed-Beanie-Alabaster-Heather/dp/B08BG8JBCR/ref=zg_bs_2474937011_1/133-4501310-2921869?pd_rd_i=B08BGSTFDL&amp;psc=1
def get_good_info(good_id,good_url,good_level2_name):
    #print(good_id,";")
    headers_3 = find_header()
    max_retry = 0
    while (max_retry < 3):
        try:
            resp_2 = requests.get(good_url,headers=headers_3)
            cotent_2 = resp_2.text
            comment_list = []
            feature_list = []
            #return feature_list,comment_list,cotent_2
            f_name_re = re.compile('a-size-large product-title-word-break">([\s\S]*?)<')
            f_name = " ".join(f_name_re.findall(cotent_2)[0].split())
            f_ratings_re = re.compile('acrCustomerReviewText.*?>(.*?)rating')
            f_ratings = int("".join(f_ratings_re.findall(cotent_2)[0].split(",")))
            f_score_re = re.compile('<i class="a-icon a-icon-star a-star.*?"><span class="a-icon-alt">(.*?)out')
            f_score = float("".join(f_score_re.findall(cotent_2)[0].split(" ")))
            f_price_re = re.compile('a-price[\s\S]*?\$(.*?)<')
            f_price = float("".join(f_price_re.findall(cotent_2)[0].split(" ")))
            comment_re = re.compile('a-expander-content reviewText review-text-content a-expander-partial-collapse-content[\s\S]*?span>([\s\S]*?)<')
            comment = comment_re.findall(cotent_2)
            for i in comment:
                if i != "":
                    comment_list.append([good_id,good_level2_name,i])
            feature_list = [good_id,good_level2_name,f_name,f_ratings,f_score,f_price]
            return feature_list,comment_list,cotent_2
        except Exception:
            time.sleep(1)
        max_retry += 1
while(True):
    print("prepare to get data")
    sle_time = int(1)*60*30
    #time.sleep(sle_time)
    db_host_id = "host.docker.internal"
    db_name = "amazon_db"
    db_pass = "12345"
    db_owner = "postgres"

    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    now_time = time.strptime(now_time, "%Y-%m-%d %H:%M:%S")
    now_time = time.strftime("%Y/%m/%d %H:%M:%S", now_time)
    now_time = datetime.strptime(now_time, "%Y/%m/%d %H:%M:%S")
    print(now_time)

    ymdh_time = now_time.strftime('%Y-%m-%d-%H')
    print(ymdh_time)
    
    #control time
    if previous_time == ymdh_time:
        time.sleep(sle_time)
    else:
        previous_time = ymdh_time

    #url
    url_1 = "https://www.amazon.com/Best-Sellers-Clothing-Shoes-Jewelry-Mens-Fashion/zgbs/fashion/7147441011/ref=zg_bs_unv_fashion_2_1040658_1"
    headers_1={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    ,'Cookie':"session-id=133-4501310-2921869; ubid-main=131-9836357-5834452; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=pre-register; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19045%7CMCMID%7C68646955416687569732127159353160900196%7CMCAAMLH-1646024969%7C7%7CMCAAMB-1646024969%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1645427369s%7CNONE%7CMCAID%7C30DC8A2F6B76D3AD-6000020BA9586794%7CvVersion%7C4.4.0; aws-target-visitor-id=1645420169059-984501.34_0; skin=noskin; session-token=F/jeRlLeE95U64sN2w40thxf5LSUYp403xoLPxCk3mynDmWjBB1gl2pAYLbT2WH7fgnGJf/tPsi3GqHIYP+WM9taZoqIs35rcV6DxxJra8kErzVcn6Jjzei/opoIe7huBPIZoNvAAAKMUFAhycezJlo6RIgnAMh8+OqLwCei1upz0k0gigeS2XigUkMNUvRD; csm-hit=tb:s-TM6VJ0PHCN56EXQNR53H|1646184507480&t:1646184507750&adb:adblk_no"
    }
    url_prefix_1 = "https://www.amazon.com"
    resp_1 = requests.get(url_1,headers=headers_1)
    cotent_1 = resp_1.text
    re_con_1 = 'item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"><a href="(.*?)"'
    regex_start_1 = re.compile(re_con_1)
    re_content_1 = regex_start_1.findall(cotent_1)
    re_content_112 = [url_prefix_1+str(i) for i in re_content_1]
    re_content_112
    re_con_12 = 'item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"><a href=".*?>(.*?)<'
    regex_start_12 = re.compile(re_con_12)
    re_content_12 = regex_start_12.findall(cotent_1)
    re_content_121 = [str(i) for i in re_content_12]
    dict_first_level_ori = {}
    for i in range(len(re_content_112)):
        dict_first_level_ori[re_content_121[i]] = re_content_112[i]

    # choose 4
    dict_first_level = {}
    dict_first_level["Clothing"] = dict_first_level_ori["Clothing"]
    dict_first_level["Jewelry"] = dict_first_level_ori["Jewelry"]
    dict_first_level["Shoes"] = dict_first_level_ori["Shoes"]
    dict_first_level["Watches"] = dict_first_level_ori["Watches"]
    headers_2={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    ,'Cookie':"session-id=133-4501310-2921869; ubid-main=131-9836357-5834452; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=pre-register; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19045%7CMCMID%7C68646955416687569732127159353160900196%7CMCAAMLH-1646024969%7C7%7CMCAAMB-1646024969%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1645427369s%7CNONE%7CMCAID%7C30DC8A2F6B76D3AD-6000020BA9586794%7CvVersion%7C4.4.0; aws-target-visitor-id=1645420169059-984501.34_0; session-token=QtqxSZunlWCkb8mlUKc+7iLfa3UPCP+wqsTGyqN8t/qBPZmErmDEiTma/qLmT+py9mo5frn07mDjkUE9aoXCFpJI3JpxIzONUDSqH+OjoDJ8VArDp5s2eauoOKLDaSKIsZJGKJPItaXA2vpir04LkRiubpXdEkV00eR90dxArL5f6WBT64KsGDmrBtqrJBRS; csm-hit=tb:EBJA13JD6DHPEFPCRCHJ+s-85EAC7X7XNYYKPFPMFFM|1645760130351&t:1645760130351&adb:adblk_nodownlink: 10"
    }
    url_prefix_2 = "https://www.amazon.com"
    url_2 = dict_first_level["Clothing"]
    url_2_name = "Clothing"
    def get_leve2_good_url(url_2,url_2_name):
        resp_2 = requests.get(url_2,headers=headers_2)
        cotent_2 = resp_2.text
        re_con_2 = 'a class="a-link-normal" tabindex="-1".*?href="(.*?)"'
        regex_start_2 = re.compile(re_con_2)
        re_content_2 = regex_start_2.findall(cotent_2)
        re_content_2 = [url_prefix_2+str(i) for i in re_content_2] 
        return [url_2_name,re_content_2]
    # [[2levelname,[urls]]]
    level_2_good_name_urls = []
    for url_2_level in tqdm(list(dict_first_level.items())):
        level_2_good_name_urls.append(get_leve2_good_url(url_2_level[1],url_2_level[0]))
    # relist the list, [[name,url]]
    level_2_good_name_urls_relist = []
    good_id = 0
    for i in level_2_good_name_urls:
        temp_list = []
        for j in i[1]:
            good_id = good_id + 1
            temp_list.append([good_id,i[0],j])
        level_2_good_name_urls_relist += temp_list
    tmp_df = pd.DataFrame(level_2_good_name_urls_relist)
    tmp_df.columns = ["good_id","level2_name","url"]
    # get detailed infor
    feature_list_all = []
    comment_list_all = []
    error_list_all = []
    for i in tqdm(level_2_good_name_urls_relist[:]):
        try:
            feature_list,comment_list,a = get_good_info(i[0],i[2],i[1])
        except:
            error_list_all.append(i)
            continue
        feature_list_all.append(feature_list)
        comment_list_all += comment_list
    print(error_list_all)
    # turn to dataframe
    df_2 = pd.DataFrame(feature_list_all)
    df_2.columns = ["id","category","name","rating","score","price"]
    df_2["datetime"] = ymdh_time
    # turn to dataframe
    df_3 = pd.DataFrame(comment_list_all)
    df_3.columns = ["id","category","comment"]
    df_3["datetime"] = ymdh_time
    #print(df_3["comment"][0])
    # connect to the postgresql
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()
    # create table
    try:
        create_table = (
            """
        CREATE TABLE IF NOT EXISTS "amz_item" (
                        "db_id"   VARCHAR(255),
                        "item_id" VARCHAR(255),
                        "category" VARCHAR(255), 
                        "name" VARCHAR(255), 
                        "rating" DOUBLE PRECISION, 
                        "score" DOUBLE PRECISION, 
                        "price" DOUBLE PRECISION, 
                        "datetime" VARCHAR(255),  
                        PRIMARY KEY ("db_id") 
                    )
            """)
        cursor.execute(create_table)
        db_connection.commit()
    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
    # the style, [(),(),()]
    insert_list_item = []
    db_id_add = 0
    for row in df_2.iterrows():
        db_id_add += 1
        list_item = (ymdh_time+"-"+str(db_id_add),ymdh_time+"-"+str(row[1][0]),str(row[1][1]),
                     str(row[1][2]),float(row[1][3]),float(row[1][4]),float(row[1][5]),str(row[1][6]))
        insert_list_item.append(list_item)
    insert_list_item[0]
    # insert into postgre
    try:
        args =  ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8')
                        for i in insert_list_item)
        cursor.execute("INSERT INTO amz_item VALUES " + (args))
        db_connection.commit()

    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
    # create table
    try:
        create_table = (
            """
        CREATE TABLE IF NOT EXISTS "amz_comment" (
                        "db_id"   VARCHAR(255), 
                        "item_id" VARCHAR(255),
                        "category" VARCHAR(255), 
                        "comment" text,  
                        "datetime" VARCHAR(255),  
                        PRIMARY KEY ("db_id") 
                    )
            """)
        cursor.execute(create_table)
        db_connection.commit()
    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
    # the style, [(),(),()]
    insert_list_comment = []
    db_id_add = 0
    for row in df_3.iterrows():
        db_id_add += 1
        list_item = (ymdh_time+"-"+str(db_id_add),ymdh_time+"-"+str(row[1][0]),str(row[1][1]),
                     str(row[1][2]),str(row[1][3]))
        insert_list_comment.append(list_item)
    insert_list_comment[0]
    # insert into postgre
    try:
        args =  ','.join(cursor.mogrify("(%s,%s,%s,%s,%s)", i).decode('utf-8')
                        for i in insert_list_comment)
        cursor.execute("INSERT INTO amz_comment VALUES " + (args))
        db_connection.commit()

    except Exception as ex:
        print("errors:%s"%ex)
        db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
        cursor = db_connection.cursor()
    print("data is collected",ymdh_time)
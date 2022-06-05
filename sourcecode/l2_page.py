import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import pandas as pd
import numpy as np
import datetime
import re
#import nltk
import time
import tensorflow as tf
from tensorflow.keras import *
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from sklearn.preprocessing import *

def start_db():
    # set db_host
    db_host = "host.docker.internal"
    # connect to the postgresql
    db_connection = psycopg2.connect(host=db_host,dbname="amazon_db", user="postgres" , password="12345")
    return db_connection

def transfer_to_dict(tm_list):
    tm_index = 0
    tm_dict = {}
    for i in tm_list:
        tm_dict[str(tm_index)] = i
        tm_index += 1
    return tm_dict

def chart3456(l2_name):
    db_connection = start_db()
    #3456
    cursor = db_connection.cursor()
    # get data
    select_data = (
        """
            SELECT * FROM "amz_item";
        """)
    # create the table
    cursor.execute(select_data)
    result_1 = cursor.fetchall()
    # set dataframe
    df_1 = pd.DataFrame(result_1)
    df_1.columns = ["db_id","item_id","category","name","rating","score","price","datetime"]
    df_2 = df_1.copy()
    df_2 = df_2[df_2["category"] == l2_name].reset_index(drop=True)
    df_3 = df_2.copy()
    df_3_1 = df_3[df_3["datetime"] == df_3["datetime"].max()].reset_index(drop=True)
    chart3_sale = int(df_3_1["rating"].mean())
    chart4_score = round(df_3_1["score"].mean(),3)
    chart5_price = round(df_3_1["price"].mean(),3)
    chart6_amount = int(chart3_sale*chart5_price)
    return chart3_sale,chart4_score,chart5_price,chart6_amount

def chart2(l2_name):
    db_connection = start_db()
    # 2
    cursor = db_connection.cursor()
    # get data
    select_data = (
        """
            SELECT * FROM "amz_item";
        """)
    # create the table
    cursor.execute(select_data)
    result_1 = cursor.fetchall();
    # set dataframe
    df_1 = pd.DataFrame(result_1)
    df_1.columns = ["db_id","item_id","category","name","rating","score","price","datetime"]
    df_2 = df_1.copy()
    df_2 = df_2[df_2["category"] == l2_name].reset_index(drop=True)
    df_avg_sale_pie_1 =  df_2.copy()
    df_avg_sale_pie_1 = df_avg_sale_pie_1[df_avg_sale_pie_1["datetime"] == df_avg_sale_pie_1["datetime"].max()].reset_index(drop=True)
    df_avg_sale_pie_2 = df_avg_sale_pie_1.groupby(by=["name"],dropna=False)["rating"].mean().reset_index()
    df_avg_sale_pie_2["rating"] = df_avg_sale_pie_2["rating"].astype("int")
    df_avg_sale_pie_2 = df_avg_sale_pie_2.sort_values(by=["rating"],ascending=False).reset_index(drop=True)
    df_avg_sale_pie_2 = df_avg_sale_pie_2.iloc[:6]
    #df_avg_sale_pie_2["rating"] = round(df_avg_sale_pie_2["rating"]/df_avg_sale_pie_2["rating"].sum(),3)
    df_web_1 = []
    df_web_1_name = df_avg_sale_pie_2["name"].tolist()
    df_web_1_rating = df_avg_sale_pie_2["rating"].tolist()
    for i in range(len(df_web_1_name)):
        tmp_dict = {}
        tmp_dict["name"] = df_web_1_name[i]
        tmp_dict["value"] = df_web_1_rating[i]
        df_web_1.append(tmp_dict)
    chart_2_list_dict = transfer_to_dict(df_web_1)
    return chart_2_list_dict

def chart1(l2_name):
    db_connection = start_db()
    # 1
    cursor = db_connection.cursor()
    # get data
    select_data = (
        """
            SELECT * FROM "amz_item";
        """)
    # create the table
    cursor.execute(select_data)
    result_1 = cursor.fetchall();
    # set dataframe
    df_1 = pd.DataFrame(result_1)
    df_1.columns = ["db_id","item_id","category","name","rating","score","price","datetime"]
    df_2 = df_1.copy()
    df_2 = df_2[df_2["category"] == l2_name].reset_index(drop=True)
    df_sale_line_1 =  df_2.copy()
    df_sale_line_2 = df_sale_line_1.groupby(by=["datetime"],dropna=False)["rating"].mean().reset_index()
    df_sale_line_2["rating"] = df_sale_line_2["rating"].astype("int")
    chart1_datetime_dict = transfer_to_dict(df_sale_line_2["datetime"].tolist())
    chart1_rating_dict = transfer_to_dict(df_sale_line_2["rating"].tolist())
    tmp_list = df_sale_line_2["rating"].tolist()
    chart1_total_sm_dict = transfer_to_dict([200/(max(tmp_list)-min(tmp_list)/1.1)*(i-min(tmp_list)/1.1) for i in tmp_list])
    return chart1_datetime_dict,chart1_rating_dict,chart1_total_sm_dict

def chart8(l2_name):
    db_connection = start_db()
    # 1
    cursor = db_connection.cursor()
    # get data
    select_data = (
        """
            SELECT * FROM "amz_item";
        """)
    # create the table
    cursor.execute(select_data)
    result_1 = cursor.fetchall();
    # set dataframe
    df_1 = pd.DataFrame(result_1)
    df_1.columns = ["db_id","item_id","category","name","rating","score","price","datetime"]
    df_2 = df_1.copy()
    df_2 = df_2[df_2["category"] == l2_name].reset_index(drop=True)
    df_sale_line_1 =  df_2.copy()
    df_sale_line_2 = df_sale_line_1.groupby(by=["datetime"],dropna=False)["score"].mean().reset_index()
    df_sale_line_2["score"] = df_sale_line_2["score"].astype("float")
    df_sale_line_2["score"] = df_sale_line_2["score"].apply(lambda x:float(round(x,3)))
    chart8_datetime_dict = transfer_to_dict(df_sale_line_2["datetime"].tolist())
    chart8_rating_dict = transfer_to_dict(df_sale_line_2["score"].tolist())
    return chart8_datetime_dict,chart8_rating_dict


    # word require def 
def filter_text(x,type_list):
    from gensim import corpora, models
    comment_str = re.sub(r"[^a-zA-Z]", " ", x.lower())
    comment_list = nltk.pos_tag(nltk.word_tokenize(comment_str))
    new_comment_list = []
    for i in comment_list:
        if i[1] in type_list:
            if len(i[0])>2:
                new_comment_list.append(i[0])
    return new_comment_list

def LDA_model(words_list):
    from gensim import corpora, models
    dictionary = corpora.Dictionary(words_list)
    corpus = [dictionary.doc2bow(words) for words in words_list]
    lda_model = models.ldamodel.LdaModel(corpus=corpus, num_topics=2, id2word=dictionary, passes=10)
 
    return lda_model

def word_cloud(l2_name):
    from gensim import corpora, models
    type_list = ["NN","NNS","JJ"]
    db_connection = start_db()
    cursor = db_connection.cursor()
    # get data
    select_data = (
        """
            SELECT * FROM "amz_comment";
        """)
    # create the table
    cursor.execute(select_data)
    result_1 = cursor.fetchall()
    # set dataframe
    df_5 = pd.DataFrame(result_1)
    df_5.columns = ["db_id","item_id","category","comment","datetime"]
    df_5 = df_5[df_5["datetime"] == df_5["datetime"].max()].reset_index(drop=True)
    df_5 = df_5[df_5["category"] == l2_name].reset_index(drop=True)
    df_5["comment"] = df_5["comment"].apply(lambda x:filter_text(x,type_list))
    comment_list = df_5["comment"].tolist()
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    type_list = ["NN","NNS","JJ"]
    words_list = comment_list[:int(len(comment_list)/2)]   #notice change
    lda_model = LDA_model(words_list)
    words_list = lda_model.show_topic(0, 50)
    large_word_list = []
    for i in words_list:
        large_word_list.append((i[0],int(i[1]*1000000)))
    word_list = {}
    index_tmp = 0
    for i in large_word_list:
        temp_dict = {}
        temp_dict["name"]=i[0]
        temp_dict["value"]=i[1]
        word_list[str(index_tmp)]=temp_dict
        index_tmp+=1
    word_list = str(word_list)
    return word_list
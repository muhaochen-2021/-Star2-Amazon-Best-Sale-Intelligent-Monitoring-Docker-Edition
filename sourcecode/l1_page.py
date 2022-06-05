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

def chart3456():
    db_connection = start_db()
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
    df_avg_sale_pie_1 =  df_1.copy()
    df_avg_sale_pie_1 = df_avg_sale_pie_1[df_avg_sale_pie_1["datetime"] == df_avg_sale_pie_1["datetime"].max()].reset_index(drop=True)
    df_avg_sale_pie_2 = df_avg_sale_pie_1.groupby(by=["category"],dropna=False)["rating"].mean().reset_index()
    df_avg_sale_pie_2["rating"] = df_avg_sale_pie_2["rating"].astype("int")
    df_avg_sale_pie_2["percent"] = df_avg_sale_pie_2["rating"]/df_avg_sale_pie_2["rating"].sum()*100
    df_avg_sale_pie_2["percent"] = df_avg_sale_pie_2["percent"].astype("int")
    dict_sale = dict(zip(df_avg_sale_pie_2['category'],df_avg_sale_pie_2['rating']))
    dict_per = dict(zip(df_avg_sale_pie_2['category'],df_avg_sale_pie_2['percent']))

    return dict_sale,dict_per


def chart8():
    db_connection = start_db()
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
    df_avg_sale_pie_1 =  df_1.copy()
    df_avg_sale_pie_2 = df_avg_sale_pie_1[df_avg_sale_pie_1["datetime"] != df_avg_sale_pie_1["datetime"].max()].reset_index(drop=True)
    df_avg_sale_pie_1 = df_avg_sale_pie_1[df_avg_sale_pie_1["datetime"] == df_avg_sale_pie_1["datetime"].max()].reset_index(drop=True)
    df_avg_sale_pie_2 = df_avg_sale_pie_2[df_avg_sale_pie_2["datetime"] == df_avg_sale_pie_2["datetime"].max()].reset_index(drop=True)
    df_avg_sale_pie_3 = df_avg_sale_pie_2.groupby(by=["category"],dropna=False)["score"].mean().reset_index()
    df_avg_sale_pie_3["score"] = df_avg_sale_pie_3["score"].astype("float")
    df_avg_sale_pie_3["score"] = df_avg_sale_pie_3["score"].apply(lambda x:float(round(x,3)))
    pre_score = df_avg_sale_pie_3["score"].tolist()
    df_avg_sale_pie_4 = df_avg_sale_pie_1.groupby(by=["category"],dropna=False)["score"].mean().reset_index()
    df_avg_sale_pie_4["score"] = df_avg_sale_pie_4["score"].astype("float")
    df_avg_sale_pie_4["score"] = df_avg_sale_pie_4["score"].apply(lambda x:float(round(x,3)))
    cur_score = df_avg_sale_pie_4["score"].tolist()

    return pre_score,cur_score

def itemWrap_list():
    db_connection = start_db()
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
    df_sale_line_1 =  df_1.copy()
    df_sale_line_2 = df_sale_line_1.groupby(by=["datetime"],dropna=False)["rating"].sum().reset_index()
    df_sale_line_2["rating"] = df_sale_line_2["rating"].astype("int")
    df_sale_line_2["datetime"] = df_sale_line_2["datetime"].astype("str")
    df_sale_line_2 = df_sale_line_2.iloc[-13:,:].reset_index(drop=True)
    df_sale_line_2 = df_sale_line_2.reindex(index=df_sale_line_2.index[::-1]).reset_index(drop=True)
    total = df_sale_line_2["rating"].tolist()
    time_name =  df_sale_line_2["datetime"].tolist()
    total_small = [170/(max(total)-min(total)/1.1)*(i-min(total)/1.1) for i in total]
    return total,time_name,total_small



# word require def 
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

def word_cloud():
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
    result_1 = cursor.fetchall();
    # set dataframe
    df_5 = pd.DataFrame(result_1)
    df_5.columns = ["db_id","item_id","category","comment","datetime"]
    df_5 = df_5[df_5["datetime"] == df_5["datetime"].max()].reset_index(drop=True)
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


# predict
def transfer_to_dict(tm_list):
    tm_index = 0
    tm_dict = {}
    for i in tm_list:
        tm_dict[str(tm_index)] = i
        tm_index += 1
    return tm_dict

def to_sequences(data, seq_len):
    d = []
    for index in range(len(data) - seq_len):
        d.append(data[index: index + seq_len])
    return np.array(d)

def preprocess(data_raw, seq_len):
    data = to_sequences(data_raw, seq_len)
    num_train = -5
    X_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]
    X_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]
    return X_train, y_train, X_test, y_test


def predict():
    db_connection = start_db()
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
    df_sale_line_1 =  df_1.copy()
    df_sale_line_2 = df_sale_line_1.groupby(by=["datetime"],dropna=False)["rating"].sum().reset_index()
    df_sale_line_2["rating"] = df_sale_line_2["rating"].astype("int")
    # predict 
    scaler = MinMaxScaler()
    scaled_close_ori = df_sale_line_2["rating"].tolist()
    avg_item_1 = np.average(scaled_close_ori[-9:])
    avg_item_2 = np.average(scaled_close_ori[-8:])
    avg_item_3 = np.average(scaled_close_ori[-7:])
    avg_item_4 = np.average(scaled_close_ori[-6:])
    avg_item_5 = np.average(scaled_close_ori[-5:])
    scaled_close_ori = scaled_close_ori + [avg_item_1,avg_item_2,avg_item_3,avg_item_4,avg_item_5]
    scaled_close = np.array(scaled_close_ori).reshape([len(scaled_close_ori),1])
    scaled_close = scaler.fit_transform(scaled_close)
    scaled_close = scaled_close.reshape(-1, 1)
    SEQ_LEN = 10
    X_train, y_train, X_test, y_test =\
    preprocess(scaled_close, SEQ_LEN)
    WINDOW_SIZE = SEQ_LEN - 1
    model = keras.Sequential()
    model.add(keras.Input(shape=(WINDOW_SIZE,X_train.shape[-1])))
    model.add(LSTM(WINDOW_SIZE,dropout=0.2))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(30, activation='relu'))
    model.add(Dense(units=1, activation="linear"))
    BATCH_SIZE = 16
    model.compile(
        loss='mean_squared_error',
        optimizer='adam'
    )
    history = model.fit(
        X_train,
        y_train,
        epochs=80,   #notice change
        batch_size=BATCH_SIZE,
        shuffle=False,
        validation_split=0.1
    )
    y_hat = model.predict(X_test)
    y_test_inverse = scaler.inverse_transform(y_test)
    y_hat_inverse = scaler.inverse_transform(y_hat)
    df_list_1 = df_sale_line_2.copy()
    datetime_last = datetime.datetime.strptime(df_list_1["datetime"][len(df_list_1)-1], "%Y-%m-%d-%H")
    datetime_pre_list = [(datetime_last+ datetime.timedelta(hours=i+1)).strftime('%Y-%m-%d-%H') for i in range(5)]
    list_2 = []
    for i in range(len(datetime_pre_list)):
        list_2.append([datetime_pre_list[i],int(y_hat_inverse.tolist()[i][0])])
    df_list_2 = pd.DataFrame(list_2)
    df_list_2.columns = ["datetime","rating"]
    df_list_2 = df_list_1.append(df_list_2).reset_index(drop=True)
    df_list_2["type"] = "pre"
    df_list_1["type"] = "cur"
    df_list = [df_list_1,df_list_2]
    df_line = df_list.copy()
    dic_pred_time = transfer_to_dict(df_line[1]["datetime"].tolist())
    dic_pred_pre = transfer_to_dict(df_list_2["rating"].tolist())
    dic_pred_cur = transfer_to_dict(df_list_1["rating"].tolist())
    return dic_pred_time,dic_pred_pre,dic_pred_cur
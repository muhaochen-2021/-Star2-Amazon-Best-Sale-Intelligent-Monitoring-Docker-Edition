from flask import Flask, render_template
import l1_page
import l2_page

app = Flask(__name__)

@app.route('/')
def index():
    dict_sale,dict_per = l1_page.chart3456()
    pre_score,cur_score = l1_page.chart8()
    score_list = [pre_score,cur_score]
    total,time_name,total_small = l1_page.itemWrap_list()
    sale_13_list = [total,time_name,total_small]
    #word_list = l1_page.word_cloud()
    word_list=0
    dic_pred_time,dic_pred_pre,dic_pred_cur = l1_page.predict()
    #dic_pred_time = 0; dic_pred_pre = 0; dic_pred_cur = 0
    return render_template('index.html',dict_sale=dict_sale,dict_per=dict_per,score_list=score_list
                                        ,sale_13_list = sale_13_list,word_list=word_list
                                        ,dic_pred_time=dic_pred_time,dic_pred_pre=dic_pred_pre,dic_pred_cur=dic_pred_cur)

@app.route('/clothing')
def clothing():
    l2_name = "Clothing" 
    chart3_sale,chart4_score,chart5_price,chart6_amount = l2_page.chart3456(l2_name)
    chart_2_list_dict = l2_page.chart2(l2_name)
    chart1_datetime_dict,chart1_rating_dict,chart1_total_sm_dict = l2_page.chart1(l2_name)
    chart8_datetime_dict,chart8_rating_dict = l2_page.chart8(l2_name)
    #char_7_word_list = l2_page.word_cloud(l2_name)
    char_7_word_list = 0
    return render_template('clothing.html',l2_name=l2_name,chart3_sale=chart3_sale,chart4_score=chart4_score
                                            ,chart5_price=chart5_price,chart6_amount=chart6_amount
                                            ,chart_2_list_dict=chart_2_list_dict,chart1_datetime_dict=chart1_datetime_dict
                                            ,chart1_rating_dict=chart1_rating_dict,chart1_total_sm_dict=chart1_total_sm_dict
                                            ,chart8_datetime_dict=chart8_datetime_dict,chart8_rating_dict=chart8_rating_dict
                                            ,char_7_word_list=char_7_word_list)
@app.route('/jewelry')
def jewelry():
    l2_name = "Jewelry" 
    chart3_sale,chart4_score,chart5_price,chart6_amount = l2_page.chart3456(l2_name)
    chart_2_list_dict = l2_page.chart2(l2_name)
    chart1_datetime_dict,chart1_rating_dict,chart1_total_sm_dict = l2_page.chart1(l2_name)
    chart8_datetime_dict,chart8_rating_dict = l2_page.chart8(l2_name)
    #char_7_word_list = l2_page.word_cloud(l2_name)
    char_7_word_list = 0
    return render_template('jewelry.html',l2_name=l2_name,chart3_sale=chart3_sale,chart4_score=chart4_score
                                            ,chart5_price=chart5_price,chart6_amount=chart6_amount
                                            ,chart_2_list_dict=chart_2_list_dict,chart1_datetime_dict=chart1_datetime_dict
                                            ,chart1_rating_dict=chart1_rating_dict,chart1_total_sm_dict=chart1_total_sm_dict
                                            ,chart8_datetime_dict=chart8_datetime_dict,chart8_rating_dict=chart8_rating_dict
                                            ,char_7_word_list=char_7_word_list)
                                
@app.route('/shoes')
def shoes():
    l2_name = "Shoes" 
    chart3_sale,chart4_score,chart5_price,chart6_amount = l2_page.chart3456(l2_name)
    chart_2_list_dict = l2_page.chart2(l2_name)
    chart1_datetime_dict,chart1_rating_dict,chart1_total_sm_dict = l2_page.chart1(l2_name)
    chart8_datetime_dict,chart8_rating_dict = l2_page.chart8(l2_name)
    #char_7_word_list = l2_page.word_cloud(l2_name)
    char_7_word_list = 0
    return render_template('shoes.html',l2_name=l2_name,chart3_sale=chart3_sale,chart4_score=chart4_score
                                            ,chart5_price=chart5_price,chart6_amount=chart6_amount
                                            ,chart_2_list_dict=chart_2_list_dict,chart1_datetime_dict=chart1_datetime_dict
                                            ,chart1_rating_dict=chart1_rating_dict,chart1_total_sm_dict=chart1_total_sm_dict
                                            ,chart8_datetime_dict=chart8_datetime_dict,chart8_rating_dict=chart8_rating_dict
                                            ,char_7_word_list=char_7_word_list)

@app.route('/watches')
def watches():
    l2_name = "Watches" 
    chart3_sale,chart4_score,chart5_price,chart6_amount = l2_page.chart3456(l2_name)
    chart_2_list_dict = l2_page.chart2(l2_name)
    chart1_datetime_dict,chart1_rating_dict,chart1_total_sm_dict = l2_page.chart1(l2_name)
    chart8_datetime_dict,chart8_rating_dict = l2_page.chart8(l2_name)
    #char_7_word_list = l2_page.word_cloud(l2_name)
    char_7_word_list = 0
    return render_template('watches.html',l2_name=l2_name,chart3_sale=chart3_sale,chart4_score=chart4_score
                                            ,chart5_price=chart5_price,chart6_amount=chart6_amount
                                            ,chart_2_list_dict=chart_2_list_dict,chart1_datetime_dict=chart1_datetime_dict
                                            ,chart1_rating_dict=chart1_rating_dict,chart1_total_sm_dict=chart1_total_sm_dict
                                            ,chart8_datetime_dict=chart8_datetime_dict,chart8_rating_dict=chart8_rating_dict
                                            ,char_7_word_list=char_7_word_list)

if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0")




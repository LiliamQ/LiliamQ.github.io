from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import psycopg2
from pyecharts import options as opts
from pyecharts.charts import Map
import numpy as np 

#读取数据，存放如数组



#用存放的数据绘图并连接网页
def map_base():
    conn = psycopg2.connect(database="emgyplan", user="postgres", password="123456", host="127.0.0.1", port="5432")
    print("Opened database successfully")
    read_sql = "select pro_name, pro_num from poverty_alleviation;"
    insert_sql="insert into  poverty_alleviation values('100','where','0','0');"
    cur = conn.cursor()
    cur.execute(read_sql)
    rows = cur.fetchall()
    rows=np.array(rows)
    attri = rows[:,0]
    value = rows[:,1]
    print(attri)
    print(value)
    c = (
        Map()
        .set_global_opts(title_opts=opts.TitleOpts(title="中国各省份贫困县基础情况"))
        .add("", [list(z) for z in zip(attri,value)], maptype='china')
        .render(path="../templates/index.html")
    )
    

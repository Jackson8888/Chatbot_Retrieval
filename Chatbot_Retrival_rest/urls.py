#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: urls.py 
@desc: 接口url
@time: 2019/05/10 
"""


# ===============
#
#   apis 下面的路由
#
# ===============

from django.urls import path


from Chatbot_Retrival_rest.Api.QA.QA_server import qa_server

urlpatterns = [

    path('qa', qa_server), # 问答
]
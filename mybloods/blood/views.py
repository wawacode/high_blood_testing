from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from blood.serializers import BloodSerializer
# Create your views here
class BloodView(APIView):
    def get(self,request):
        return render(request,"form1.html")
    def post(self,request):
        #接收request.data中的前端数据，同时进行序列化
        myblood=BloodSerializer(data=request.data)
        #判断myblood的有效性s
        if myblood.is_valid():
            myblood.save()
            return Response(myblood.data)
        else:
            return Response({"result":"报错"})
def showpic(request):
    '''
    在网页上面输出的结果是一个数据分析报告
    一般数据分析报告需要的元素：
    1、数据分析目的（需求）
    2、数据来源
    3、分析方法
    4、分析结果
    前端完成
    :param request:
    :return:
    '''
    import pandas
    datas = pandas.read_csv("static/psm.csv")
    # 被测人群患高血压的人数
    ill_all = datas[datas["Hypertension"] == 1.0]["Hypertension"].count()
    # 被测人群总人数
    all = datas["Hypertension"].count()
    # 患病比率
    rate = round(ill_all / all, 2)
    # 未患病的比率
    unrate = 1 - rate
    from pyecharts.charts import Pie
    x = ["高血压患病率", "高血压未患病率"]
    y = [rate, unrate]
    pie = (
        Pie()
            .add("高血压患病比率图", [list(z) for z in zip(x, y)])
    )
    #pie.render("高血压患病率1.html")
    #在这里不直接渲染网页，而是渲染一个数据 render_embed()
    embed_code=pie.render_embed()
    print(type(embed_code))
    #把embed_code字符串类型中的echarts地址用replace方法替换一个地址，然后注意覆盖原变量
    embed_code=embed_code.replace("https://assets.pyecharts.org/assets/echarts.min.js",
                                  "https://cdn.bootcdn.net/ajax/libs/echarts/4.8.0/echarts.min.js")
    mypie={
        "newpie":embed_code
    }

    return render(request,"blood.html",mypie)
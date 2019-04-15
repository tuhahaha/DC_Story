import json    
import sys
import io
import re 
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')                                                                                     
CRfeaturelist=[
    ["釉色","青釉","绿釉","黄釉","黑釉","白釉","红釉","蓝釉","粉彩","珐琅彩","晶彩","结晶釉",
    "斗彩","古彩","墨彩","水点桃花","釉里红","料器珐琅","钧釉","青白釉","白釉黑彩","乳白",
    "金属釉","回青","浙料","浙青","平等青","石子青","石青","珠明料","苏麻离青",""],

    ["窑系","官窑","哥窑","钧窑","定窑","越窑","汝窑","磁州窑","吉州窑","耀州窑","龙泉窑",""],

    ["纹样","缠枝纹","卷草纹","忍冬纹","草龙纹","海水纹","雷纹","云纹","云雷纹","如意纹",
    "龙纹","莲花纹","莲瓣纹","宝相花纹","牡丹纹","扁菊花纹","百花纹","冰梅纹","木叶纹",
    "蕉叶纹","瓜果纹","三果纹","折枝纹","过枝纹","皮球花纹","婴戏纹",""],

    ["器型","蟠龙瓶","多管瓶","梅瓶","花口瓶","玉壶春瓶","宝月瓶","天球瓶","象腿瓶","胆式瓶",
    "橄榄瓶","蒜头瓶","棒槌瓶","纸槌瓶","油锤瓶","柳叶瓶","藏草瓶","转心瓶","净瓶","盘口瓶",
    "穿带瓶","瓜棱瓶","贯耳瓶","莱菔瓶","荸荠瓶","葫芦瓶","筋瓶","卷口瓶","弦纹瓶","双鱼瓶",
    "鹅颈瓶","鸡腿瓶","凤首瓶","六方瓶","宫碗","注碗","盏","茶船","斗笠碗","心碗","折腹碗 ",
    "卧足碗","孔明碗","净水碗","玉璧底碗","笠式碗","四出碗","葵口碗","盉碗","骰子碗","攒碗",
    "攒盘","高足盘","压手杯","羽觞","高士杯","三秋杯","爵杯","耳杯","高足杯","鸡缸杯","鸽形杯",
    "马蹄杯","铃铛杯","方斗杯瓜棱罐","折方罐","鸡心罐","天字罐","撞罐","月牙罐","冰梅罐",
    "蟋蟀罐","鼓式罐","苹果尊","鱼篓尊","石榴尊","太白尊","马蹄尊","络子尊","百尊","萝卜尊",
    "观音尊","牛头尊","双鱼","鼓钉洗","圆洗","单柄洗","葵瓣洗","委角洗","蔗段洗","莲花洗",
    "桃式洗","叶式洗",""],

    ["装饰工艺","刻花","镂空","镂雕","堆塑","堆贴","剔花","雕花","划花","印花","沥粉","堆花",
    "彩绘",""],

    ["部位","敞口","斂口","花口","直口","盤口","唇口","折沿","洗口","花口","菱花口","复口",
    "子口","龙耳","凤耳","蒙耳","贯耳","牺耳","戟耳","绳耳","鱼耳","鹦鹉耳","螭耳","鸠耳",
    "象耳","菊耳","如意耳","绶带耳","铺首耳","蝠衔磐耳","丰肩","溜肩","平肩","折肩","鼓腹",
    "圆鼓腹","直筒腹","扁圆腹","弧腹","折腹","斜直腹","垂腹","直流","曲流","鸭嘴流","实足",
    "柱形足","锥形足","兽形足","珠足","饼形足","卧足","高足","双圈足","蹄足",""]

] 




def main():
    counter=0
    pathroot=os.getcwd()
    filelist=os.listdir(pathroot)
    for fileitem in filelist :
        num=re.findall('^\d+',fileitem)
        if num :
            print(num[0])
            dirname=pathroot+"//"+str(fileitem)
            os.chdir(dirname)
            fr=open(fileitem+'.txt',encoding='utf-8')
            fw=open(fileitem+'feature.txt','w',encoding='utf-8')
            tx=fr.read()
            nofeature=writedownfeature(fw,tx)
            counter+=nofeature
    print("空数据共有"+str(counter)+"个")
    return 0



def writedownfeature (fw,crinfo):
    featureflag=1
    attnum=0
    anslist=[
        ["釉色"],["窑系"],["纹样"],["器型"],["装饰工艺"],["部位"]
    ]
    for attribute in CRfeaturelist :
        attrname=attribute[0]
        i=1
        while attribute[i] is not "" :
            ans=re.findall(attribute[i],crinfo)
            if ans :
                anslist[attnum].append(ans[0])
                featureflag=0
            i+=1
        json.dump(anslist[attnum],fw,ensure_ascii=False,indent=4)

        print(anslist[attnum])

        attnum+=1

    return featureflag



if __name__ == "__main__":
    main()
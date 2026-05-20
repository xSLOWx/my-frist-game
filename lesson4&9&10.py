import json
import random

secret = random.randint(0, 100)
CiShu=0

#清空/新建排行榜
def New_Ranking():
    with open("Ranking.json","w", encoding="utf-8") as f:
        json.dump([],f)

#排行榜添加
def Ranking_add():
    try:   
        with open("Ranking.json","r", encoding="utf-8") as f:
            i =json.load(f)
            i.append({"name":name,"CiShu":CiShu,"num":secret})
        with open("Ranking.json","w", encoding="utf-8") as f:
            json.dump(i,f,ensure_ascii=False,indent=4)
    
    except FileNotFoundError:
        print("文件不存在")
        New_Ranking()
        with open("Ranking.json","r", encoding="utf-8") as f:
            i =json.load(f)
            i.append({"name":name,"CiShu":CiShu,"num":secret})
        with open("Ranking.json","w", encoding="utf-8") as f:
            json.dump(i,f,ensure_ascii=False,indent=4)

if __name__ == "__main__":
    print("—————————————————————— 排行榜 ——————————————————————")
    print("————————————————————————————————————————————————————")
    try:
        with open("Ranking.json","r", encoding="utf-8") as f:
            i =json.load(f)
            k=1
            for j in i:
                print(f"———————第{k}名———————  {j["name"]}  ———次数：{j["CiShu"]} —————")
                print("————————————————————————————————————————————————————")
                k+=1
    except FileNotFoundError:
        New_Ranking()
        print("暂无……")
    while True:
        try:
            guess = int (input("猜猜神秘数字是多少？(0-100)"))
            if guess < 0 or guess > 100:
                print(f"请输入0—100的数字")
                continue
        except ValueError:
            print("请输入数字。")
            continue
        CiShu+=1
        if guess == secret:
            print(f"猜对了，真棒！")
            print(f"只用了{CiShu}次就猜对了，留下你的名字吧(拒绝请按Enter)：",end="")
            name=input("")
            if name=="":
                name=="神秘人"
            Ranking_add()
            break
        elif guess > secret:
            print(f"这个数字比神秘数字大")
        else:
            print(f"这个数字比神秘数字小")
# Classのコンストラクタ　詳細理解
class user_info:
    def __init__(self, name, birth, address):
        print("__init__はメソッドの宣言で、名前が特別なだけで他のメソッドと性質は同じです(異なる見解もあります)")
        self.name = "abc"
        self.birth = 0
        self.address = "xyz"


taro = user_info("taro", 1980, "tokyo")

print("生成されたインスタンス:", taro)
print("taro.name:"+taro.name)
print("taro.birth:"+str(taro.birth))
print("taro.address:"+taro.address)

# 子クラスにコントラクタを定義するとき、super関数を用いる　super().親のコンストラクタ
class Parent:
    parent_static_v = "親の静的変数"

    def __init__(self, parent_self_v="親インスタンス変数"):
        print("親のコンストラクタ")
        self.parent_self_v = parent_self_v

    def func_parent(self):
        print("親のメソッド")


class Child(Parent):
    child_static_v = "子の静的変数:この変数の初期値"

    def __init__(self, child_self_v="子のインスタンス変数"):
        super().__init__("親インスタンス変数")
        print("子のコンストラクタ")
        self.child_self_v = child_self_v

    def func_child(self):
        print("子のメソッド")


child = Child()
print(Parent.parent_static_v)
print(Child.child_static_v)
child.func_child()
child.func_parent()
print(child.child_static_v)
print(child.parent_static_v)
print(child.child_self_v)
print(child.parent_self_v)

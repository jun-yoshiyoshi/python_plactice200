# 承継
class Parent:
    parent_static_v = "親の静的変数:親の変数の初期値"

    def __init__(self, parent_self_v="親のインスタンス変数:"):
        print("親のコンストラクタ")
        self.parent_self_v = parent_self_v

    def func_parent(self):
        print("親のメソッド")


class Child(Parent):
    child_static_v = "子の静的変数:子の変数の初期値"

    def func_child(self):
        print("子のメソッド")


child = Child()
print(Parent.parent_static_v)
print(Child.child_static_v)
child.func_child()
child.func_parent()
print(child.child_static_v)
print(child.parent_static_v)
print(child.parent_self_v)

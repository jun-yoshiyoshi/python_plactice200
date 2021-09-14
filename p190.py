# キャッチした例外の丸投げ　raise

def fun1():
    try:
        raise Exception('error in fun1()')
    except:
        print("1: fun1 can' t handle this error")
        # 同じエラーを投げる
        raise


def fun2():
    try:
        print('2:call fun1')
        fun1()
        print('3: done')
    except Exception as e:
        print('4: catch error which happens in fun 1()')
        print(e)


fun2()

'''
関数fun2()はfun1()をその内部で呼び出しています。 
fun1()内部でエラーを発生させて自らexceptでそれを受け取っていますが、 
そのexceptの中でraiseをしています。 
こうすると同じエラーが再発生するので、実質的に「呼び出し元に処理を依頼する」ことになり ます。
一応 try/ exceptでエラーをハンドルしようとしたけれども「ここでは対処しきれないエラーなので、呼び出し元で例外処理をしてもらう」
というような場合で同じエラーを再度raiseします。
fun1()の中で再度raiseされたエラーをfun2()が受け取っているので、例外のメッセージがオリジナルのもののままになっています。
なお、例外を処理しきれない場合はraiseで同じものを再度発生させるのではなく別のエラーをraiseさせても構いません。
例えば適切なエラーメッセージに更新して再度raiseするというのはいいアイデアかもしれません。'''

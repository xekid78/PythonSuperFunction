# PythonSuperFunction
super()関数

## 処理
super()関数を使って親クラスの__init__()メソッドを利用する。

## コード
```
class Greeting(object):
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def __init__(self):
        super(Hello, self).__init__()

    def wahaha(self):
        print("WA HA HA HA")

hello = Hello()
hello.say_hello()
hello.wahaha()
```

## 出力結果  
```
hello paiza
WA HA HA HA
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |

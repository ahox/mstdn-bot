# mstdn-bot
マストドンのBOTだよ
## 使い方
### 1.BOTの登録
register.py を実行して登録したいインスタンスにBOTを登録します。

インスタンスは初期データでは friends.cafe となっています。変更したい場合は register.py 内で変更しましょう。

登録情報は clientcred.secret ファイルへ保存されます。

### 2.BOTのログイン
login.py を実行して登録したインスタンスにBOT用のアカウントでログインします。

ログイン情報は login.secret 内に YAML で記述します。

サンプルデータが login.sample.yaml にありますので mail と pass を自分のものに変更して login.secret という名前で保存しましょう。

インスタンスは初期データでは friends.cafe となっています。変更したい場合は login.py 内で変更しましょう。

ログイン情報は usercred.secret ファイルへ保存されます。

### 3.BOTでトゥートする

main.py を実行すると Hello world をトゥートします。

from mastodon import Mastodon

# マストドンインスタンスへボットを登録して、登録情報を clientcred.secret ファイルへ保存します。
# この処理はボット作成時に一度だけ実施します。
# 以降は登録情報を clientcred.secret から読み込むことでボットを利用可能です。
Mastodon.create_app(
    'mstdn-bot',
    api_base_url='https://friends.cafe',
    to_file='clientcred.secret'
)

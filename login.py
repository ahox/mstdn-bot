from ruamel import yaml
from mastodon import Mastodon

# メールアドレスとパスワードを用いてマストドンインスタンスにログインします。
# ログイン情報は usercred.secret へ保存されるため、毎回ログインする必要はありません。
mastodon = Mastodon(
    client_id='clientcred.secret',
    api_base_url='https://friends.cafe'
)
with open('login.secret', 'r') as stream:
    login_data = yaml.safe_load(stream)

mastodon.log_in(
    login_data['mail'],
    login_data['pass'],
    to_file='usercred.secret'
)

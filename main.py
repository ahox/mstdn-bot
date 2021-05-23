from mastodon import Mastodon

mastodon = Mastodon(
    access_token='usercred.secret',
    api_base_url='https://friends.cafe'
)
mastodon.toot('Hello world.')

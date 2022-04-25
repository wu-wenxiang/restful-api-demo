VERSION = '1.0.0'

PUBLIC_URLS = [
    ('GET', r'^/$'),
    ('GET', r'^/v\d+/?$'),
    ('POST', r'^/v\d+/tokens/?$'),
]

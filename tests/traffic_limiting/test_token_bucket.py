#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_token_bucket.py
@Time    :   2022/09/24 11:09:11
@Author  :   puffin jiang
@Version :   1.0
'''


import time

from traffic_limiting.token_bucket import TokenBucket


def test_token_bucket():
    token_bucket = TokenBucket(5, 3)
    tokens = 2
    assert token_bucket.get_token(2)
    time.sleep(1)
    assert token_bucket.get_token(4)
    assert not token_bucket.get_token(1)

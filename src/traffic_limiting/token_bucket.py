#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   token_bucket.py
@Time    :   2022/09/24 11:09:43
@Author  :   puffin jiang
@Version :   1.0
'''

import threading
import time


class TokenBucket(object):
    _lock = threading.Lock()

    def __init__(self, capacity=10, rate=1):
        """
            init default capacity and interval
        Args:
            capacity (int): capacity of the token bucket, default 10
            rate (float): speed of put the token every second
        """
        self._capacity = capacity
        self._token_amount = capacity
        self._rate = rate
        self._last_timestamp = time.time()

    def get_token(self, tokens=1):
        """        
        get token in token bucket
        Args:
            tokens (int): the number of token get from bucket

        Returns:
            boolean: 
        """
        with self._lock:
            current_time = time.time()
            # generate token amount
            generate_token = round(
                (current_time - self._last_timestamp) * self._rate)

            self._token_amount = min(
                self._capacity, self._token_amount + generate_token)
            self._last_timestamp = current_time
            if self._token_amount > tokens:
                self._token_amount -= tokens
                return True
        return False

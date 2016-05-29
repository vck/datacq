#!/usr/bin/python
"""
pustaka penghasil waktu terkini
"""

from time import strftime

def date_time():
    """
    @generate date based on current date
    04262016-135453 -->
    """
    timestamps = strftime("%m%d%Y-%H%M%S")
    return timestamps

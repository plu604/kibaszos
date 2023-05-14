# Used to store configuration settings for Flask and its extensions

import os

class DevelopmentConfig(object):
    SECRET_KEY = os.urandom(24) or "ioj78asd3vn43jjnsa89462hjkasdtzi25njkl243gv1kk,nbcxyg21985436"
    DEBUG = True

class ProductionConfig(object):
    SECRET_KEY = os.urandom(24) or "dh3o2hrtziu768iuo1vnm312njklhz32u1vghcvserlm1l23j1bptnkl23nj5l6"
    DEBUG = False
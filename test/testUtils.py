# -*- coding: utf-8 -*-

'''
Utilities for test
'''
import json
    
def get_config_paths():
    '''
    How to get the path of config.json in test directory, Use this. 
    '''
    import os.path
    paths = {}
    pathname = os.path.abspath("conf/channel.json")
    pathname = pathname.replace('test/', "")
    pathname = pathname.replace('test\\', "")
    paths['channel'] = pathname
    pathname = os.path.abspath("conf/snsapi.json")
    pathname = pathname.replace('test/', "")
    pathname = pathname.replace('test\\', "")
    paths['snsapi'] = pathname
    return paths

def get_channel(platform):
    paths = get_config_paths()
    with open(paths['channel']) as fp:
        channel = json.load(fp)
        
    for site in channel:
        if site['platform'] == platform:
            return site
        
    raise TestInitNoSuchPlatform(platform)

def clean_saved_token():
    import os,glob
    for f in glob.glob('*.token.save'):
        os.remove(f)

class TestInitError(Exception):
    """docstring for TestInitError"""
    def __init__(self):
        super(TestInitError, self).__init__()
    def __str__(self):
        print "Test init error. You may want to check your configs."

class TestInitNoSuchPlatform(TestInitError):
    def __init__(self, platform = None):
        self.platform = platform
    def __str__(self):
        if self.platform is not None:
            print "Test init error -- No such platform : %s. " \
            "Please check your channel.json config. " % self.platform
        

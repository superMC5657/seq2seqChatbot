from configparser import SafeConfigParser
import os

current_path = os.path.abspath(__file__)
now_cig = os.path.dirname(current_path)
conf_file = os.path.join(now_cig + "/seq2seq.ini")


def get_config(config_file=conf_file):
    parser = SafeConfigParser()
    parser.read(config_file, encoding='utf-8')
    # parser.read() ERROR:gbk codec, so I changed the def of parser.read
    # get the ints, floats and strings
    # _conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
    _conf_strings = [(key, str(value)) for key, value in parser.items('strings')]
    _conf_ints = [(key, int(value)) for key, value in parser.items('ints')]
    return dict(_conf_ints + _conf_strings)

import re


def extract_hashtags(text):
    regex = "#(\w+)"
    hashtag_list = re.findall(regex, text)
    return hashtag_list
from re import sub

def MentionLinkFilter(text):
    return sub(r"(?:\@|https?\://)\S+","", str(text)).lstrip()
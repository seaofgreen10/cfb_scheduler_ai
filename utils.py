import re



def remove_tags(text):
    tag_re = re.compile(r'<[^>]+>')
    return tag_re.sub('', text)
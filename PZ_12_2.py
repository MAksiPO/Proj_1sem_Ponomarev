import string
st = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

st = [x for x in st if x in string.ascii_lowercase]
print("".join(st))
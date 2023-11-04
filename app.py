import os


def xor(s):
    chars = '0123456789abcdef'
    arr = [i ^ 5 for i in s.encode()]
    result = ''
    for b in arr:
        result += chars[(b & 255) >> 4]
        result += chars[(b & 255) & 15]
    return result


def mobile_info(st):
    if len(st) > 6:
        st = st[:-(len(st) - 7)]
    elif len(st) < 6:
        return {"msg": "手机号有误"}
    with open(os.path.abspath('') + r"\手机号码归属地.txt", mode="r", encoding="gbk") as f:
        mobile = f.read()
        index = mobile.index(st)
        s = mobile[index:index + 50]
        s1 = s.split("\n")[0]
        s2 = s1.split("----")
        s3 = {"city": s2[2], "province": s2[1]}
    # print(s3)
    return s3



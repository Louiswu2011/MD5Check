import hashlib


class MD5NotMatch(Exception):
    pass


class SHA1NotMatch(Exception):
    pass


class BothNotMatch(Exception):
    pass

def check(origin, check):
    if origin == check:
        return True
    else:
        return False


def getmd5(file):
    md5 = hashlib.md5
    content = file.read()
    md5.update(content.encode('utf-8'))
    return md5.hexdigest()


def getsha1(file):
    sha1 = hashlib.sha1
    content = file.read()
    sha1.update(content.encode('utf-8'))
    return sha1.hexdigest()


def checkfile(file, targetmd5, targetsha1):
    md5stat = check(targetmd5, getmd5(file)) == True
    sha1stat = check(targetsha1, getsha1(file))
    if md5stat & sha1stat:
        return True
    elif md5stat == False & sha1stat == False:
        raise BothNotMatch
        return False
    elif not md5stat:
        raise MD5NotMatch
        return False
    elif not sha1stat:
        raise SHA1NotMatch
        return False
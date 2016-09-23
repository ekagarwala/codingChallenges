print ord('a')


inString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def incrementLetter(letter, n):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return chr((ord(letter) - 97 + n) % 26 + 97)
    else:
        return letter


def translate(inString, n):
    print ''.join([incrementLetter(x, n) for x in inString])


translate(inString, 2)

translate('map', 2)

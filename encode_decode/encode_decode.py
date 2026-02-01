import base64
import ast
from math import *
from lzma import compress, decompress
from secrets import randbelow

def safe_secret_int(n) :
    """generate a sefe random int betwenn [0 and n[ with the secrets package"""
    return randbelow(n)

def to_ascii(txt : str) :
    encoded = base64.b64encode(txt.encode('UTF-8'))
    return encoded.decode("ascii")

def to_utf_8(base64_txt : str) :
    decoded = base64.b64decode(base64_txt.encode('ascii'))
    return decoded.decode("UTF-8")

#old version
'''
/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AXtAihdAAUaCmNWCs/YaWrv2rQ7XLYqAtQ4wa+zuoIITlNejFT
nOXFuLuZ6ZeeWZSKYgFxkkWROrBaza4BFjCbpdrkSnZ1fA8wfKTDNWWGiG/+KEgqeEA68tU6bAib6VklqQj
hzoFMD3AtGcOKNaULmI0Lug+z6AKYtkOMPC34iabAjT2Pj+CDX/y0I1Ehw5ZJEAkTo6SyaXZHgC5wavnJVJ
6QdbrCZdF4ZFzWeP0ob+mWQIcFqnYKbiUJqTUleYO8+ITijcfjfVa2708sCNt2eY8s0YoffnmQJ9a7Im+Zr
H5VLbXOuiLkYc2VDMCNEFum+fcYfHqHGQTCkE0IkWWh98tLZnqw1CXiN7dj6tGwsCoqAGeR9FsGSukFhHD0
MeeGSdUB2mj1rwGD86EDIUmxjTtB8UnVf8X7MMXAy/KEmz/vRzpO2f1banJo2CddUGFdnIJ5HOsUTBXn1IF
KmA/glRKJV55V84iNqtjz2hb2IMQ8o6kmpC477k1Bf03AR5x1kDwEgTE3fjKrG6qb85FlYOt4HQe6ooQAQq
er9qjuMrTCVvG0iv1cszFcoYbABy8I3je5dLgD+VA2uwjpoMxrIED7WtOqhw7lv9Kdt4VBd/+RwKCmGIlfS
GYaJSrFnGrXKz3VtySS+LIa26lRYbJCrM+dknpV2e/yCkTLIfrDwPrUJjgRpkolGVOG5dwRT4CKUfBwKlXw
uIv3VTf5rJeGmEHN1hhNfBECo3s4OYABUMt1QdruF5AABxATuCwAAVfdZhrHEZ/sCAAAAAARZWg==
'''

def cc_B_encode(source: str, key: str, math_formula: str) -> str:
    """encode une chaîne de caractères grâce à une clé et une fonction mathématique"""
    assert "x" in math_formula, "La variable x doit être définie dans la formule mathématique"
    f = eval(f"lambda x: {math_formula}")
    
    # Encodage des caractères avec la formule
    encoded_nums = [int(round(f(ord(c)))) for c in source]
    
    # Chiffrement avec la clé
    encoded = ''.join(
        chr((ord(c) + ord(key[i % len(key)])) % 1114112)
        for i, c in enumerate(','.join(map(str, encoded_nums)))
    )
    
    return to_ascii(encoded)


def cc_B_decode(source: str, key: str, reversed_math_formula: str) -> str:
    """décode une chaîne de caractères grâce à une clé et une fonction mathématique"""
    source = to_utf_8(source)
    assert "x" in reversed_math_formula, "La variable x doit être définie dans la formule inversée"
    rf = eval(f"lambda x: {reversed_math_formula}")
    
    # Déchiffrement avec la clé
    decrypted = ''.join(
        chr(ord(c) - ord(key[i % len(key)]))
        for i, c in enumerate(source)
    )
    
    # Conversion en liste d'entiers
    nums = map(int, decrypted.split(','))
    
    # Application de la formule inversée
    return ''.join(
        chr(int(round(rf(1114112 + -n))) if n < 0 else int(round(rf(n))))
        for n in nums
    )

def compress_string(input_string: str, txt_format: str = "utf-8") -> str:
    compressed = compress(input_string.encode(txt_format))
    return base64.b64encode(compressed).decode(txt_format)

def decompress_string(encoded_string: str, txt_format: str = "utf-8") -> str:
    compressed = base64.b64decode(encoded_string.encode(txt_format))
    return decompress(compressed).decode(txt_format)




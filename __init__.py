#coding=utf-8
import sys

__author__ = 'trigged'

import xpermutations

t1 = [1, 2, 3]
t2 = ["a", "b", "c"]

charset = ["ba", "bo", "bi"]

charset = ["ba", "bo", "be", "bi", "bu", "bang", "beng", "bing", "bong", "pa", "po", "pe", "pi", "pu", "pang", "peng",
           "ping", "pong", "ma", "mo", "me", "mi", "mu", "mang", "meng", "ming", "mong", "fa", "fo", "fe", "fi", "fu",
           "fang", "feng", "fing", "fong", "da", "do", "de", "di", "du", "dang", "deng", "ding", "dong", "ta", "to", "te",
           "ti", "tu", "tang", "teng", "ting", "tong", "na", "no", "ne", "ni", "nu", "nang", "neng", "ning", "nong", "la",
           "lo", "le", "li", "lu", "lang", "leng", "ling", "long", "ga", "go", "ge", "gi", "gu", "gang", "geng", "ging",
           "gong", "ka", "ko", "ke", "ki", "ku", "kang", "keng", "king", "kong", "ha", "ho", "he", "hi", "hu", "hang",
           "heng", "hing", "hong", "ja", "jo", "je", "ji", "ju", "jang", "jeng", "jing", "jong", "qa", "qo", "qe", "qi",
           "qu", "qang", "qeng", "qing", "qong", "xa", "xo", "xe", "xi", "xu", "xang", "xeng", "xing", "xong", "zha", "zho",
           "zhe", "zhi", "zhu", "zhang", "zheng", "zhing", "zhong", "cha", "cho", "che", "chi", "chu", "chang", "cheng",
           "ching", "chong", "sha", "sho", "she", "shi", "shu", "shang", "sheng", "shing", "shong", "ra", "ro", "re", "ri",
           "ru", "rang", "reng", "ring", "rong", "za", "zo", "ze", "zi", "zu", "zang", "zeng", "zing", "zong", "ca", "co",
           "ce", "ci", "cu", "cang", "ceng", "cing", "cong", "sa", "so", "se", "si", "su", "sang", "seng", "sing", "song",
           "ya", "yo", "ye", "yi", "yu", "yang", "yeng", "ying", "yong", "wa", "wo", "we", "wi", "wu", "wang", "weng", "wing", "wong", ]


# print list(xpermutations.xpermutations(charset))
#
# print list()

def buildTask(max_url, length):
    count = 0
    urls = []
    for i in xpermutations.xcombinations(charset, length):
        urls.append("".join(i) + ".com")
        count += 1
        if count > max_url:
            yield urls
            urls = []
            count = 0





            # print sys.argv[1]
            # print sys.argv[2]
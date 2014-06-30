#coding=utf-8

import commands
import gevent
from gevent import monkey
monkey.patch_all()

__author__ = 'trigged'

first = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s", "y", "w"]

yunm = ["a", "o", "e", "i", "u", "ang", "eng", "ing", "ong"]


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


def generaChars():
    for i in first:
        for j in yunm:
            print '"' + i + j + '",',


def buildTask():
    urls = []
    for i in charset:
        for j in charset:
            url = i + j + ".com"
            urls.append(url)
        yield urls


# blender colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def ranTask(domain):
    url = domain
    out = commands.getoutput('whois %s' % url)
    if 'No match' in out:
        print url, " :", Colors.OKGREEN + "Available" + Colors.ENDC
    else:
        print url, " :", Colors.FAIL + "Taken" + Colors.ENDC


def main():
    for urls in buildTask():
        # print len(urls)
        task = [gevent.spawn(ranTask, url) for url in urls]
        gevent.joinall(task, timeout=10)



if __name__ == "__main__":
    main()
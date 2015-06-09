#coding=utf-8

import commands
import gevent
from gevent import monkey
monkey.patch_all()
import sys
import xpermutations


__author__ = 'trigged'

first = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s", "y", "w"]

yunm = ["a", "o", "e", "i", "u", "ang", "eng", "ing", "ong"]

charset = ['b', 'ba', 'bo', 'bai', 'bei', 'bao', 'ban', 'ben', 'bang',   'bi', 'bie', 'biao', 'bian',
             'bing', 'p', 'pa', 'po', 'pai', 'pao', 'pan', 'pen', 'pang', 'peng', 'pi',
           'piao', 'pian', 'pin', 'ping', 'm', 'ma', 'mo', 'me', 'mai', 'mao', 'mou', 'man', 'men', 'mang',
           'meng', 'mi', 'mie', 'miao',  'mian', 'min', 'ming', 'f', 'fa', 'fo', 'fei', 'fou', 'fan',
           'fen', 'fang', 'feng', 'da', 'de', 'dai', 'dei', 'dao', 'dou', 'dan', 'dang', 'deng', 'di',
           'die', 'diao', 'diu', 'dian', 'ding', 'dong', 't', 'ta', 'te', 'tai', 'tao', 'tou', 'tan',
           'tang', 'teng', 'ti', 'tie', 'tiao', 'tian', 'ting', 'tong', 'n', 'na', 'nai', 'nei', 'nao',
           'no', 'nen', 'nang', 'neng', 'ni', 'nie', 'niao', 'niu', 'nian', 'nin', 'niang', 'ning',
           'nong', 'l', 'la', 'le', 'lai', 'lei', 'lao', 'lou', 'lan', 'lang', 'leng', 'li', 'lia',
           'lie', 'liao', 'liu', 'lian', 'lin', 'liang', 'ling', 'long', 'g', 'ga', 'ge', 'gai',
           'gei', 'gao', 'gou', 'gan', 'gen', 'gang', 'geng', 'gong', 'k', 'ka', 'ke', 'kai', 'kou',
           'kan', 'ken', 'kang', 'keng', 'kong', 'h', 'ha', 'he', 'hai', 'hei', 'hao', 'hou', 'hen',
           'hang', 'heng', 'hong', 'j', 'ji', 'jia', 'jie', 'jiao', 'jiu', 'jian', 'jin', 'jiang', 'jing',
           'jiong', 'q', 'qi', 'qia', 'qie', 'qiao', 'qiu', 'qian', 'qin', 'qiang', 'qing', 'qiong', 'x',
           'xi', 'xia', 'xie', 'xiao', 'xiu', 'xian', 'xin', 'xiang', 'xing', 'xiong', 'zh', 'zha', 'zhe',
           'zhi', 'zhai', 'zhao', 'zhou', 'zhan', 'zhen', 'zhang', 'zheng', 'zhong', 'ch', 'cha', 'che',
           'chi', 'chai', 'chao', 'chou', 'chan', 'chen', 'chang', 'cheng', 'chong', 'sh', 'sha', 'she',
           'shi', 'shai', 'shao', 'shou', 'shan', 'shen', 'shang', 'sheng', 'r', 're', 'ri', 'rao', 'rou',
           'ran', 'ren', 'rang', 'reng', 'rong', 'z', 'za', 'ze', 'zi', 'zai', 'zao', 'zou', 'zang', 'zeng',
           'zong', 'c', 'ca', 'ce', 'ci', 'cai', 'cao', 'cou', 'can', 'cen', 'cang', 'ceng', 'cong', 's',
           'sa', 'se', 'si', 'sai', 'sao', 'sou', 'san', 'sen', 'sang', 'seng', 'song', 'y', 'ya', 'yao',
           'you', 'yan', 'yang', 'yu', 'ye', 'yue', 'yuan', 'yi', 'yin', 'yun', 'ying', 'yong', 'w', 'wa',
           'wo', 'wai', 'wei', 'wan', 'wen', 'wang', 'weng', 'server', 'api']

def generaChars():
    for i in first:
        for j in yunm:
            print '"' + i + j + '",',


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


# blender colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def runTask(domain):
    url = domain
    out = commands.getoutput('whois %s' % url)
    print out[:27],
    if 'No match' in out:
        print url, " :", Colors.OKGREEN + "Available" + Colors.ENDC
    else:
        print url, " :", Colors.FAIL + "Taken" + Colors.ENDC


def main():
    for urls in buildTask(int(1000), int(2)):
        print urls
        task = [gevent.spawn(runTask, url) for url in urls]
        gevent.joinall(task, timeout=10)


if __name__ == "__main__":
    main()
from optparse import OptionParser
from AndroidStatsParser import *
import os


def getDiffBatt(lines1, lines2, uid1, uid2):
    return getBattery(lines1, uid1) - getBattery(lines2, uid2)


def getDiffBattTrepn(lines1):
    return getBatteryTrepn(lines1) - 0


def getUIDs(lines1, lines2, appname):
    return getUID(lines1, appname), getUID(lines2, appname)


def getDiffNet(lines1, lines2, uid1, uid2):
    rx1, tx1 = getRxTx(lines1, uid1)
    rx2, tx2 = getRxTx(lines2, uid2)
    return rx1 - rx2, tx1 - tx2


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option("-a", "--filea", type="str", dest="inpath1", help="Stats file 1")
    parser.add_option("-b", "--fileb", type="str", dest="inpath2", help="Stats file 2")
    parser.add_option("-p", "--app", type="str", dest="app", help="App package name")
    (options, args) = parser.parse_args()

    options.inpath1 = os.path.abspath(options.inpath1)
    f1 = open(options.inpath1).readlines()
    f1 = [line.strip() for line in f1]

    options.inpath2 = os.path.abspath(options.inpath2)
    f2 = open(options.inpath2).readlines()
    f2 = [line.strip() for line in f2]

    uid1, uid2 = getUIDs(f1, f2, options.app)
    diffBat = getDiffBatt(f1, f2, uid1, uid2)
    diffNet = getDiffNet(f1, f2, uid1, uid2)

    print("Bat:{} Net:{}".format(diffBat, diffNet))

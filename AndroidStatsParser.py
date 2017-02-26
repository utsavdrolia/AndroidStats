from optparse import OptionParser
import os

DUMMY = 0
UID_POS = DUMMY + 1
AGG_TYPE_POS = UID_POS + 1
SECTION_POS = AGG_TYPE_POS + 1
APP_POS = SECTION_POS + 2
BAT_POS = SECTION_POS + 2
NETRX_POS = SECTION_POS + 3
NETTX_POS = SECTION_POS + 4

UID = 'uid'
PWI = 'pwi'
NET = 'nt'


def getUID(lines, appname):
    for line in lines:
        args = line.split(",")
        if args[SECTION_POS] == UID:
            if args[APP_POS] == appname:
                return args[4]


def getBattery(lines, uid):
    for line in lines:
        args = line.split(",")
        if args[UID_POS] == uid:
            if args[SECTION_POS] == PWI:
                return float(args[BAT_POS])
    return 0


def getBatteryTrepn(lines):
    flag = False
    for line in lines:
        if line.startswith("System Statistics"):
            flag = True
        if flag:
            args = line.split(",")
            if args[0] == "332":
                return float(args[3])/1000
    return 0


def getRxTx(lines, uid):
    for line in lines:
        args = line.split(",")
        if args[UID_POS] == uid:
            if args[SECTION_POS] == NET:
                return long(args[NETRX_POS]), long(args[NETTX_POS])

    return 0, 0


if __name__ == '__main__':
    parser = OptionParser()

    # parser.add_option("-i", "--input", type="str", dest="inpath", help="Stats file")
    parser.add_option("-b", "--binput", type="str", dest="batpath", help="Stats file")
    # parser.add_option("-a", "--app", type="str", dest="app", help="App package name")
    (options, args) = parser.parse_args()

    # options.inpath = os.path.abspath(options.inpath)
    options.batpath = os.path.abspath(options.batpath)
    # f = open(options.inpath).readlines()
    # f = [line.strip() for line in f]
    # uid = getUID(f, options.app)
    # print("UID:{}".format(uid))
    f = open(options.batpath).readlines()
    f = [line.strip() for line in f]
    bat = getBatteryTrepn(f)
    print("Battery:{}".format(bat))
    # netrx, nettx = getRxTx(f, uid)

    # print("Battery:{} mAh TX:{} bytes Rx:{} bytes".format(bat, nettx, netrx))

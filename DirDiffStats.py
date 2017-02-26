from optparse import OptionParser
import os
import DiffStats
from pprint import PrettyPrinter


def dirStats(dir1, dir2, app):
    stat_dict = {}
    inpath1 = os.path.abspath(dir1)
    inpath2 = os.path.abspath(dir2)

    set1 = set(os.listdir(inpath1))
    set2 = set(os.listdir(inpath2))

    if set1 == set2:
        for stat in set1:
            stat1 = inpath1 + os.sep + stat
            stat2 = inpath2 + os.sep + stat
            f1 = [line.strip() for line in open(stat1).readlines()]
            f2 = [line.strip() for line in open(stat2).readlines()]
            uid1, uid2 = DiffStats.getUIDs(f1, f2, app)
            stat_dict[stat] = {"bat": DiffStats.getDiffBatt(f1, f2, uid1, uid2),
                               "net": sum(DiffStats.getDiffNet(f1, f2, uid1, uid2))}

        return stat_dict.values()
    else:
        print("Directories contain different stats:{} {}".format(set1, set2))


def dirStatsTrepn(batdir1, netdir1, netdir2, app):
    stat_dict = {}
    netpath1 = os.path.abspath(netdir1)
    netpath2 = os.path.abspath(netdir2)
    batpath1 = os.path.abspath(batdir1)

    set1 = set(os.listdir(netpath1))
    set2 = set(os.listdir(netpath2))
    set3 = set(os.listdir(batpath1))

    if set1 == set2 == set3:
        for stat in set1:
            stat1 = netpath1 + os.sep + stat
            stat2 = netpath2 + os.sep + stat
            f1 = [line.strip() for line in open(stat1).readlines()]
            f2 = [line.strip() for line in open(stat2).readlines()]
            uid1, uid2 = DiffStats.getUIDs(f1, f2, app)
            net = sum(DiffStats.getDiffNet(f1, f2, uid1, uid2))

            stat1 = batpath1 + os.sep + stat
            f1 = [line.strip() for line in open(stat1).readlines()]
            stat_dict[stat] = {"bat": DiffStats.getDiffBattTrepn(f1),
                               "net": net}

        return stat_dict.values()
    else:
        print("Directories contain different stats:{} {}".format(set1, set2))


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option("-a", "--dira", type="str", dest="dir1", help="Stats dir 1")
    parser.add_option("-b", "--dirb", type="str", dest="dir2", help="Stats dir 2")
    parser.add_option("-p", "--app", type="str", dest="app", help="App package name")
    (options, args) = parser.parse_args()

    printer = PrettyPrinter()
    printer.pprint(dirStats(options.dir1, options.dir2, options.app))


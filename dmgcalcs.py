import math


def food_buffs(d):
    d["boss atk inc"] += 0.5 + 0.2
    d["crit rate"] += 0.5
    d["crit dmg"] += 0.3
    d["phy atk inc"] += 0.5
    d["mag atk inc"] += 0.5
    d["phy dmg inc"] += 0.3 + 0.2
    d["mag dmg inc"] += 0.3 + 0.2
    return d


def effective_mdc(d, argv, boss=None):
    mdc = d["max dmg inc"]

    if boss == None:
        return mdc

    # def ignore
    di1 = 1 - 0.15 * (d["node lvl"] >= 40)
    di2 = 1 - 0.25 * argv.ds4
    di3 = 1 - 0.02 * argv.ap
    di_total = math.floor(1000 * di1 * di2 * di3) / 1000
    reduction = 1 - boss["def"] * di_total
    return mdc * reduction


def calc_noncrit(d, argv, boss=None):
    noncrit = d["sd"]
    if d["phy atk"] > d["mag atk"]:
        noncrit *= d["phy atk"]
        noncrit *= 1 + d["phy dmg inc"] + (d["node lvl"] > 20) * 0.1
        noncrit *= 1 + d["phy atk inc"] + (boss != None) * d["sd"] * d["boss atk inc"]
    else:
        noncrit *= d["mag atk"]
        noncrit *= 1 + d["mag dmg inc"] + (d["node lvl"] > 20) * 0.1
        noncrit *= 1 + d["mag atk inc"] + (boss != None) * d["sd"] * d["boss atk inc"]

    noncrit *= 1 + d["final dmg"] + d["node lvl"] * 0.02
    mdc = effective_mdc(d, argv, boss)
    noncrit = min(noncrit, mdc)
    if boss == None:
        return int(noncrit)
    return int(noncrit) * (1 - max(boss["dr"] - argv.idr, 0))


def calc_crit(d, argv, boss=None):
    noncrit = calc_noncrit(d, argv, boss)
    mdc = effective_mdc(d, argv, boss)
    crit = noncrit * (1.2 + d["crit dmg"])
    return int(min(crit, mdc))


def calc_avg_dmg(d, argv, boss=None):
    d["sd"] = float(argv.sd)
    d["node lvl"] = int(argv.node)
    if argv.food:
        d = food_buffs(d)
    if argv.br:
        d["boss atk inc"] += 0.5

    cr = min(d["crit rate"], 1)
    if boss != None:
        cr = max(0, cr - boss["crit res"])
        cr = min(cr + d["crit atk"] / 1e4, 1)

    return int((1 - cr) * calc_noncrit(d, argv, boss) + cr * calc_crit(d, argv, boss))

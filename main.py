import sys, tabulate, argparse, pandas
from getstats import *
from bossvalues import *
from dmgcalcs import *


def main(argv):
    filenames = argv.char

    dmg_tab = {}
    for (i, f) in enumerate(filenames):
        dmg_tab[f] = []
        stats = get_stats(f)
        #! are these hyper stat values 20% for all classes?
        stats["final dmg"] += 0.2 * argv.sfd
        stats["crit dmg"] += 0.2 * argv.scd
        stats["boss atk inc"] += 0.2 * argv.sba
        for b in BOSSES:
            avg_dmg = calc_avg_dmg(stats, argv, boss=BOSSES[b])
            avg_dmg_formatted = format(avg_dmg, ",")
            if avg_dmg == effective_mdc(stats, argv, boss=BOSSES[b]):
                avg_dmg_formatted = "*" + avg_dmg_formatted
            dmg_tab[f].append(avg_dmg_formatted)

    print(tabulate.tabulate(dmg_tab, headers=filenames, showindex=BOSSES.keys(), stralign="right"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--char", help="character stats", nargs="+")
    parser.add_argument("-s", "--sd", help="skill damage", default=1.00)
    parser.add_argument("-n", "--node", help="node lvl", default=1)
    parser.add_argument("--sfd", help="hyper passive fd", action="store_true")
    parser.add_argument("--scd", help="hyper passive cd", action="store_true")
    parser.add_argument("--sba", help="hyper passive ba", action="store_true")
    parser.add_argument("--idr", help="ignore dmg reduction", default=0)
    parser.add_argument("-f", "--food", help="food buffs 50s and tangs", action="store_true")
    parser.add_argument("--br", help="boss rush", action="store_true")
    parser.add_argument("--ds4", help="defense smash 4", action="store_true")
    parser.add_argument("--ap", help="ark pendant", action="store_true")

    args = parser.parse_args()
    main(args)


# main(["llama_pa.png", "llama_cd.png"], sd=1.45, node=40, food=True)

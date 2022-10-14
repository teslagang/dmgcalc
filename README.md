# dmgcalc

Calculates damage output using screenshots of your character stat page.

# Current options
```
➜ python main.py -h                                                            
usage: main.py [-h] [-c CHAR [CHAR ...]] [-s SD] [-n NODE] [--sfd] [--scd] [--sba] [--idr IDR] [-f] [--br] [--ds4] [--ap]

options:
  -h, --help            show this help message and exit
  -c CHAR [CHAR ...], --char CHAR [CHAR ...]
                        character stats
  -s SD, --sd SD        skill damage
  -n NODE, --node NODE  node lvl
  --sfd                 hyper passive fd
  --scd                 hyper passive cd
  --sba                 hyper passive ba
  --idr IDR             ignore dmg reduction
  -f, --food            food buffs 50s and tangs
  --br                  boss rush
  --ds4                 defense smash 4
  --ap                  ark pendant
```

# Example usage
```
➜ python main.py -c llama_cd.png llama_pa.png --sd 1.7 --node 40 --sfd --scd -f
         llama_cd.png    llama_pa.png
-----  --------------  --------------
lotus       3,003,048       3,057,196
  Ark       5,714,127       5,678,474
  Mag       8,872,633       9,204,207
  SC6         978,516         989,755
  SC5       6,439,370       7,077,294
  SC4       9,282,840       9,891,003
  SC3      11,257,704      11,326,806
  SC2      12,401,124      12,441,993
  SC1     *12,731,899     *12,731,899
  CRA      11,978,807      12,012,865
   GD     *12,731,899     *12,731,899
   SF     *12,731,899     *12,731,899
   ```
   
# TODO
- buckshot cannonneer option applies -55% fd. maybe option --buckshot
- check if all hyper passive boosts give flat 20%
- verify damage reduction values for bosses
- do bosses have "crit dmg reduction" in addition to crit resist?
- add logic for paladin threaten and fever 
- for single file analysis, 
-- breakdown of what to improve?
-- hypotheticals? "-2 cd + 4 fd" will take current stats, adjust according to input, and report dmg into a new column?

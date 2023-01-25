import pandas as pd
import random

pokédex = pd.read_json('pokedex.json')
moves = pd.read_json('moves.json', lines=True)
learnset = pd.read_json('learnsets.json')

#print(learnset['bulbasaur'])
#print(pokédex.loc[0][1]['english'])
print(pokédex.loc[0][3]['HP'])
#print(moves['absorb'])

pokémon = []
p_moves = {}
HP = {}
Ty = []

#print(list(learnset['amoonguss']['learnset'])[1])

def start():
    for i in range(6):
        pokémon.append(pokédex.loc[random.randint(0,809)][1]['english'])
    print(pokémon)
    for i in range(6):
        p_moves[pokémon[i]] = []
        for j in range(4):
            p_moves[pokémon[i]].append(random.randint(0,len(learnset[pokémon[i].lower()]['learnset'])))
start()
def battle():
    print('What should',pokémon[0],'do?')
    print(' 1 Fight\n','2 Pokémon')
    action = int(input(''))
    if action == 1:
        for i in range(4):
            print(i+1,list(learnset[pokémon[0].lower()]['learnset'])[p_moves[list(p_moves)[0]][i]].capitalize())
    else:
        for i in range(6):
            print(i+1,pokémon[i])
battle()

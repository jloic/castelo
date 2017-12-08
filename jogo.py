#!/usr/bin/env python3.4
#-*- coding: utf8 -*-
import sys
import time
import random

MAX_ROW = 4
MAX_LINE = 4

class Enemy:
    def __init__(self, name, life, defense, attack):
        self.name = name
        self.life = life
        self.defense = defense
        self.attack = attack

class Fight:
    def __init__(self, enemy):
      #  self.player = player
        self.enemy = enemy

    def fight(self, player = None):
        self.player = player
        while 1:
            print("Você ataca.")

            time.sleep(1)
            if random.random() >= 0.2:
                print("Consegui o golpe ! ", self.enemy.name, " levou ", self.player.attack, " de danos !")
                damage = self.player.attack - self.enemy.defense
                if damage < 0:
                    damage = 0
                self.enemy.life -= damage
                print(self.enemy.name, ' esta com ', self.enemy.life, ' de vida.')
            else:
                print("O ", self.enemy.name, " esquivou o seu ataque :(")

            if self.enemy.life <= 0:
                print(self.enemy.name, " está morto, você ganhou !")
                return 0

            print(self.enemy.name, " ataca.")

            time.sleep(1)
            if random.random() >= 0.4:
                print("Ele acerta em você ! Você levou ", self.enemy.attack, " de danos !")
                damage = self.enemy.attack - self.player.defense
                if damage < 0:
                    damage = 0
                self.player.life -= damage
                print("Você esta com ", self.player.life, " de vida.")
            else:
                print("Você esquivou o ataque.")

            if self.player.life <= 0:
                print("Você está morto, você perdeu :(")
                return 1

            print("-- Continuar --")
            input()

def fight_enemy(name):
    enemy = Enemy(*MONSTERS[name])
    fight = Fight(enemy)
    return fight.fight


########## AQUI COMECA O JOGO

MONSTERS = {
"trex": ["T-Rex", 20, 1, 2],
"monster_frog": ["Sapinho monstro", 30, 2,5],
"snake":["Cobra dos hits", 40, 1, 8],
"three_head_dragon": ["Dragão de 3 cabeças", 50, 5, 2],
"gods_snake": ["Cobra dos deuses", 40, 1, 6],
"dragon" : ["Dragão", 30, 2, 6],
"king_dragon": ["Dragão Rei", 100, 8, 20],
"spikes_monster": ["Monstro de espinhos", 30, 8, 2]
}



def get_sword(player):
    print("Agora você pode dar +3 de danos.")
    player.attack += 3

def get_enchanted_sword(player):
    print("Agora você pode dar +10 de danos.")
    player.attack += 10

def get_shield(player):
    print("Agora você tem +3 de defesa.")
    player.defense += 3

def get_flaming_shield(player):
    print("Agora você tem +6 de defesa e +1 de dano")
    player.defense += 6
    player.attack += 1

def get_god_bracelet(player):
    print("Uma luz aparece no teto, você pega a pulseira e ganha +15 de ataque")
    player.attack += 15

def get_mega_sword(player):
    print("O chão se abre e num raio se levanta a mega espada ! Você tem +30 de danos")
    player.attack += 30

def get_lightning_shield(player):
    print("Na parede você encontra o Escudo dos Raios. Você tem +20 de defesa e +10 de ataque")
    player.defense += 20
    player.attack += 10

def get_life_potion(player):
    print("Você bebe o frasco e ganha +200 de vida")
    player.life += 200

def get_mini_life(player):
    print("Você bebe o frasco e ganha +30 de vida")
    player.life += 30

def get_protection_googles(player):
    print("Você coloca os oculos e fica com +3 de proteção")
    player.defense += 3

def get_gun(player):
    print("Você ganha +10 de ataque")
    player.attack += 10

room = {
        (0,0) : ["THE KING ESTA NESTA SALA ! TEMA-ME !!!!", fight_enemy('king_dragon')],
        (1,0) : ["Encontrou a pulseira dos deuses.", get_god_bracelet],
        (1,1) : ["... Tremores ...", get_mega_sword],
        (0,1) : ["A sala esta brilhando.", get_lightning_shield],
        (2,0) : ["PSSSSSSS !!!!!", fight_enemy('gods_snake')],
        (2,1) : ["Pica pica ...", fight_enemy('spikes_monster')],
        (3,1) : ["GRRRRR RRRRRRR R R R !", fight_enemy('trex')],
        (0,2) : ["UEBET UEBET !!!", fight_enemy('monster_frog')],
        (0,3) : ["Poção de vida !", get_life_potion],
        (1,3) : ["Vamos ver !", get_protection_googles],
        (2,3) : ["Uma mini-poção...", get_mini_life],
        (3,2) : ["Essa sala tem uma arminha !", get_gun],
        (1,2) : ["Pppissss ...", fight_enemy('snake')],
        (2,2) : ["3 cabeças ??!!", fight_enemy('three_head_dragon')]
        }

#### AQUI ACABA


class Player:
    def __init__(self):
        self.position = None
        self.life = 20
        self.attack = 1
        self.defense = 1
        self.visited = []
        pass

    def goto_room(self, position):
        self.position = position
        action = None
        if position in self.visited:
            print("Entrou numa sala que já visitou")
        else:
            self.visited.append(position)
            if position in room:
                print(position, " : " , room[position][0], end=' ')
                action = room[position][1]
            else:
                print("Entrou numa sala sombria .... ")


        if action is None:
            print(" [N, S, L, O] ? ")
        else:
            action(self)


    def play(self):
        self.goto_room((3, 3))
        while 1:
            next_action = input()
            position = self.position
            if next_action == 'N':
                position = (position[0], position[1]+1)
            elif next_action == 'S':
                position = (position[0], position[1] - 1)
            elif next_action == 'O':
                position = (position[0] - 1, position[1])
            elif next_action == 'L':
                position = (position[0] + 1, position[1])
            else:
                print("Não entendi !")
                continue

            if position[0] < 0 or position[0] >= MAX_ROW \
                    or position[1] < 0 or position[1] >= MAX_LINE:
                print("Você não pode ir nesta direção, tem uma parede !")
                self.goto_room(self.position)
                continue

            self.goto_room(position)

player = Player()
player.play()

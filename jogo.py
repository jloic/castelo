#-*- coding: utf8 -*-
import sys
import time
import random

MAX_ROW = 3
MAX_LINE = 3


def fight_trex(player):
    trex = Enemy('T-Rex', 20, 1, 2)
    fight = Fight(player, trex)
    fight.fight()

def fight_dragon(player):
    dragon = Enemy('Dragão', 30, 2, 6)
    fight = Fight(player, dragon)
    fight.fight()


def get_sword(player):
    print "Agora você pode dar +3 de danos."
    player.attack += 3

def get_shield(player):
    print "Agora você tem +3 de defesa."
    player.defense += 3

def get_enchanted_sword(player):
    print "Agora você pode dar +10 de danos."
    player.attack += 10

def get_shield(player):
    print "Agora você tem +3 de defesa."
    player.defense += 3

def get_flaming_shield(player):
    print "Agora você tem +6 de defesa e +1 de dano"
    player.defense += 6
    player.attack += 1



room = {
        (1,1) : ["Essa sala contem uma espada. Parabéns !", get_sword],
        (0,1) : ["Essa sala contem uma espada encantada. Parabéns !", get_enchanted_sword],
        (2, 2):  ["Você está na primeira sala do castelo.", None],
        (2,0) : ["Nesta sala tem um T-Rex !!!", fight_trex],
        (0,0) : ["Nesta sala tem um Dragão Preto !!!", fight_dragon],
        (1,0) : ["Nesta sala tem um Dragão Laranja !", fight_dragon],
        (0,2) : ["Você achou um escudo. Ele vai te proteger", get_shield],
        (1,2) : ["Você achou um escudo em chamas. Ele vai te proteger e machucar os inimigos.", get_flaming_shield]
        }

class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        while 1:
            print "Você ataca."

            time.sleep(1)
            if random.random() >= 0.2:
                print "Consegui o golpe ! ", self.enemy.name, " levou ", self.player.attack, " de danos !"
                damage = self.player.attack - self.enemy.defense
                if damage < 0:
                    damage = 0
                self.enemy.life -= damage
                print self.enemy.name, ' esta com ', self.enemy.life, ' de vida.'
            else:
                print "O ", self.enemy.name, " esquivou o seu ataque :("

            if self.enemy.life <= 0:
                print self.enemy.name, " está morto, você ganhou !"
                return 0

            print self.enemy.name, " ataca."

            time.sleep(1)
            if random.random() >= 0.4:
                print "Ele acerta em você ! Você levou ", self.enemy.attack, " de danos !"
                damage = self.enemy.attack - self.player.defense
                if damage < 0:
                    damage = 0
                self.player.life -= damage
                print "Você esta com ", self.player.life, " de vida."
            else:
                print "Você esquivou o ataque."

            if self.player.life <= 0:
                print "Você está morto, você perdeu :("
                return 1

            print "-- Continuar --"
            raw_input()


class Enemy:
    def __init__(self, name, life, defense, attack):
        self.name = name
        self.life = life
        self.defense = defense
        self.attack = attack

class Player:
    def __init__(self):
        self.position = None
        self.life = 20
        self.attack = 1
        self.defense = 1
        pass

    def goto_room(self, position):
        if position in room:
            print position, " : " , room[position][0],

            action = room[position][1]
        else:
            print "Entrou numa sala sombria .... "
            action = None

        self.position = position

        if action is None:
            print " [N, S, L, O] ? "
        else:
            action(self)


    def play(self):
        self.goto_room((2, 2))
        while 1:
            next_action = raw_input()
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
                print "Não entendi !"
                continue

            if position[0] < 0 or position[0] >= MAX_ROW \
                    or position[1] < 0 or position[1] >= MAX_LINE:
                print "Você não pode ir nesta direção, tem uma parede !"
                self.goto_room(self.position)
                continue

            self.goto_room(position)

player = Player()
player.play()

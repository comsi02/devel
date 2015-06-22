#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

'''
    1. 등록
    2. game start
        - total round, total turn, 상대아이디
    3. round start
        - round info, round
    4. turn start
    5. turn end
    6. round end
    7. game end
    4. 공격 (가위/바위/보)
'''

class Player:
    def __init__(self, name):
        self.name = name
        print "* player name is {0}".format(self.name)

class Battle:

    MAX_TURN = 10

    MSG_ENTER = 0
    MSG_ATT = 1

    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    


    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB

        self.turn = 0

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print s

if __name__ == '__main__':
    p1 = Player('song')
    p2 = Player('shim')
    battle = Battle(p1,p2)


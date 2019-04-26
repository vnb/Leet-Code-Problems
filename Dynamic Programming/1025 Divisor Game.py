#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
"""

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        a_wins = 0
        b_wins = 0
        j = 2
        def get_i(N):
            for i in range(1,N):
                if N % i == 0:
                    return i
            return 0
        while get_i(N) != 0 and N > 0:
            x = get_i(N)
            if j % 2 == 0:
                N = N - x
                a_wins = 1
                b_wins = 0
            else:
                N = N - x
                b_wins = 1
                a_wins = 0
            j += 1
        if a_wins == 1:
            return True
        else:
            return False
                
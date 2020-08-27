#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *

from . import about_dice_project as adp
from . import about_scoring_project as asp


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

    class Game():
        pass

    class Player():
        pass

    class User():
        pass

    class AI():
        pass

    def test_test(self):
        dice = adp.DiceSet()
        self.assertEqual(dice.values, None)

    def test_dice_values_do_not_change_unless_explicitly_rolled(self):
        dice = adp.DiceSet()
        dice.roll(5)
        first_time = dice.values
        second_time = dice.values
        self.assertEqual(first_time, second_time)

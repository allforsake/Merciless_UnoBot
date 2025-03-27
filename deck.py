#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle
import logging

import card as c
from card import Card
from errors import DeckEmptyError


class Deck(object):
    """ This class represents a deck of cards """

    def __init__(self):
        self.cards = list()
        self.graveyard = list()
        self.logger = logging.getLogger(__name__)

        self.logger.debug(self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        self.logger.debug("Shuffling Deck")
        shuffle(self.cards)

    def draw(self):
        """Draws a card from this deck"""
        try:
            card = self.cards.pop()
            self.logger.debug("Drawing card " + str(card))
            return card
        except IndexError:
            if len(self.graveyard):
                while len(self.graveyard):
                    self.cards.append(self.graveyard.pop())
                self.shuffle()
                return self.draw()
            else:
                raise DeckEmptyError()

    def dismiss(self, card):
        """Returns a card to the deck"""
        if card.special:
            card.color = None
        self.graveyard.append(card)

    def _fill_classic_(self):
        # Fill deck with the classic card set
        self.cards.clear()
        for color in c.COLORS:
            for value in c.VALUES:
                self.cards.append(Card(color, value))
                if not value == c.ZERO:
                    self.cards.append(Card(color, value))
        for special in c.SPECIALS:
            for _ in range(4):
                self.cards.append(Card(None, None, special=special))
        self.shuffle()

    def _fill_wild_(self):
        # Fill deck with a wild card set
        self.cards.clear()
        for color in c.COLORS:
            for value in c.WILD_VALUES:
                for _ in range(4):
                    self.cards.append(Card(color, value))
        for special in c.SPECIALS:
            for _ in range(6):
                self.cards.append(Card(None, None, special=special))
        self.shuffle()

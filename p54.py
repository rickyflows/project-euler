#!/usr/bin/env python3
from poker import Card, Rank
from enum import Enum
from functools import total_ordering
from collections import Counter
from typing import List

@total_ordering
class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __lt__(self, other):
        return self.value < other.value

@total_ordering
class Hand:
    hand_size = 5
    def __init__(self, cards: List[Card]):
        if len(cards) != self.hand_size:
            raise Exception
        self.cards = sorted(cards)
        self.hand_type = self._process_type(cards)
        self.hand_value = self._process_value(cards)

    def _process_type(self, cards):
        candidate_types = []
        ranks = Counter(card.rank for card in cards)
        if len(ranks) == 5:
            # high card, straight, flush, straight flush, or royal flush
            suits = Counter(card.suit for card in cards)
            if len(suits) == 1:
                # flush
                if self._is_straight():
                    if self._is_royal():
                        return HandType.ROYAL_FLUSH
                    else:
                        return HandType.STRAIGHT_FLUSH
                return HandType.FLUSH
            else:
                # straight or high card
                if self._is_straight():
                    return HandType.STRAIGHT
                return HandType.HIGH_CARD
        if len(ranks) == 2:
            # full house or four of a kind
            if max(ranks.values()) == 4:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        if len(ranks) == 3:
            # two pair or three of a kind
            if max(ranks.values()) == 3:
                return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIR
        if len(ranks) == 4:
            # pair
            return HandType.PAIR

    def _process_value(self, cards):
        ranks = Counter(card.rank for card in cards)
        if len(ranks) == 5:
            # high card, straight, flush, straight flush, or royal flush
            return max(ranks)
        if len(ranks) == 2:
            # full house or four of a kind
            return max(ranks, key=ranks.get)
        if len(ranks) == 3:
            # two pair or three of a kind
            if max(ranks.values()) == 3:
                return max(ranks, key=ranks.get)
            return tuple(sorted([rank for rank in ranks if ranks[rank] == 2], reverse=True))
        if len(ranks) == 4:
            # pair
            return max(ranks, key=ranks.get)

    def _is_straight(self):
        # requires cards to be sorted
        card_ranks = [card.rank for card in self.cards]
        if Rank('A') in card_ranks:
            # special case
            return card_ranks == [Rank('2'), Rank('3'), Rank('4'), Rank('5'), Rank('A')]
        return Rank.difference(card_ranks[0], card_ranks[-1]) == self.hand_size - 1

    def _is_royal(self):
        return all(card.is_broadway for card in self.cards)

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            if self.hand_value == other.hand_value:
                self_ranks = [card.rank for card in self.cards][::-1]
                other_ranks = [card.rank for card in other.cards][::-1]
                for self_rank, other_rank in zip(self_ranks, other_ranks):
                    if self_rank == other_rank:
                        continue
                    return self_rank < other_rank
            return self.hand_value < other.hand_value
        return self.hand_type < other.hand_type

def main():
    with open("data/poker.txt") as f:
        data = f.readlines()
    count = 0
    for line in data:
        cards = [Card(rep) for rep in line.split()]
        count += Hand(cards[:5]) > Hand(cards[5:])

    print(count)

if __name__ == "__main__":
    main()

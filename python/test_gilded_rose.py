# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def get_fixture_items(self, name):
        return [
            Item(name, 0, 0),
            Item(name, -1, 10),
            Item(name, 5, 45),
            Item(name, 6, 45),
            Item(name, 7, 52),
            Item(name, 12, 52),
        ]

    def check_asserts(self, items, expects):
        self.assertEqual(len(items), len(expects))

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for i, item in enumerate(items):
            self.assertEqual(item.quality, expects[i].quality)
            self.assertEqual(item.sell_in, expects[i].sell_in)

    def test_01_others_item(self):
        name = "Others"
        items = self.get_fixture_items(name)
        expects = [
            Item(name, -1, 0),
            Item(name, -2, 8),
            Item(name, 4, 44),
            Item(name, 5, 44),
            Item(name, 6, 51),
            Item(name, 11, 51),
        ]
        self.check_asserts(items, expects)

    def test_02_aged_brie(self):
        name = GildedRose.AGED_BRIE
        items = self.get_fixture_items(name)
        expects = [
            Item(name, -1, 2),
            Item(name, -2, 12),
            Item(name, 4, 46),
            Item(name, 5, 46),
            Item(name, 6, 52),
            Item(name, 11, 52),
        ]
        self.check_asserts(items, expects)

    def test_03_sulfuras_hand_of_ragnaros(self):
        name = GildedRose.SULFURAS_HAND_OF_RAGNAROS
        items = self.get_fixture_items(name)
        self.check_asserts(items, items)

    def test_04_backstage_passes_to_a_tafkal80etc_concert(self):
        name = GildedRose.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT
        items = self.get_fixture_items(name)
        expects = [
            Item(name, -1, 0),
            Item(name, -2, 0),
            Item(name, 4, 48),
            Item(name, 5, 47),
            Item(name, 6, 52),
            Item(name, 11, 52),
        ]
        self.check_asserts(items, expects)


if __name__ == "__main__":
    unittest.main()

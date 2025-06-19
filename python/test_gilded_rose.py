# -*- coding: utf-8 -*-
import copy
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def get_fixture_items(self, name):
        return [
            Item.from_values(name, 9, 19),
            Item.from_values(name, 1, 1),
            Item.from_values(name, 4, 6),
            Item.from_values(name, 0, 80),
            Item.from_values(name, -1, 80),
            Item.from_values(name, 14, 21),
            Item.from_values(name, 9, 51),
            Item.from_values(name, 4, 52),
            Item.from_values(name, 2, 5),
            Item.from_values(name, 8, 18),
            Item.from_values(name, 8, 51),
            Item.from_values(name, 3, 52),
            Item.from_values(name, 1, 4),
        ]

    def _check_asserts(self, items, expects):
        self.assertEqual(len(items), len(expects))

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for i, item in enumerate(items):
            self.assertEqual(expects[i].quality, item.quality, f"[{i}] {item} {expects[i]}")
            self.assertEqual(expects[i].sell_in, item.sell_in, f"[{i}] {item} {expects[i]}")

    def _original_func(self, items):
        items = copy.deepcopy(items)
        for item in items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
        return items

    def test_01_others_item(self):
        items = self.get_fixture_items("Others")
        expects = self._original_func(items)
        self._check_asserts(items, expects)
        
    def test_02_aged_brie(self):
        name = Item.AGED_BRIE
        items = self.get_fixture_items(name)
        expects = self._original_func(items)
        self._check_asserts(items, expects)

    def test_03_sulfuras_hand_of_ragnaros(self):
        name = Item.SULFURAS_HAND_OF_RAGNAROS
        items = self.get_fixture_items(name)
        self._check_asserts(items, items)

    def test_04_backstage_passes_to_a_tafkal80etc_concert(self):
        name = Item.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT
        items = self.get_fixture_items(name)
        expects = self._original_func(items)
        self._check_asserts(items, expects)


if __name__ == "__main__":
    unittest.main()

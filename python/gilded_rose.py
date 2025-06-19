# -*- coding: utf-8 -*-


class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    SULFURAS_HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == self.SULFURAS_HAND_OF_RAGNAROS:
                continue
            self._update_age_brie(item)
            self._update_backstage_passes_to_a_tafkal80etc_concert(item)
            self._update_other(item)

    def _update_age_brie(self, item):
        if item.name != self.AGED_BRIE:
            return
        item.sell_in -= 1
        if item.quality < 50:
            if item.sell_in < 0:
                item.quality += 1
            item.quality += 1

    def _update_backstage_passes_to_a_tafkal80etc_concert(self, item):
        if item.name != self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT:
            return
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                item.quality += 1
            if item.sell_in < 6:
                item.quality += 1

        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = item.quality - item.quality

    def _update_other(self, item):
        if (
            item.name == self.AGED_BRIE
            or item.name == self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT
        ):
            return
        item.sell_in -= 1
        if item.quality > 0:
            if item.sell_in < 0:
                item.quality -= 1
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

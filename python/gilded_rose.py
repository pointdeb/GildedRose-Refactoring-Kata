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
            
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT:
                if item.quality > 0:
                    item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT:
                        if item.sell_in < 11:
                            item.quality = item.quality + 1
                        if item.sell_in < 6:
                            item.quality = item.quality + 1
            
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name == self.AGED_BRIE:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                elif item.name == self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT:
                    item.quality = item.quality - item.quality
                elif item.quality > 0:
                    item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

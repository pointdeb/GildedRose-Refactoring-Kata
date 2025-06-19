# -*- coding: utf-8 -*-


from typing import List

class Item:
    AGED_BRIE = "Aged Brie"
    SULFURAS_HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT = (
        "Backstage passes to a TAFKAL80ETC concert"
    )

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in -= 1
        if self.quality > 0:
            if self.sell_in < 0:
                self.quality -= 1
            self.quality -= 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @classmethod
    def from_values(cls, name, sell_in, quality):
        if name == cls.AGED_BRIE:
            return AgedBrieItem(sell_in, quality)
        elif name == cls.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT:
            return BackstagePassesToATafkal80EtcConcertItem(sell_in, quality)
        elif name == cls.SULFURAS_HAND_OF_RAGNAROS:
            return SulfurasHandOfRagnarosItem(sell_in, quality)
        else:
            return cls(name, sell_in, quality)


class AgedBrieItem(Item):

    def __init__(self, sell_in, quality):
        name = self.AGED_BRIE
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        if self.quality < 50:
            if self.sell_in < 0:
                self.quality += 1
            self.quality += 1


class BackstagePassesToATafkal80EtcConcertItem(Item):

    def __init__(self,sell_in, quality):
        name = self.BACKSTAGE_PASSES_TO_A_TAFKAL80ETC_CONCERT
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                self.quality += 1
            if self.sell_in < 6:
                self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= self.quality


class SulfurasHandOfRagnarosItem(Item):

    def __init__(self, sell_in, quality):
        name = self.SULFURAS_HAND_OF_RAGNAROS
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class GildedRose(object):
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
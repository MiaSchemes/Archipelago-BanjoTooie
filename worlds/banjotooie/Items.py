from BaseClasses import Item
import typing
from .Names import itemName


class BanjoTooieItem(Item):
    game: str = "Banjo Tooie"
class ItemData(typing.NamedTuple):
    btid: int = 0
    qty: int = 0
    type: str = ""



jinjo_table = {
    itemName.WJINJO:        ItemData(1230501, 1, "progress"),
    itemName.OJINJO:        ItemData(1230502, 2, "progress"),
    itemName.YJINJO:        ItemData(1230503, 3, "progress"),
    itemName.BRJINJO:       ItemData(1230504, 4, "progress"),
    itemName.GJINJO:        ItemData(1230505, 5, "progress"),
    itemName.RJINJO:        ItemData(1230506, 6, "progress"),
    itemName.BLJINJO:       ItemData(1230507, 7, "progress"),
    itemName.PJINJO:        ItemData(1230508, 8, "progress"),
    itemName.BKJINJO:       ItemData(1230509, 9, "progress")
}

jiggy_table = {
    itemName.JIGGYIH1:  ItemData(1230676, 1, "progress"),
    itemName.JIGGYIH2:  ItemData(1230677, 1, "progress"),
    itemName.JIGGYIH3:  ItemData(1230678, 1, "progress"),
    itemName.JIGGYIH4:  ItemData(1230679, 1, "progress"),
    itemName.JIGGYIH5:  ItemData(1230680, 1, "progress"),
    itemName.JIGGYIH6:  ItemData(1230681, 1, "progress"),
    itemName.JIGGYIH7:  ItemData(1230682, 1, "progress"),
    itemName.JIGGYIH8:  ItemData(1230683, 1, "progress"),
    itemName.JIGGYIH9:  ItemData(1230684, 1, "progress"),
    itemName.JIGGYIH10: ItemData(1230685, 1, "progress"),
    itemName.JIGGYMT1:  ItemData(1230596, 1, "progress"),
    itemName.JIGGYMT2:  ItemData(1230597, 1, "progress"),
    itemName.JIGGYMT3:  ItemData(1230598, 1, "progress"),
    itemName.JIGGYMT4:  ItemData(1230599, 1, "progress"),
    itemName.JIGGYMT5:  ItemData(1230600, 1, "progress"),
    itemName.JIGGYMT6:  ItemData(1230601, 1, "progress"),
    itemName.JIGGYMT7:  ItemData(1230602, 1, "progress"),
    itemName.JIGGYMT8:  ItemData(1230603, 1, "progress"),
    itemName.JIGGYMT9:  ItemData(1230604, 1, "progress"),
    itemName.JIGGYMT10: ItemData(1230605, 1, "progress"),
    itemName.JIGGYGM1:  ItemData(1230606, 1, "progress"),
    itemName.JIGGYGM2:  ItemData(1230607, 1, "progress"),
    itemName.JIGGYGM3:  ItemData(1230608, 1, "progress"),
    itemName.JIGGYGM4:  ItemData(1230609, 1, "progress"),
    itemName.JIGGYGM5:  ItemData(1230610, 1, "progress"),
    itemName.JIGGYGM6:  ItemData(1230611, 1, "progress"),
    itemName.JIGGYGM7:  ItemData(1230612, 1, "progress"),
    itemName.JIGGYGM8:  ItemData(1230613, 1, "progress"),
    itemName.JIGGYGM9:  ItemData(1230614, 1, "progress"),
    itemName.JIGGYGM10: ItemData(1230615, 1, "progress"),
    itemName.JIGGYWW1:  ItemData(1230616, 1, "progress"),
    itemName.JIGGYWW2:  ItemData(1230617, 1, "progress"),
    itemName.JIGGYWW3:  ItemData(1230618, 1, "progress"),
    itemName.JIGGYWW4:  ItemData(1230619, 1, "progress"),
    itemName.JIGGYWW5:  ItemData(1230620, 1, "progress"),
    itemName.JIGGYWW6:  ItemData(1230621, 1, "progress"),
    itemName.JIGGYWW7:  ItemData(1230622, 1, "progress"),
    itemName.JIGGYWW8:  ItemData(1230623, 1, "progress"),
    itemName.JIGGYWW9:  ItemData(1230624, 1, "progress"),
    itemName.JIGGYWW10: ItemData(1230625, 1, "progress"),
    itemName.JIGGYJR1:  ItemData(1230626, 1, "progress"),
    itemName.JIGGYJR2:  ItemData(1230627, 1, "progress"),
    itemName.JIGGYJR3:  ItemData(1230628, 1, "progress"),
    itemName.JIGGYJR4:  ItemData(1230629, 1, "progress"),
    itemName.JIGGYJR5:  ItemData(1230630, 1, "progress"),
    itemName.JIGGYJR6:  ItemData(1230631, 1, "progress"),
    itemName.JIGGYJR7:  ItemData(1230632, 1, "progress"),
    itemName.JIGGYJR8:  ItemData(1230633, 1, "progress"),
    itemName.JIGGYJR9:  ItemData(1230634, 1, "progress"),
    itemName.JIGGYJR10: ItemData(1230635, 1, "progress"),
    itemName.JIGGYTD1:  ItemData(1230636, 1, "progress"),
    itemName.JIGGYTD2:  ItemData(1230637, 1, "progress"),
    itemName.JIGGYTD3:  ItemData(1230638, 1, "progress"),
    itemName.JIGGYTD4:  ItemData(1230639, 1, "progress"),
    itemName.JIGGYTD5:  ItemData(1230640, 1, "progress"),
    itemName.JIGGYTD6:  ItemData(1230641, 1, "progress"),
    itemName.JIGGYTD7:  ItemData(1230642, 1, "progress"),
    itemName.JIGGYTD8:  ItemData(1230643, 1, "progress"),
    itemName.JIGGYTD9:  ItemData(1230644, 1, "progress"),
    itemName.JIGGYTD10: ItemData(1230645, 1, "progress"),
    itemName.JIGGYGI1:  ItemData(1230646, 1, "progress"),
    itemName.JIGGYGI2:  ItemData(1230647, 1, "progress"),
    itemName.JIGGYGI3:  ItemData(1230648, 1, "progress"),
    itemName.JIGGYGI4:  ItemData(1230649, 1, "progress"),
    itemName.JIGGYGI5:  ItemData(1230650, 1, "progress"),
    itemName.JIGGYGI6:  ItemData(1230651, 1, "progress"),
    itemName.JIGGYGI7:  ItemData(1230652, 1, "progress"),
    itemName.JIGGYGI8:  ItemData(1230653, 1, "progress"),
    itemName.JIGGYGI9:  ItemData(1230654, 1, "progress"),
    itemName.JIGGYGI10: ItemData(1230655, 1, "progress"),
    itemName.JIGGYHP1:  ItemData(1230656, 1, "progress"),
    itemName.JIGGYHP2:  ItemData(1230657, 1, "progress"),
    itemName.JIGGYHP3:  ItemData(1230658, 1, "progress"),
    itemName.JIGGYHP4:  ItemData(1230659, 1, "progress"),
    itemName.JIGGYHP5:  ItemData(1230660, 1, "progress"),
    itemName.JIGGYHP6:  ItemData(1230661, 1, "progress"),
    itemName.JIGGYHP7:  ItemData(1230662, 1, "progress"),
    itemName.JIGGYHP8:  ItemData(1230663, 1, "progress"),
    itemName.JIGGYHP9:  ItemData(1230664, 1, "progress"),
    itemName.JIGGYHP10: ItemData(1230665, 1, "progress"),
    itemName.JIGGYCC1:  ItemData(1230666, 1, "progress"),
    itemName.JIGGYCC2:  ItemData(1230667, 1, "progress"),
    itemName.JIGGYCC3:  ItemData(1230668, 1, "progress"),
    itemName.JIGGYCC4:  ItemData(1230669, 1, "progress"),
    itemName.JIGGYCC5:  ItemData(1230670, 1, "progress"),
    itemName.JIGGYCC6:  ItemData(1230671, 1, "progress"),
    itemName.JIGGYCC7:  ItemData(1230672, 1, "progress"),
    itemName.JIGGYCC8:  ItemData(1230673, 1, "progress"),
    itemName.JIGGYCC9:  ItemData(1230674, 1, "progress"),
    itemName.JIGGYCC10: ItemData(1230675, 1, "progress"),
}

level_progress_table = {
    itemName.MUMBOMT:        ItemData(1230855, 1, "progress"),
    itemName.MUMBOGM:        ItemData(1230856, 1, "progress"),
    itemName.MUMBOWW:        ItemData(1230857, 1, "progress"),
    itemName.MUMBOJR:        ItemData(1230858, 1, "progress"),
    itemName.MUMBOTD:        ItemData(1230859, 1, "progress"),
    itemName.MUMBOGI:        ItemData(1230860, 1, "progress"),
    itemName.MUMBOHP:        ItemData(1230861, 1, "progress"),
    itemName.MUMBOCC:        ItemData(1230862, 1, "progress"),
    itemName.MUMBOIH:        ItemData(1230863, 1, "progress"),

    itemName.HUMBAMT:        ItemData(1230174, 1, "progress"),
    itemName.HUMBAGM:        ItemData(1230175, 1, "progress"),
    itemName.HUMBAWW:        ItemData(1230176, 1, "progress"),
    itemName.HUMBAJR:        ItemData(1230177, 1, "progress"),
    itemName.HUMBATD:        ItemData(1230178, 1, "progress"),
    itemName.HUMBAGI:        ItemData(1230179, 1, "progress"),
    itemName.HUMBAHP:        ItemData(1230180, 1, "progress"),
    itemName.HUMBACC:        ItemData(1230181, 1, "progress"),
    itemName.HUMBAIH:        ItemData(1230182, 1, "progress"),
}

misc_collectable_table = {
    itemName.HONEY:         ItemData(1230512, 25, "useful"),
    itemName.PAGES:         ItemData(1230513, 25, "useful"),
    itemName.DOUBLOON:      ItemData(1230514, 30, "useful")
}



all_item_table = {
    **jinjo_table,
    **level_progress_table,
    **misc_collectable_table,
    **jiggy_table
}

all_group_table = {
    'jiggy' : jiggy_table,
    'jinjo' : jinjo_table,
    'misc' : misc_collectable_table
}




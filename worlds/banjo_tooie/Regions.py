import typing
from BaseClasses import Region
from .Names import regionName, locationName, itemName
from .Locations import BanjoTooieLocation

BANJOTOOIEREGIONS: typing.Dict[str, typing.List[str]] = {
    "Menu":              [],
    regionName.SM:       [
        locationName.CHEATOSM1,
        locationName.JINJOIH5,
    #    locationName.FSWIM
    ],
    regionName.IOHJV:    [
        # locationName.JIGGYIH1,
        # locationName.JIGGYIH2,
        # locationName.JIGGYIH3,
        # locationName.JIGGYIH4,
        # locationName.JIGGYIH5,
        # locationName.JIGGYIH6,
        # locationName.JIGGYIH7,
        # locationName.JIGGYIH8,
        # locationName.JIGGYIH9,
        locationName.JIGGYIH10,
        locationName.TREBLEJV
    ],
    regionName.IOHWH:    [
        locationName.JINJOIH1
    ],
    regionName.MT:       [
        locationName.JINJOMT1, 
        locationName.JINJOMT2,
        locationName.JINJOMT3,
        locationName.JINJOMT4,
        locationName.JINJOMT5,
        locationName.JIGGYMT1,
        locationName.JIGGYMT2,
        locationName.JIGGYMT3,
        locationName.JIGGYMT4,
        locationName.JIGGYMT5,
        locationName.JIGGYMT6,
        locationName.JIGGYMT7,
        locationName.JIGGYMT8,
        locationName.JIGGYMT9,
        locationName.JIGGYMT10,
        locationName.GLOWBOMT1,
        locationName.GLOWBOMT2,
        locationName.HONEYCMT1,
        locationName.HONEYCMT2,
        locationName.HONEYCMT3,
        locationName.CHEATOMT1,
        locationName.CHEATOMT2,
        locationName.CHEATOMT3,
        locationName.GGRAB,
        locationName.BBLASTER,
        locationName.EGGAIM,
        locationName.TREBLEMT
    ],
    regionName.IOHPL:    [
        locationName.JINJOIH4,
        locationName.HONEYCIH1,
        locationName.FEGGS
    ],
    regionName.GM:       [
        locationName.JINJOGM1,
        locationName.JINJOGM2,
        locationName.JINJOGM3,
        locationName.JINJOGM4,
        locationName.JINJOGM5,
        locationName.JIGGYGM1,
        locationName.JIGGYGM2,
        locationName.JIGGYGM3,
        locationName.JIGGYGM4,
        locationName.JIGGYGM5,
        locationName.JIGGYGM6,
        locationName.JIGGYGM7,
        locationName.JIGGYGM8,
        locationName.JIGGYGM9,
        locationName.JIGGYGM10,
        locationName.GLOWBOGM1,
        locationName.GLOWBOGM2,
        locationName.GLOWBOMEG,
        locationName.HONEYCGM1,
        locationName.HONEYCGM2,
        locationName.HONEYCGM3,
        locationName.CHEATOGM1,
        locationName.CHEATOGM2,
        locationName.CHEATOGM3,
        locationName.BDRILL,
        locationName.BBAYONET,
        locationName.TREBLEGM
    ],
    regionName.IOHPG:   [
        locationName.GEGGS
    ],
    regionName.IOHCT:   [
        locationName.JINJOIH3,
        locationName.GLOWBOIH1,
        locationName.IEGGS,
        locationName.TRAINSWIH
    ],
    regionName.WW:      [
        locationName.JINJOWW1,
        locationName.JINJOWW2,
        locationName.JINJOWW3,
        locationName.JINJOWW4,
        locationName.JINJOWW5,
        locationName.JIGGYWW1,
        locationName.JIGGYWW2,
        locationName.JIGGYWW3,
        locationName.JIGGYWW4,
        locationName.JIGGYWW5,
        locationName.JIGGYWW6,
        locationName.JIGGYWW7,
        locationName.JIGGYWW8,
        locationName.JIGGYWW9,
        locationName.JIGGYWW10,
        locationName.GLOWBOWW1,
        locationName.GLOWBOWW2,
        locationName.HONEYCWW1,
        locationName.HONEYCWW2,
        locationName.HONEYCWW3,
        locationName.CHEATOWW1,
        locationName.CHEATOWW2,
        locationName.CHEATOWW3,
        locationName.AIREAIM,
        locationName.SPLITUP,
        locationName.PACKWH,
        locationName.TREBLEWW
    ],
    regionName.JR:      [
        locationName.JRLDB1,
        locationName.JRLDB2,
        locationName.JRLDB3,
        locationName.JRLDB4,
        locationName.JRLDB5,
        locationName.JRLDB6,
        locationName.JRLDB7,
        locationName.JRLDB8,
        locationName.JRLDB9,
        locationName.JRLDB10,
        locationName.JRLDB11,
        locationName.JRLDB12,
        locationName.JRLDB13,
        locationName.JRLDB14,
        locationName.JRLDB15,
        locationName.JRLDB16,
        locationName.JRLDB17,
        locationName.JRLDB18,
        locationName.JRLDB19,
        locationName.JRLDB20,
        locationName.JRLDB21,
        locationName.JRLDB22,
        locationName.JRLDB23,
        locationName.JRLDB24,
        locationName.JRLDB25,
        locationName.JRLDB26,
        locationName.JRLDB27,
        locationName.JRLDB28,
        locationName.JRLDB29,
        locationName.JRLDB30,
        locationName.JINJOJR1,
        locationName.JINJOJR2,
        locationName.JINJOJR3,
        locationName.JINJOJR4,
        locationName.JINJOJR5,
        locationName.JIGGYJR1,
        locationName.JIGGYJR2,
        locationName.JIGGYJR3,
        locationName.JIGGYJR4,
        locationName.JIGGYJR5,
        locationName.JIGGYJR6,
        locationName.JIGGYJR7,
        locationName.JIGGYJR8,
        locationName.JIGGYJR9,
        locationName.JIGGYJR10,
        locationName.GLOWBOJR1,
        locationName.GLOWBOJR2,
        locationName.HONEYCJR1,
        locationName.HONEYCJR2,
        locationName.HONEYCJR3,
        locationName.CHEATOJR1,
        locationName.CHEATOJR2,
        locationName.CHEATOJR3,
        locationName.WWHACK,
        locationName.TTORP,
        locationName.AUQAIM,
        locationName.TREBLEJR
    ],
    regionName.IOHWL:   [
         locationName.JINJOIH2,
         locationName.CEGGS
    ],
    regionName.TL:      [
        locationName.JINJOTL1,
        locationName.JINJOTL2,
        locationName.JINJOTL3,
        locationName.JINJOTL4,
        locationName.JINJOTL5,
        locationName.JIGGYTD1,
        #locationName.JIGGYTD2, #In CCL
        locationName.JIGGYTD3,
        locationName.JIGGYTD4,
        locationName.JIGGYTD5,
        locationName.JIGGYTD6,
        locationName.JIGGYTD7,
        locationName.JIGGYTD8,
        locationName.JIGGYTD9,
        locationName.JIGGYTD10,
        locationName.JIGGYHP7,
        locationName.GLOWBOTL1,
        locationName.GLOWBOTL2,
        locationName.HONEYCTL1,
        locationName.HONEYCTL2,
        locationName.HONEYCTL3,
        locationName.CHEATOTL1,
        locationName.CHEATOTL2,
        locationName.CHEATOTL3,
        locationName.SPRINGB,
        locationName.TAXPACK,
        locationName.TREBLETL,
        locationName.TRAINSWTD,
    ],
    regionName.TL_HATCH: [
        locationName.HATCH,
    ],
    regionName.IOHQM:   [],
    regionName.GI:      [
        locationName.JINJOGI1,
        locationName.JINJOGI2,
        locationName.JINJOGI3,
        locationName.JINJOGI4,
        locationName.JINJOGI5,
        locationName.JIGGYGI1,
        locationName.JIGGYGI2,
        locationName.JIGGYGI3,
        locationName.JIGGYGI4,
        locationName.JIGGYGI5,
        locationName.JIGGYGI6,
        locationName.JIGGYGI7,
        locationName.JIGGYGI8,
        locationName.JIGGYGI9,
        locationName.JIGGYGI10,
        locationName.GLOWBOGI1,
        locationName.GLOWBOGI2,
        locationName.HONEYCGI1,
        locationName.HONEYCGI2,
        locationName.HONEYCGI3,
        locationName.CHEATOGI1,
        locationName.CHEATOGI2,
        locationName.CHEATOGI3,
        locationName.SNPACK,
        locationName.LSPRING,
        locationName.CLAWBTS,
        locationName.TREBLEGI,
        locationName.TRAINSWGI,
    ],
    regionName.HP:      [
        locationName.JINJOHP1,
        locationName.JINJOHP2,
        locationName.JINJOHP3,
        locationName.JINJOHP4,
        locationName.JINJOHP5,
        locationName.JIGGYHP1,
        locationName.JIGGYHP2,
        locationName.JIGGYHP3,
        locationName.JIGGYHP4,
        locationName.JIGGYHP6,
        #locationName.JIGGYHP7, # in TDL
        locationName.JIGGYHP8,
        locationName.JIGGYHP9,
        locationName.JIGGYHP10,
        locationName.GLOWBOHP1,
        locationName.GLOWBOHP2,
        locationName.HONEYCHP1,
        locationName.HONEYCHP2,
        locationName.HONEYCHP3,
        locationName.CHEATOHP1,
        locationName.CHEATOHP2,
        locationName.CHEATOHP3,
        locationName.SHPACK,
        locationName.GLIDE,
        locationName.TREBLEHP,
        locationName.TRAINSWHP1,
        locationName.TRAINSWHP2
    ],
    regionName.CC:      [
        locationName.JINJOCC1,
        locationName.JINJOCC2,
        locationName.JINJOCC3,
        locationName.JINJOCC4,
        locationName.JINJOCC5,
        locationName.JIGGYCC1,
        locationName.JIGGYCC2,
        locationName.JIGGYCC3,
        locationName.JIGGYCC4,
        locationName.JIGGYCC5,
        locationName.JIGGYCC6,
        locationName.JIGGYCC7,
        locationName.JIGGYCC8,
        locationName.JIGGYCC9,
        locationName.JIGGYCC10,
        locationName.JIGGYTD2,
        locationName.GLOWBOCC1,
        locationName.GLOWBOCC2,
        locationName.HONEYCCC1,
        locationName.HONEYCCC2,
        locationName.HONEYCCC3,
        locationName.CHEATOCC1,
        locationName.CHEATOCC2,
        locationName.CHEATOCC3,
        locationName.SAPACK,
        locationName.TREBLECC
    ],
    regionName.CK: [],
    regionName.H1: [
        locationName.HAG1
    ],
    regionName.GMS: [
        locationName.CHUFFY
    ],
    regionName.TLS: [],
    regionName.GIS: [],     
    regionName.HPLS: [],      
    regionName.HPIS: [
        locationName.JIGGYHP5,
    ],     
    regionName.IOHCTS: []  
}

BANJOTOOIECONNECTIONS: typing.Dict[str, typing.Set[str]] = {
        "Menu":                        {regionName.SM},
        regionName.SM:                 {regionName.IOHJV},
        regionName.IOHJV:              {regionName.IOHWH},
        regionName.IOHWH:              {regionName.MT, regionName.IOHPL},
        regionName.MT:                 {regionName.TL_HATCH},
        regionName.IOHPL:              {regionName.GM, regionName.IOHCT, regionName.IOHPG},
        regionName.IOHCT:              {regionName.JR, regionName.HP},
        regionName.IOHPG:              {regionName.WW, regionName.IOHWL},
        regionName.IOHWL:              {regionName.TL, regionName.CC, regionName.IOHQM},
        regionName.TL:                 {regionName.TL_HATCH},
        regionName.IOHQM:              {regionName.GI, regionName.CK},
        regionName.CK:                 {regionName.H1},
        #Train Station Connections
        regionName.GM:                 {regionName.GMS},
        regionName.GMS:                {regionName.IOHCTS, regionName.TLS, regionName.GIS, regionName.HPLS},
        regionName.TLS:                {regionName.IOHCTS, regionName.TL, regionName.GIS, regionName.HPLS},
        regionName.GIS:                {regionName.IOHCTS, regionName.GI, regionName.HPLS},
        regionName.HPLS:               {regionName.IOHCTS, regionName.HP, regionName.HPIS},
        regionName.IOHCTS:             {regionName.IOHCT}
    }
    
def create_regions(self):
    multiworld = self.multiworld
    player = self.player
    active_locations = self.location_name_to_id

    multiworld.regions += [create_region(multiworld, player, active_locations, region, locations) for region, locations in
                           BANJOTOOIEREGIONS.items()]
    
    multiworld.get_location(locationName.HAG1, player).place_locked_item(
        multiworld.worlds[player].create_event_item(itemName.VICTORY))


def create_region(multiworld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, multiworld)
    if locations:
        loc_to_id = {loc: active_locations.get(loc, 0) for loc in locations if active_locations.get(loc, None)}
        if locationName.HAG1 in locations:
            ret.add_locations({locationName.HAG1: None})
        else:
            ret.add_locations(loc_to_id, BanjoTooieLocation)
    return ret

def connect_regions(self):
    multiworld = self.multiworld
    player = self.player

    for source, target in BANJOTOOIECONNECTIONS.items():
        source_region = multiworld.get_region(source, player)
        if regionName.TL_HATCH in target:
            continue
        source_region.add_exits(target)

    region_MT = multiworld.get_region(regionName.MT, player)
    region_MT.add_exits({regionName.TL_HATCH,},
                        {regionName.TL_HATCH: lambda state: (state.has(itemName.GGRAB, player) and state.has(itemName.EGGAIM, player)) or
                                                            (state.has(itemName.MUMBOMT, player) or state.has(itemName.BDRILL, player))})
    region_TL = multiworld.get_region(regionName.TL, player)
    region_TL.add_exits({regionName.TL_HATCH,})



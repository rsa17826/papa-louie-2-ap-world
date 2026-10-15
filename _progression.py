from typing import NotRequired, TypedDict


class ProgressionNode(TypedDict):
  room: str
  receive: list[str]
  # requires: NotRequired[list[list[str]]]
  requires: list[list[str]]
  info: NotRequired[str]


PROG: list[ProgressionNode] = [
  {
    "room": "menu",
    "requires": [
      [],
    ],
    "receive": [
      "unlockedLevel:level1",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level1",
      "unlockedLevel:level2",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level2",
      "unlockedLevel:level3",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level3",
      "unlockedLevel:level4",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level4",
      "unlockedLevel:level5",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level5",
      "unlockedLevel:level6",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level6",
      "unlockedLevel:level7",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level7",
      "unlockedLevel:level8",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level8",
      "unlockedLevel:level9",
    ],
  },
  {
    "room": "level9",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level9",
      "unlockedLevel:level10",
    ],
  },
  {
    "room": "level10",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "flag:beat level10",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:marty",
      ],
      [
        "char:rita",
      ],
      [
        "char:prudence",
      ],
      [
        "char:taylor",
      ],
      [
        "char:clover",
      ],
      [
        "char:mindy",
      ],
      [
        "char:akari",
      ],
      [
        "char:zoe",
      ],
    ],
    "receive": [
      "move:nothing",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:big pauly",
      ],
      [
        "char:kahuna",
      ],
      [
        "char:kingsley",
      ],
    ],
    "receive": [
      "move:stomp",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:ninjoy",
      ],
      [
        "char:penny",
      ],
      [
        "char:sarge fan",
      ],
    ],
    "receive": [
      "move:walljump",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:james",
      ],
      [
        "char:captain cori",
      ],
      [
        "char:rico",
      ],
    ],
    "receive": [
      "move:push",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:scooter",
      ],
      [
        "char:connor",
      ],
      [
        "char:peggy",
      ],
    ],
    "receive": [
      "move:dbjump",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:georgito",
      ],
      [
        "char:yippy",
      ],
      [
        "char:greg",
      ],
    ],
    "receive": [
      "move:crawl",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        # TODO weapon stun only - see if this changes anything anywhere
        "char:boomer",
      ],
      [
        "char:professor fitz",
      ],
      [
        "char:foodini",
      ],
      [
        "char:papa louie",
      ],
      [
        # REVIEW has higher jump, test both with and without, and use char:xandra instead of move:glide if required
        "char:xandra",
      ],
    ],
    "receive": [
      "move:glide",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "char:prudence",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "char:taylor",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "flag:hasChar",
        "move:stomp",
      ],
    ],
    "receive": [
      "char:clover",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 red coins",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:3 burgers",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:big pauly",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:mindy",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "char:marty",
      ],
      [
        "char:rita",
      ],
      [
        "char:prudence",
      ],
      [
        "char:taylor",
      ],
      [
        "char:clover",
      ],
      [
        "char:mindy",
      ],
      [
        "char:akari",
      ],
      [
        "char:zoe",
      ],
      [
        "char:big pauly",
      ],
      [
        "char:kahuna",
      ],
      [
        "char:kingsley",
      ],
      [
        "char:ninjoy",
      ],
      [
        "char:penny",
      ],
      [
        "char:sarge fan",
      ],
      [
        "char:james",
      ],
      [
        "char:captain cori",
      ],
      [
        "char:rico",
      ],
      [
        "char:scooter",
      ],
      [
        "char:connor",
      ],
      [
        "char:peggy",
      ],
      [
        "char:georgito",
      ],
      [
        "char:yippy",
      ],
      [
        "char:greg",
      ],
      [
        "char:boomer",
      ],
      [
        "char:professor fitz",
      ],
      [
        "char:foodini",
      ],
      [
        "char:papa louie",
      ],
      [
        "char:xandra",
      ],
      [
        "char:marty",
      ],
    ],
    "receive": [
      "flag:hasChar",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:fizzocan",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "char:akari",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [],
    ],
    "receive": [
      "collectCheck:5 flowers",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "flag:hasChar",
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:11 burgers",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "flag:hasChar",
        "move:crawl",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      # REVIEW can't kill saucers in any way so force other char than this one if that kill required
      "char:boomer",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:glide",
      ],
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "coinless:level3",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "coinless:level5",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:glide",
        "move:walljump",
      ],
    ],
    "receive": [
      "coinless:level8",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:kahuna",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level1",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level2",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level3",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level4",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level5",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level6",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level7",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level8",
    ],
  },
  {
    "room": "level9",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level9",
    ],
  },
  {
    "room": "level10",
    "requires": [
      [
        "move:nothing",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "powerless:level10",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:crawl",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:professor fitz",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 helmets",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:11 burgers",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:dbjump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:georgito",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:crawl",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:foodini",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:dbjump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:yippy",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 purple coins",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:crawl",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:6 burgers",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:push",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:scooter",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:dbjump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:kingsley",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:push",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:connor",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 worms",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:8 burgers",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:walljump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:james",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:push",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:greg",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:walljump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:captain cori",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 balloons",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:crawl",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:10 burgers",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:ninjoy",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:walljump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:peggy",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:penny",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 cans",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 cans",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:push",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:13 burgers",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:dbjump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:sarge fan",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:walljump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:rico",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:crawl",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:zoe",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:stomp",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:5 onion coins",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:dbjump",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:12 burgers",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [
        "move:glide",
        "flag:hasChar",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level9",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:papa louie",
    ],
  },
  {
    "room": "level10",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:xandra",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [
        "flag:hasChar",
      ],
    ],
    "receive": [
      "char:marty",
      "char:rita",
    ],
  },
]

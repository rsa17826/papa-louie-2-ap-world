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
      "level:level0",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level0",
      "level:level1",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level1",
      "level:level2",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level2",
      "level:level3",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level3",
      "level:level4",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level4",
      "level:level5",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level5",
      "level:level6",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level6",
      "level:level7",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level7",
      "level:level8",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level8",
      "level:level9",
    ],
  },
  {
    "room": "level9",
    "requires": [
      [],
    ],
    "receive": [
      "flag:beat level9",
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
    "room": "level0",
    "requires": [
      [],
    ],
    "receive": [
      "char:prudence",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [],
    ],
    "receive": [
      "char:taylor",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "char:clover",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [],
    ],
    "receive": [
      "collectCheck:5 red coins",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [],
    ],
    "receive": [
      "collectCheck:3 burgers",
    ],
  },
  {
    "room": "level0",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "char:big pauly",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "char:mindy",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:fizzocan",
    ],
  },
  {
    "room": "level1",
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
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "collectCheck:5 flowers",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:11 burgers",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [],
    ],
    "receive": [
      # REVIEW can't kill saucers in any way so force other char than this one if that kill required
      "char:boomer",
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
      "char:kahuna",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "char:professor fitz",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:5 helmets",
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
      "collectCheck:11 burgers",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [],
    ],
    "receive": [
      "char:georgito",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "char:foodini",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "char:yippy",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:5 purple coins",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "collectCheck:6 burgers",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:push",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [],
    ],
    "receive": [
      "char:scooter",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "char:kingsley",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:push",
      ],
    ],
    "receive": [
      "char:connor",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:5 worms",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:8 burgers",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:walljump",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": [
      "char:james",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:push",
      ],
    ],
    "receive": [
      "char:greg",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:walljump",
      ],
    ],
    "receive": [
      "char:captain cori",
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
      "collectCheck:5 balloons",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "collectCheck:10 burgers",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [],
    ],
    "receive": [
      "char:ninjoy",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:walljump",
      ],
    ],
    "receive": [
      "char:peggy",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "char:penny",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:5 cans",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:5 cans",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:push",
      ],
    ],
    "receive": [
      "collectCheck:13 burgers",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [],
    ],
    "receive": [
      "char:sarge fan",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:walljump",
      ],
    ],
    "receive": [
      "char:rico",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "char:zoe",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "collectCheck:5 onion coins",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:dbjump",
      ],
    ],
    "receive": [
      "collectCheck:12 burgers",
    ],
  },
  {
    "room": "level7",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "collectCheck:100 coins",
    ],
  },
  {
    "room": "level8",
    "requires": [
      [],
    ],
    "receive": [
      "char:papa louie",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [],
    ],
    "receive": [
      # TODO where this at?
      "char:xandra",
    ],
  },
  {
    "room": "menu",
    "requires": [
      [],
    ],
    "receive": [
      "char:marty",
      "char:rita",
    ],
  },
]

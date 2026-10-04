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
      "level:level10",
    ],
  },
  {
    "room": "level10",
    "requires": [
      [],
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
        "char:rita",
        "char:prudence",
        "char:taylor",
        "char:clover",
        "char:mindy",
        "char:akari",
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
        "char:kahuna",
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
        "char:penny",
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
        "char:captain cori",
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
        "char:connor",
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
        "char:yippy",
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
        "char:professor fitz",
        "char:foodini",
        "char:papa louie",
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
      "char:taylor",
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
      "char:clover",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "?:5 red coins",
    ],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": [
      "?:3 burgers",
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
      "?:100 coins",
    ],
  },
  {
    "room": "level2",
    "requires": [
      [],
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
      ],
    ],
    "receive": [
      "char:mindy",
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
      "?:5 flowers",
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
      "?:11 burgers",
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
      "?:100 coins",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
      ],
    ],
    "receive": [
      "char:boomer",
    ],
  },
  {
    "room": "level3",
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
    "room": "level3",
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
    "room": "level3",
    "requires": [
      [
        "move:stomp",
      ],
    ],
    "receive": [
      "?:5 helmets",
    ],
  },
  {
    "room": "level3",
    "requires": [
      [
        "move:glide",
      ],
    ],
    "receive": [
      "?:11 burgers",
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
      "?:100 coins",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
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
      ],
    ],
    "receive": [
      "?:5 purple coins",
    ],
  },
  {
    "room": "level4",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "?:6 burgers",
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
      "?:100 coins",
    ],
  },
  {
    "room": "level5",
    "requires": [
      [
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
      ],
    ],
    "receive": [
      "?:5 worms",
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
      "?:8 burgers",
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
      "?:100 coins",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
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
      ],
    ],
    "receive": [
      "?:5 balloons",
    ],
  },
  {
    "room": "level6",
    "requires": [
      [
        "move:crawl",
      ],
    ],
    "receive": [
      "?:10 burgers",
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
      "?:100 coins",
    ],
  },
]

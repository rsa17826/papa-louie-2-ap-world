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
]
# TODO
# move:push
# move:key
# move:fan

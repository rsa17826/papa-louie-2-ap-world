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
]
# TODO
# move:push
# move:key
# move:fan

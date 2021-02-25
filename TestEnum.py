from enum import Enum

class Color(Enum):
   Red = 1
   Green = 2

color = Color.Red
if color == Color.Red:
  print("Yes")
else:
  print("No")
### 8-16. Imports

import tshirt_maker
import tshirt_maker as tm

from tshirt_maker import make_shirt
from tshirt_maker import make_shirt as ms_fn

from tshirt_maker import *

tshirt_maker.make_shirt("s", "Bachelors Royale")
tm.make_shirt("M", "Squad leader")
make_shirt("L", "Bachelors party")
ms_fn("XL", "Losers team")
make_shirt("xxl", "Game over")
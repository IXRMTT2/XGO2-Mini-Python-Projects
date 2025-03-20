from xgolib import XGO
from xgoedu import XGOEDU
XGO_mini = XGO("xgomini")
XGO_edu = XGOEDU()

XGO_mini.turn(-100)
time.sleep(5)
XGO_mini.turn(0)
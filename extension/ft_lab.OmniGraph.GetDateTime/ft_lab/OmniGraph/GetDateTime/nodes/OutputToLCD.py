"""
Time output to LCD (hh:mm).
"""
from pxr import Usd, UsdGeom, UsdPhysics, UsdShade, Sdf, Gf, Tf
import numpy as np
import omni.ext

class OutputToLCD:
    @staticmethod
    def compute(db) -> bool:
        try:
            hour   = db.inputs.d1_hour
            minute = db.inputs.d2_minute
            second = db.inputs.d3_second

            # xABCDEFG => 0b01111110 = 0x7e = '0'
            nameList = ["A", "B", "C", "D", "E", "F", "G"]
            numMaskList = [0x7e, 0x30, 0x6d, 0x79, 0x33, 0x5b, 0x5f, 0x70, 0x7f, 0x7b]

            # Get stage.
            stage = omni.usd.get_context().get_stage()

            # Show/hide "AM"
            if db.inputs.c1_amPrim != None and db.inputs.c1_amPrim != "":
                prim = stage.GetPrimAtPath(db.inputs.c1_amPrim)
                if prim.IsValid():
                    primImageable = UsdGeom.Imageable(prim)
                    primImageable.GetVisibilityAttr().Set('inherited' if hour < 12 else 'invisible')

            # Show/hide "PM"
            if db.inputs.c2_pmPrim != None and db.inputs.c2_pmPrim != "":
                prim = stage.GetPrimAtPath(db.inputs.c2_pmPrim)
                if prim.IsValid():
                    primImageable = UsdGeom.Imageable(prim)
                    primImageable.GetVisibilityAttr().Set('inherited' if (hour >= 12) else 'invisible')


            # Hour : 10th digit.
            hour12 = hour if (hour < 12) else (hour - 12)
            if db.inputs.a1_hourNum10Prim != None and db.inputs.a1_hourNum10Prim != "":
                basePrimPath = db.inputs.a1_hourNum10Prim
                shiftV = 0x40
                maskV  = numMaskList[(int)(hour12 / 10) % 10]
                for i in range(7):
                    primPath = f"{basePrimPath}/{nameList[i]}"
                    prim = stage.GetPrimAtPath(primPath)
                    if prim.IsValid():
                        primImageable = UsdGeom.Imageable(prim)
                        primImageable.GetVisibilityAttr().Set('inherited' if ((maskV & shiftV) != 0) else 'invisible')
                    shiftV >>= 1

            # Hour : 1th digit.
            if db.inputs.a2_hourNum1Prim != None and db.inputs.a2_hourNum1Prim != "":
                basePrimPath = db.inputs.a2_hourNum1Prim
                shiftV = 0x40
                maskV  = numMaskList[(int)(hour12) % 10]
                for i in range(7):
                    primPath = f"{basePrimPath}/{nameList[i]}"
                    prim = stage.GetPrimAtPath(primPath)
                    if prim.IsValid():
                        primImageable = UsdGeom.Imageable(prim)
                        primImageable.GetVisibilityAttr().Set('inherited' if ((maskV & shiftV) != 0) else 'invisible')
                    shiftV >>= 1

            # Minute : 10th digit.
            if db.inputs.b1_minuteNum10Prim != None and db.inputs.b1_minuteNum10Prim != "":
                basePrimPath = db.inputs.b1_minuteNum10Prim
                shiftV = 0x40
                maskV  = numMaskList[(int)(minute / 10) % 10]
                for i in range(7):
                    primPath = f"{basePrimPath}/{nameList[i]}"
                    prim = stage.GetPrimAtPath(primPath)
                    if prim.IsValid():
                        primImageable = UsdGeom.Imageable(prim)
                        primImageable.GetVisibilityAttr().Set('inherited' if ((maskV & shiftV) != 0) else 'invisible')
                    shiftV >>= 1

            # Minute : 1th digit.
            if db.inputs.b2_minuteNum1Prim != None and db.inputs.b2_minuteNum1Prim != "":
                basePrimPath = db.inputs.b2_minuteNum1Prim
                shiftV = 0x40
                maskV  = numMaskList[(int)(minute) % 10]
                for i in range(7):
                    primPath = f"{basePrimPath}/{nameList[i]}"
                    prim = stage.GetPrimAtPath(primPath)
                    if prim.IsValid():
                        primImageable = UsdGeom.Imageable(prim)
                        primImageable.GetVisibilityAttr().Set('inherited' if ((maskV & shiftV) != 0) else 'invisible')
                    shiftV >>= 1

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True



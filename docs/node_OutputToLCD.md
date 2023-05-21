# OutputToLCD

This node controls a virtual 7-segment LED LCD screen.    
![outputToLCD_icon.png](./images/outputToLCD_icon.png)     

## OutputToLCD.ogn

```json
{
    "OutputToLCD": {
        "version": 1,
        "categories": "examples",
        "description": "Time output to LCD (hh:mm).",
        "language": "Python",
        "metadata": {
            "uiName": "Time output to LCD (hh:mm)"
        },
        "inputs": {
            "a1_hourNum10Prim": {
                "type": "token",
                "description": "Tenth digit of the hour Prim",
                "metadata": {
                    "uiName": "HourNum10 Prim"
                }
            },
            "a2_hourNum1Prim": {
                "type": "token",
                "description": "First digit of the hour Prim",
                "metadata": {
                    "uiName": "HourNum1 Prim"
                }
            },
            "b1_minuteNum10Prim": {
                "type": "token",
                "description": "Tenth digit of the minute Prim",
                "metadata": {
                    "uiName": "MinuteNum10 Prim"
                }
            },
            "b2_minuteNum1Prim": {
                "type": "token",
                "description": "First digit of the minute Prim",
                "metadata": {
                    "uiName": "MinuteNum1 Prim"
                }
            },
            "c1_amPrim": {
                "type": "token",
                "description": "AM Prim",
                "metadata": {
                    "uiName": "AM Prim"
                }
            },
            "c2_pmPrim": {
                "type": "token",
                "description": "PM Prim",
                "metadata": {
                    "uiName": "PM Prim"
                }
            },
            "d1_hour": {
                "type": "int",
                "description": "Hour",
                "default": 0,
                "metadata": {
                    "uiName": "Hour"
                }
            },
            "d2_minute": {
                "type": "int",
                "description": "Minute",
                "default": 0,
                "metadata": {
                    "uiName": "Minute"
                }
            },
            "d3_second": {
                "type": "int",
                "description": "Second",
                "default": 0,
                "metadata": {
                    "uiName": "Second"
                }
            }
        },
        "outputs": {
        }
    }
}
```

![OutputToLCD_node.png](./images/OutputToLCD_node.png)     

### Inputs

|Attribute name|Type|UI name|Description|    
|---|---|---|---|    
|a1_hourNum10Prim|token|HourNum10 Prim|Tenth digit of the hour Prim|    
|a2_hourNum1Prim|token|HourNum1 Prim|First digit of the hour Prim|    
|b1_minuteNum10Prim|token|MinuteNum10 Prim|Tenth digit of the minute Prim|    
|b2_minuteNum1Prim|token|MinuteNum1 Prim|First digit of the minute Prim|    
|c1_amPrim|token|AM Prim|AM Prim|    
|c2_pmPrim|token|PM Prim|PM Prim|    
|d1_hour|int|Hour|Hour|    
|d2_minute|int|Minute|Minute|    
|d3_second|int|Second|Second|    

The "a1_" or "b1_" at the beginning of the attribute name is used to display the data in ascending order when it is displayed in a graph.     

Those that specify a "token" type will be connected to the Prim path.     
In total, 6 Prims will be connected to this node.     
![GetDateTime_Digital_01.jpg](../images/GetDateTime_Digital_01.jpg)    
Four prims that imitate "7-segment LEDs" are placed as numerical components.     
One of the "7-segment LEDs" consists of four components, A, B, C, D, E, F, and G, as shown below.     
![GetDateTime_Digital_02.jpg](../images/GetDateTime_Digital_02.jpg)    
The same A, B, C, D, E, F, and G are given for the child Prim names.    
This is turned On/Off to indicate the numerical value.     

The numbers were expressed in 8 bits as follows.      
The lower 7 bits are assigned to ABCDEFG respectively.     

|Image|Bit value|Hexadecimal|     
|---|---|---|     
|<img src="./images/num_0.jpg" height=40 />|01111110|0x7e|     
|<img src="./images/num_1.jpg" height=40 />|00110000|0x30|     
|<img src="./images/num_2.jpg" height=40 />|01101101|0x6d|     
|<img src="./images/num_3.jpg" height=40 />|01111001|0x79|     
|<img src="./images/num_4.jpg" height=40 />|00110011|0x33|     
|<img src="./images/num_5.jpg" height=40 />|01011011|0x5b|     
|<img src="./images/num_6.jpg" height=40 />|01011111|0x5f|     
|<img src="./images/num_7.jpg" height=40 />|01110000|0x70|     
|<img src="./images/num_8.jpg" height=40 />|01111111|0x7f|     
|<img src="./images/num_9.jpg" height=40 />|01111011|0x7b|     

d1_hour, d2_minute, and d3_second are entered as hours, minutes, and seconds.      

## OutputToLCD.py

```python
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
```

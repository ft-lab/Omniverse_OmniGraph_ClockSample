# RotationByTime

Given an hour, minute, and second, returns the XYZ of each rotation(degree).      
![rotationByTime_icon.png](./images/rotationByTime_icon.png)     

## RotationByTime.json

```json
{
    "RotationByTime": {
        "version": 1,
        "categories": "examples",
        "description": "Rotation mechanism by time.",
        "language": "Python",
        "metadata": {
            "uiName": "Rotation By Time"
        },
        "inputs": {
            "a1_defaultRotateXYZ": {
                "type": "float3",
                "description": "Default rotateXYZ",
                "default": [0.0, 0.0, 0.0],
                "metadata": {
                    "uiName": "Default rotateXYZ"
                }
            },
            "a2_rotationAxis": {
                "type": "int",
                "description": "Rotation axis (0:X, 0:Y, 0:Z)",
                "default": 0,
                "metadata": {
                    "uiName": "Rotation axis"
                }
            },
            "b1_hour": {
                "type": "int",
                "description": "Hour",
                "default": 0,
                "metadata": {
                    "uiName": "Hour"
                }
            },
            "b2_minute": {
                "type": "int",
                "description": "Minute",
                "default": 0,
                "metadata": {
                    "uiName": "Minute"
                }
            },
            "b3_second": {
                "type": "int",
                "description": "Second",
                "default": 0,
                "metadata": {
                    "uiName": "Second"
                }
            }
        },
        "outputs": {
            "a1_hourRotateXYZ": {
                "type": "float3",
                "description": "Hour rotateXYZ",
                "default": [0.0, 0.0, 0.0],
                "metadata": {
                    "uiName": "Hour RotateXYZ"
                }
            },
            "a2_minuteRotateXYZ": {
                "type": "float3",
                "description": "Minute rotateXYZ",
                "default": [0.0, 0.0, 0.0],
                "metadata": {
                    "uiName": "Minute RotateXYZ"
                }
            },
            "a3_secondRotateXYZ": {
                "type": "float3",
                "description": "Second rotateXYZ",
                "default": [0.0, 0.0, 0.0],
                "metadata": {
                    "uiName": "Second RotateXYZ"
                }
            }
        }
    }
}
```
![RotationByTime_node.png](./images/RotationByTime_node.png)     

### Inputs

|Attribute name|Type|UI name|Description|    
|---|---|---|---|    
|a1_defaultRotateXYZ|float3|Default rotateXYZ|Default rotateXYZ|    
|a2_rotationAxis|int|Rotation axis|Rotation axis (0:X, 1:Y, 2:Z)|    
|b1_hour|int|Hour|Hour|    
|b2_minute|int|Minute|Minute|    
|b3_second|int|Second|Second|    

The "a1_" or "b1_" at the beginning of the attribute name is used to display the data in ascending order when it is displayed in a graph.     

"a1_defaultRotateXYZ" is the initial rotation value of the clock hands provided in the 3D model.     
![RotationByTime_img_01.jpg](./images/RotationByTime_img_01.jpg)    
"a2_rotationAxis" is the axis of rotation (0:X, 1:Y, 2:Z).     

b1_hour, b2_minute, and b3_second are entered as hours, minutes, and seconds.      


### Outputs

|Attribute name|Type|UI name|Description|    
|---|---|---|---|    
|a1_hourRotateXYZ|float3|Hour rotateXYZ|Hour rotateXYZ|    
|a2_minuteRotateXYZ|float3|Minute rotateXYZ|Minute rotateXYZ|    
|a3_secondRotateXYZ|float3|Second rotateXYZ|Second rotateXYZ|    




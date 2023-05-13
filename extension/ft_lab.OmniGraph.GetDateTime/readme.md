# ft_lab.OmniGraph.GetDateTime

"ft_lab.OmniGraph.GetDateTime" は現在の日付と時間を取得するOmniGraphのカスタムノードのサンプルです。    
![data/preview.png](data/preview.png)     

[GetDateTime.ogn](ft_lab/OmniGraph/GetDateTime/nodes/GetDateTime.ogn)では以下のように指定。      
入力値はなく、日付と時間の情報が出力されるだけの構成になります。     

```json
{
    "GetDateTime": {
        "version": 1,
        "categories": "examples",
        "description": "Get datetime node.",
        "language": "Python",
        "metadata": {
            "uiName": "Get DateTime"
        },
        "inputs": {
        },
        "outputs": {
            "year": {
                "type": "int",
                "description": "year",
                "default": 2000,
                "metadata": {
                    "uiName": "Year"
                }
            },
            "month": {
                "type": "int",
                "description": "month",
                "default": 1,
                "metadata": {
                    "uiName": "Month"
                }
            },
            "day": {
                "type": "int",
                "description": "day",
                "default": 1,
                "metadata": {
                    "uiName": "Day"
                }
            },
            "hour": {
                "type": "int",
                "description": "hour",
                "default": 1,
                "metadata": {
                    "uiName": "Hour"
                }
            },
            "minute": {
                "type": "int",
                "description": "minute",
                "default": 1,
                "metadata": {
                    "uiName": "Minute"
                }
            },
            "second": {
                "type": "int",
                "description": "second",
                "default": 1,
                "metadata": {
                    "uiName": "Second"
                }
            }
        }
    }
}
```


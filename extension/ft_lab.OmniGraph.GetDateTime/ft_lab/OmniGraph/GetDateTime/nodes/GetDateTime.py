"""
Get date time.
"""
import numpy as np
import omni.ext
import datetime

class GetDateTime:
    @staticmethod
    def compute(db) -> bool:
        try:
            # Get current date and time.
            now = datetime.datetime.now()
            db.outputs.a1_year   = now.year
            db.outputs.a2_month  = now.month
            db.outputs.a3_day    = now.day
            db.outputs.b1_hour   = now.hour
            db.outputs.b2_minute = now.minute
            db.outputs.b3_second = now.second

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True



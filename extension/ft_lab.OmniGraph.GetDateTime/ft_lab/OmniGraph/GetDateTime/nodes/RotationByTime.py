"""
Rotation by time.
"""
import numpy as np
import omni.ext

class RotationByTime:
    @staticmethod
    def compute(db) -> bool:
        try:
            # Calculate clock rotation from seconds.
            if db.inputs.a2_rotationAxis >= 0 and db.inputs.a2_rotationAxis <= 2:
                v = db.outputs.a3_secondRotateXYZ
                v[0] = db.inputs.a1_defaultRotateXYZ[0]
                v[1] = db.inputs.a1_defaultRotateXYZ[1]
                v[2] = db.inputs.a1_defaultRotateXYZ[2]
                v[db.inputs.a2_rotationAxis] = ((float)(db.inputs.b3_second) / 60.0) * 360.0

            # Calculate clock rotation from minutes.
            if db.inputs.a2_rotationAxis >= 0 and db.inputs.a2_rotationAxis <= 2:
                v = db.outputs.a2_minuteRotateXYZ
                v[0] = db.inputs.a1_defaultRotateXYZ[0]
                v[1] = db.inputs.a1_defaultRotateXYZ[1]
                v[2] = db.inputs.a1_defaultRotateXYZ[2]
                v[db.inputs.a2_rotationAxis] = ((float)(db.inputs.b2_minute * 60.0 + db.inputs.b3_second) / (60.0 * 60.0)) * 360.0

            # Calculate clock rotation from hours.
            if db.inputs.a2_rotationAxis >= 0 and db.inputs.a2_rotationAxis <= 2:
                v = db.outputs.a1_hourRotateXYZ
                v[0] = db.inputs.a1_defaultRotateXYZ[0]
                v[1] = db.inputs.a1_defaultRotateXYZ[1]
                v[2] = db.inputs.a1_defaultRotateXYZ[2]
                v[db.inputs.a2_rotationAxis] = ((float)(db.inputs.b1_hour * 60.0 + db.inputs.b2_minute) / (60.0 * 24.0)) * 360.0 * 2.0

        except TypeError as error:
            db.log_error(f"Processing failed : {error}")
            return False
    
        return True



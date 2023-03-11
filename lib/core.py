import dataclasses

def continuous_torque(rpm):
    base_continuous_torque = 170
    knee_rpm = 5000
    if rpm < knee_rpm:
        return base_continuous_torque
    else:
        return  base_continuous_torque - 0.0025 * (rpm - knee_rpm)

def max_torque(rpm):
    base_max_torque = 320
    knee_rpm = 2750
    if rpm < knee_rpm:
        return base_max_torque
    else:
        return base_max_torque - .03 * (rpm - knee_rpm)

power_constant = 9.5488

def continuous_power(rpm):
    return continuous_torque(rpm) * rpm / power_constant

def max_power(rpm):
    return max_torque(rpm) * rpm / power_constant

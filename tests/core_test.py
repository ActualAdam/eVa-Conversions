import pytest
from lib import core

knee = 5000
def test_continuous_torque_should_be_base_torque_below_the_knee():
    base_torque = 170
    assert core.continuous_torque_at_rpm(0) == 170
    assert core.continuous_torque_at_rpm(knee - 1) == 170
    assert core.continuous_torque_at_rpm(knee) == 170

# only run createsubs in the unix version of micropython
import sys
import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="requires linux")
def test_101():
    assert True

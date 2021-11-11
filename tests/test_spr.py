import sys
import os
import pytest
import subprocess

# only run createsubs in the unix version of micropython
@pytest.mark.skipif(sys.platform == "win32", reason="requires linux")
def test_createstubs():
    # Use temp_path to generate stubs
    # demo test hardcoded for ubuntu 20.04
    scriptfolder = os.path.abspath("./board")
    cmd = [
        os.path.abspath("tests/tools/micropython_v1_16"),
        "main.py",
    ]
    try:
        subproc = subprocess.run(
            cmd,
            cwd=scriptfolder,
            timeout=100000,
            capture_output=True,
        )
        print(subproc.stderr)
        assert subproc.returncode == 0, "createstubs ran with an error :" + str(
            subproc.stderr
        )
    except ImportError as e:
        print(e)
        pass
    # did it run without error ?

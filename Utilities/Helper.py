import Utilities.Logger as L
import sys


def assert_test(condition, fail_str, success_str = "*******Completed successfully*******"):
    assert condition, L.logging.error(fail_str)
    L.logging.info(success_str)



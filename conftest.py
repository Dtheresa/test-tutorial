# import pytest
# import time


def pytest_addoption(parser):
    parser.addoption("--host",
                     action="store",
                     default="http://jsonplaceholder.typicode.com")

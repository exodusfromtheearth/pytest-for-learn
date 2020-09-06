# -*- coding: utf-8 -*-
import os


def filepath(fileroot="data", filename="test.yaml"):
    return os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))), fileroot, filename
    )
# dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(dir)
# testdir = os.path.join(dir, "data", "test.yaml")
# print(testdir)
# print(filepath("data/Arrow", "fundingcase.yaml"))




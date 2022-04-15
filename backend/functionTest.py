import pytest
import sys

import functions

def minIssueArea_test():
    responses = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    assert functions.findIssueAvg(responses) == ["Criminal Procedures", "Law" ]
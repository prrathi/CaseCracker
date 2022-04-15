import pytest
import sys
sys.path.insert(1, "../")
import functions

# Test for the function finding the two cloest issue areas for a given justice
def test_minIssueArea():
    selfResponses = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1]
    targetJustice = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1]
    assert functions.minIssueArea(selfResponses, targetJustice) == ["Criminal Procedures", "Civil Rights" ]

def test_minIssueArea2():
    responses = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1]
    targetJustice = [2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2]
    assert functions.minIssueArea(responses, targetJustice) == ["Criminal Procedures", "Civil Rights" ]


def test_minIssueArea3():
    responses = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1]
    targetJustice = [2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1]
    assert functions.minIssueArea(responses, targetJustice) == ["Civil Rights", "Privacy" ]

def test_minIssueArea4():
    responses = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    targetJustice = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    assert functions.minIssueArea(responses, targetJustice) == ["Criminal Procedures", "Civil Rights" ]


def test_findClosestJustice():
    responses = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    assert functions.findClosestJustice(responses) == [['Byron White', 'Privacy', 'Civil Rights'], ['Felix Frankfurter', 'Civil Rights', 'Criminal Procedures'], ['John Harlan', 'Civil Rights', 'Criminal Procedures']]

def test_findClosestJustice1():
    selfResponses = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1]
    issueAverages = functions.findIssueAvg(selfResponses)
    closestJustice = functions.findClosestJustice(issueAverages)
    assert functions.findClosestJustice(issueAverages) == [['John Harlan', 'Criminal Procedures', 'Due Process'], ['Abe Fortas', 'Due Process', 'Criminal Procedures'], ['Felix Frankfurter', 'First Amendment', 'Due Process']]
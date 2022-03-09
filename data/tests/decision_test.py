import pytest
import sys
sys.path.insert(1, "../")
import decision

def test_validateDecisionTrue():
    # 2020-073
    test_case_1 = {
            'majority_votes': 9,
            'minority_votes': 0,
            'petitioner_wins': True
        }

    # 2015-072
    test_case_2 = {
        'majority_votes': 5, 
        'minority_votes': 3, 
        'petitioner_wins': True
        }

    cases_dict = decision.match_metadata_to_transcript()

    assert cases_dict['2020-073'] == test_case_1
    assert cases_dict['2015-072'] == test_case_2
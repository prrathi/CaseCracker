import pandas as pd
import numpy as np

def match_metadata_to_transcript():

    # Reads the case metadata file
    df = pd.read_csv("../SCDB_2021_01_caseCentered_Citation.csv", encoding= 'unicode_escape')

    # Creates a dictionary to store only the metadata we're looking for
    cases_dict = {}

    # Iterates through the columns to grab only the majority votes, minority votes, and which side of the case won.
    for index, row in df.iterrows():
        if row["caseId"] not in cases_dict.keys():
            cases_dict[row["caseId"]] = {
                "majority_votes": row["majVotes"],
                "minority_votes": row["minVotes"],
                "petitioner_wins": True if row["partyWinning"] == 1 else False
            }

    # For future use, we can use cases_dict to map a given case's metadata to its transcript

    return cases_dict
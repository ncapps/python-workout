import glob
import json
from collections import defaultdict


def print_scores(dirname):

    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = defaultdict(list)

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            avg_score = sum(subject_scores) / len(subject_scores)

            print(
                f'\t{subject}:',
                f'min {min_score}, '
                f'max {max_score}, '
                f'avg {avg_score}'
            )


print_scores('ch05_files/scores')

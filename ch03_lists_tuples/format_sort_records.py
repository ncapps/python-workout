from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people):
    if not people:
        return people
    # sort people alphabetically by last name
    output = []
    for first_name, last_name, hours_to_arrival in sorted(people, key=itemgetter(1)):
        output.append(f'{last_name:10} {first_name:10} {hours_to_arrival:5.2f}')
    return output

print('\n'.join(format_sort_records(PEOPLE)))

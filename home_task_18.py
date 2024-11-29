'''# Any tester can be listed in one or more groups.
# Create the following sorted lists:
# - all testers in the team
# - testers who can only write scripts
# - testers who are at work today
# - testers who could write and review scripts, and are at work today
# The results should be sorted.'''

# - all testers in the team
test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = test_scripters + test_design_writers + reviewers + out_of_office_today
sorted_all_testers = []

for tester in all_testers:
    if tester not in sorted_all_testers:
        sorted_all_testers.append(tester)

sorted_all_testers.sort()
print(sorted_all_testers)

# - testers who can only write scripts
test_scripters_only = []
for scripter in test_scripters:
    if scripter in test_design_writers or scripter in reviewers:
        continue
    test_scripters_only.append(scripter)
print(test_scripters_only)

# - testers who are at work today

testers_working = [tester for tester in sorted_all_testers if tester not in out_of_office_today]
print(testers_working)

# - testers who could write and review scripts, and are at work today

scripters_reviewers_at_work = [tester for tester in sorted_all_testers if tester not in out_of_office_today and (tester in test_scripters or tester in reviewers)]
print(scripters_reviewers_at_work)

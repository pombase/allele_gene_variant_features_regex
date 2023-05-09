import re

# Define the regexes
regex_dict = {}
regex_dict['regex_wt'] = '\+'
regex_dict['regex_deletion'] = '\u0394'
regex_dict['regex_partial_deletion_kept'] = '\(\d+-\d+\)'
regex_dict['regex_partial_deletion_removed'] = '\u0394\(\d+-\d+\)'
regex_dict['regex_delins'] = '-[A-Z]+\d+[A-Z*]+(,[A-Z]+\d+[A-Z*]+)*'
regex_dict['regex_delins_no_dash'] = '[A-Z]+\d+[A-Z*]+(,[A-Z]+\d+[A-Z*]+)*'

# Below we re-use the regexes above to define more complex regexes

# This combination is mentioned in the text of the paper
regex_dict['regex_delins_and_partial_deletion'] = '({}|{}){}'.format(regex_dict['regex_partial_deletion_kept'], regex_dict['regex_partial_deletion_removed'], regex_dict['regex_delins'])

first_composed_regex = '({}|{}|{})'.format(regex_dict['regex_partial_deletion_removed'], regex_dict['regex_partial_deletion_kept'], regex_dict["regex_delins"])
second_composed_regex = '({}|{}|{})'.format(regex_dict['regex_partial_deletion_removed'], regex_dict['regex_delins_no_dash'], regex_dict["regex_deletion"])
regex_dict['regex_CTD'] = '{}?-CTD-({}(\(r\d+-r\d+(-\d+)?\))*)+'.format(first_composed_regex, second_composed_regex)

# Define the test cases
cases_dict = {}
cases_dict['regex_wt'] = ['ase1+']
cases_dict['regex_deletion'] = ['ase1\u0394']
cases_dict['regex_partial_deletion_kept'] = ['ase1(10-200)']
cases_dict['regex_partial_deletion_removed'] = ['ase1\u0394(10-200)']
cases_dict['regex_delins'] = ['ase1-P114PVPAL', 'ase1-P114A,Q117A', 'ase1-P114*', 'ase1-PLI114AAA', 'ase1-PLI114LAVKK']
cases_dict['regex_delins_and_partial_deletion'] = ['ase1(10-200)-P224A,Q337A,L400*']
cases_dict['regex_CTD'] = ['ase1-CTD-Y1F',
                            'ase1-CTD-Y1F(r1-r12)',
                            'ase1-CTD-\u0394(r11-r29)',
                            'ase1-CTD-Y1F(r1-r29-2)',
                            'ase1-CTD-S5A(r1-r12)\u0394(r13-r29)',
                            'ase1\u0394(1-100)-CTD-\u0394(r11-r29)',
                            'ase1-N494D-CTD-\u0394(r11-r29)',]


# Switch case on the keys of regex_dict
for key in cases_dict:
    # Switch case on the values of cases_dict
    for value in cases_dict[key]:

        # Test if the regex matches the value
        assert re.match('ase1' + regex_dict[key], value) is not None, f'{value} does not match {regex_dict[key]}'

print('All tests passed! :)')
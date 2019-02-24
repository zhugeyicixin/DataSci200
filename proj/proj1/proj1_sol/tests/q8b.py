test = {   'name': 'q8b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "sum(inspections_by_id_and_year['count'])\n"
                                               '14222',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'list(inspections_by_id_and_year.index.names)\n'
                                               "['business_id', 'year']",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'inspections_by_id_and_year_sol '
                                               '= '
                                               "ins.groupby([ins['business_id'], "
                                               'ins[\'year\']]).size().sort_values(ascending=False).rename("count").to_frame();\n'
                                               '>>> '
                                               'inspections_by_id_and_year_sol.equals(inspections_by_id_and_year)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

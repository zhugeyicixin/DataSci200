test = {   'name': 'q8c1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(scores_pairs_by_business, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'scores_pairs_by_business.columns\n'
                                               "Index(['score_pair'], "
                                               "dtype='object')",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # SOLUTION 1;\n'
                                               ">>> ins2016 = ins[ins['year'] "
                                               '== 2016];\n'
                                               '>>> \n'
                                               '>>> '
                                               'scores_pairs_by_business_sol_1 '
                                               '= '
                                               "(ins2016.sort_values('date')\n"
                                               '...                             '
                                               ".loc[:, ['business_id', "
                                               "'score']]\n"
                                               '...                             '
                                               ".groupby('business_id')\n"
                                               '...                             '
                                               '.filter(lambda group: '
                                               'len(group) == 2)\n'
                                               '...                             '
                                               ".groupby('business_id')\n"
                                               '...                             '
                                               '.agg(list)\n'
                                               '...                             '
                                               ".rename(columns={'score':'score_pair'}));\n"
                                               '>>> \n'
                                               '>>> \n'
                                               '>>> # SOLUTION 2;\n'
                                               '>>> '
                                               'scores_pairs_by_business_sol_2 '
                                               '= '
                                               "(ins2016.sort_values('date')\n"
                                               '...                             '
                                               ".groupby('business_id')\n"
                                               '...                             '
                                               '.filter(lambda group: '
                                               'len(group) == 2)\n'
                                               '...                             '
                                               ".groupby('business_id')\n"
                                               '...                             '
                                               ".agg({'score': lambda group: "
                                               'group.tolist()})\n'
                                               '...                             '
                                               ".rename(columns={'score':'score_pair'}));\n"
                                               '>>> \n'
                                               '>>> # Sort by index for '
                                               'comparison;\n'
                                               '>>> '
                                               'scores_pairs_by_business_sol_1.sort_index(inplace=True);\n'
                                               '>>> '
                                               'scores_pairs_by_business_sol_2.sort_index(inplace=True);\n'
                                               '>>> '
                                               'scores_pairs_by_business.sort_index(inplace=True);\n'
                                               '>>> \n'
                                               '>>> '
                                               'scores_pairs_by_business_sol_1.equals(scores_pairs_by_business) '
                                               'or \\\n'
                                               '...     '
                                               'scores_pairs_by_business_sol_2.equals(scores_pairs_by_business)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

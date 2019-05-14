test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(missing_counts, '
                                               'pd.Series)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> missing_counts.size # '
                                               'Should have 84 total features '
                                               '(82 features + TotalBathrooms '
                                               '+ in_rich_neighborhood)\n'
                                               '84',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'set(missing_counts.index.values) '
                                               '== '
                                               'set(training_data.columns.values)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "missing_counts.loc['Fireplace_Qu'] "
                                               '# Make sure you are '
                                               'calculating the counts '
                                               'correctly\n'
                                               '975',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> missing_counts.iloc[0] # '
                                               'Make sure you are sorting '
                                               'correctly\n'
                                               '1991',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

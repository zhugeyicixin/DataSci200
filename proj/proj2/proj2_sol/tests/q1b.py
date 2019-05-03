test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(first_ham) > 0 and '
                                               "first_ham[:0] == ''\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(first_spam) > 0 and '
                                               "first_spam[:0] == ''\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "original_training_data.loc[original_training_data['spam'] "
                                               "== 0, 'email'].iloc[0] in "
                                               'first_ham\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "original_training_data.loc[original_training_data['spam'] "
                                               "== 1, 'email'].iloc[0] in "
                                               'first_spam\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

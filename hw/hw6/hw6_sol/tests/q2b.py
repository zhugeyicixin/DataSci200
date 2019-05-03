test = {   'name': 'q2b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "sum(training_data['Fireplace_Qu'] "
                                               "== 'No Fireplace') # Make sure "
                                               "you've replaced all the "
                                               "missing values with 'No "
                                               "Fireplace'\n"
                                               '975',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'Fireplace_Qu'].isnull() == 0) "
                                               "# Make sure you haven't "
                                               'introduced anything strange\n'
                                               '1998',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'Fireplace_Qu'] == "
                                               "'Excellent')\n"
                                               '30',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

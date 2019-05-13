test = {   'name': 'q1c',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> manhattan_taxi.shape\n'
                                               '(82800, 9)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "sum(manhattan_taxi['duration'])\n"
                                               '54551565',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "manhattan_taxi.iloc[0,:]['duration']\n"
                                               '981',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "manhattan_taxi.iloc[0,:]['passengers'];\n"
                                               '>>> \n'
                                               '>>> # NOTE: The saved '
                                               'manhattan_taxi.csv is '
                                               'watermarked by setting this '
                                               'value to 2 instead of 1.;\n'
                                               '>>> #       Running the '
                                               'solution notebook will '
                                               'incorrectly set this value to '
                                               '2, so make sure the;\n'
                                               '>>> #       test result is set '
                                               'to 1 when evaluating this '
                                               'hidden test.;\n'
                                               '>>> #       The reason this '
                                               'difference exists is to make '
                                               "sure that students don't solve "
                                               'the ;\n'
                                               '>>> #       problem just by '
                                               'loading the provided data '
                                               'file.\n'
                                               '2',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> result_serial == '
                                               'result_parallel\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> time_serial > '
                                               'time_parallel # '
                                               'reduce_parallel is slower than '
                                               'reduce_serial\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> time_serial > 2 * '
                                               'time_parallel # '
                                               'reduce_parallel is too slow \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

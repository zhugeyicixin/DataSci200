test = {   'name': 'q4h',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "all(bus_multi_sample.isin(bus['name']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'len(list(bus_multi_sample)) == '
                                               'len(set(list(bus_multi_sample)))\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'len(list(bus_multi_sample.keys())) '
                                               '==  '
                                               'len(list(bus_multi_sample.keys()))\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

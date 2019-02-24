test = {   'name': 'q4c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "all(bus_strat_sample.isin(bus['name']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(bus_strat_sample) == '
                                               'len(bus.postal_code_5.unique())\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> # Note: this is the only '
                                               'name in 94120, so it must be '
                                               'in the sample.;\n'
                                               ">>> 'CALIFORNIA PACIFIC "
                                               'MEDICAL CTR - HOSPITAL '
                                               "KITCHEN' in "
                                               'list(bus_strat_sample)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

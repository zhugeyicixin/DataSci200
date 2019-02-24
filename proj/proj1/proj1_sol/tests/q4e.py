test = {   'name': 'q4e',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "all(bus_cluster_sample.isin(bus['business_id']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "len(bus[bus['business_id'].isin(bus_cluster_sample)]['postal_code'].unique())\n"
                                               '5',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> codes = '
                                               "bus[bus['business_id'].isin(bus_cluster_sample)]['postal_code'].unique();\n"
                                               '>>> '
                                               "sum(bus['postal_code'].isin(codes)) "
                                               '== len(bus_cluster_sample)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

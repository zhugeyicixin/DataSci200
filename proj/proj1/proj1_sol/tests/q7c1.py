test = {   'name': 'q7c1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'print(list(ins_named.columns))\n'
                                               "['business_id', 'score', "
                                               "'date', 'type', 'new_date', "
                                               "'year', 'name', 'address']\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(ins_named) == '
                                               'len(ins)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "ins_named['date'].equals(ins['date'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "sum(ins_named['name'].isnull())\n"
                                               '424',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'print(list(ins_named.iloc[0,[0,1,2,6,7]]))\n'
                                               "[19, 94, 20160513, 'NRGIZE "
                                               "LIFESTYLE CAFE', '1200 VAN "
                                               "NESS AVE, 3RD FLOOR']\n",
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

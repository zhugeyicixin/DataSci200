test = {   'name': 'q5b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'sorted(list(fraction_missing_df.columns))\n'
                                               "['count non null', 'count "
                                               "null', 'fraction null']",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'fraction_missing_df.index.name\n'
                                               "'postal_code_5'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def sol_count_null(s):\n'
                                               '...     return '
                                               'len(s[s.isnull()]);\n'
                                               '>>> def '
                                               'sol_count_non_null(s):\n'
                                               '...     return '
                                               'len(s[~s.isnull()]);\n'
                                               '>>> def sol_fraction_null(s):\n'
                                               '...     n = '
                                               'len(s[s.isnull()])\n'
                                               '...     nn = '
                                               'len(s[~s.isnull()])\n'
                                               '...     return (n/(n+nn));\n'
                                               '>>> sol_bus_sf = '
                                               "bus[bus['postal_code_5'].isin(sf_dense_zip)];\n"
                                               '>>> sol_fraction_missing_df = '
                                               "sol_bus_sf['longitude'].groupby(bus['postal_code_5']).agg([sol_count_non_null, "
                                               'sol_count_null, '
                                               'sol_fraction_null]);\n'
                                               '>>> '
                                               'sol_fraction_missing_df.columns '
                                               "= ['count non null', 'count "
                                               "null', 'fraction null'];\n"
                                               '>>> sol_fraction_missing_df = '
                                               'sol_fraction_missing_df.sort_values("fraction '
                                               'null", ascending=False);\n'
                                               '>>> \n'
                                               '>>> '
                                               'fraction_missing_df[["count '
                                               'non null", "count '
                                               'null"]].equals(sol_fraction_missing_df[["count '
                                               'non null", "count null"]])\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

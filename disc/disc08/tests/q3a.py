test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(ts) == len(loss) # '
                                               'theta history and loss history '
                                               'are 20 items in them\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> ts[0].shape == (2,) # '
                                               'theta history contains theta '
                                               'values\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isscalar(loss[0]) # '
                                               'loss history is a list of '
                                               'scalar values, not vector\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isscalar(loss[0]) # '
                                               'loss is decreasing\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.allclose(np.sum(t_est), '
                                               '4.5, atol=2e-1)  # theta_est '
                                               'should be close to our value\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

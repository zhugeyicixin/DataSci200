test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(ts_decay) == '
                                               'len(loss_decay) == 20 # theta '
                                               'history and loss history are '
                                               '20 items in them\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> ts_decay[0].shape == (2,) '
                                               '# theta history contains theta '
                                               'values\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isscalar(loss[0]) # '
                                               'loss history should be a list '
                                               'of values, not vector\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> loss_decay[1] - '
                                               'loss_decay[-1] > 0 # loss is '
                                               'decreasing\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.allclose(np.sum(t_est_decay), '
                                               '4.5, atol=2e-1)  # theta_est '
                                               'should be close to our value\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

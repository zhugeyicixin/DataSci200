test = {   'name': 'q10',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(test_predictions, '
                                               'np.ndarray) # must be ndarray '
                                               'of predictions\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.unique(test_predictions) # '
                                               'must be binary labels (0 or 1) '
                                               'and not probabilities\n'
                                               'array([0, 1])',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> test_predictions.shape # '
                                               'must be the right number of '
                                               'predictions\n'
                                               '(1000,)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> from pathlib import Path;\n'
                                               '>>> datadir = '
                                               "Path('/home/jovyan/');\n"
                                               '>>> \n'
                                               '>>> test_sol = '
                                               "pd.read_csv(datadir/'hw6_kaggle_solutions.csv');\n"
                                               '>>> test_labels = '
                                               "test_sol['Class'].values;\n"
                                               '>>> score = '
                                               'np.mean(test_labels == '
                                               'test_predictions);\n'
                                               '>>> print("Staff Model '
                                               'Score:", score);\n'
                                               '>>> \n'
                                               '>>> score > 0\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> score > 0.82\nTrue',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> score > 0.85\nTrue',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> score > 0.88\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

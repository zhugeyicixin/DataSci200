test = {
  'name': 'q2c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 4 < total_variance < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(total_variance, np.sum(np.var(iris_features, axis=0)))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

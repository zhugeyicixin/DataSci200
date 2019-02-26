test = {
  'name': 'q3a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> iris_2d.shape
          (150, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> -0.25 < np.sum(iris_2d[0]) < -0.24
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(0, np.sum(iris_2d))
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

test = {
  'name': 'q2b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.all(np.isclose(s, np.array([2.04857882, 0.49053911, 0.27928554, 0.15337907])))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> u.shape
          (150, 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> vt.shape
          (4, 4)
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

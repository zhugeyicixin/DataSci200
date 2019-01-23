test = {
  'name': 'q2a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> B.shape
          (4, 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(B @ v, np.array([14, 18, 14, 40]))
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

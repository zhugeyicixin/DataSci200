test = {
  'name': 'q2a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> squared_loss(2, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> squared_loss(2, 0)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> squared_loss(5, 1)
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.sum((squared_loss(np.array([5, 6]), np.array([1, 1])) - np.array([16, 25]))**2)
          0
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

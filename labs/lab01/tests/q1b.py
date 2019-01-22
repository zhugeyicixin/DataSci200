test = {
  'name': 'q1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list_sum([], [])
          []
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_sum([1], [1])
          [2]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_sum([-1], [1])
          [2]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_sum([1], [-1])
          [0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_sum([1, 2, 3], [1, 2, 3])
          [2, 12, 36]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list_sum([1, 5, 2], [3, 6, 6])
          [28, 241, 220]
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

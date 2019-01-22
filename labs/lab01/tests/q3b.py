test = {
  'name': 'q3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> array_sum([1], [1])
          array([2])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> array_sum([-1], [1])
          array([2])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> array_sum([1], [-1])
          array([0])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> array_sum([1, 2, 3], [1, 2, 3])
          array([ 2, 12, 36])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> array_sum([1, 5, 2], [3, 6, 6])
          array([ 28, 241, 220])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(array_sum([], [])) is np.ndarray
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

test = {
  'name': 'q1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> fruit_info["rank1"].dtype
          dtype('int64')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sorted(fruit_info["rank1"].dropna())
          [1, 2, 3, 4]
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

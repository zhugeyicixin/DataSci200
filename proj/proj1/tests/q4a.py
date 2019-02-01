test = {
  'name': 'q4a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sample(pd.Series(range(1, 10)), 5) == [8, 5, 2, 3, 9]
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

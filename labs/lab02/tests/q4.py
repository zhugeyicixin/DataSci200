test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> name_and_year.shape
          (5933561, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> name_and_year.loc[0,"Name"]
          'Mary'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> name_and_year.loc[0,"Year"]
          1910
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

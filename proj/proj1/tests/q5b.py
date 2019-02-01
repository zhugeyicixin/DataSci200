test = {
  'name': 'q5b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(fraction_missing_df.columns)
          ['count non null', 'count null', 'fraction null']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fraction_missing_df.index.name
          'postal_code_5'
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

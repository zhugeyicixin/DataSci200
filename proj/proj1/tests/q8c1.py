test = {
  'name': 'q8c1',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(scores_pairs_by_business, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scores_pairs_by_business.columns
          Index(['score_pair'], dtype='object')
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

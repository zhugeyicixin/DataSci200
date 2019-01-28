test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(result)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> result["Count"].sum()
          38993
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> result["Count"].iloc[0]
          4339
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

test = {
  'name': 'q2c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> count_for_names["Michael"]
          429827
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> count_for_names[:100].sum()
          95519
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> count_for_names["David"]
          371646
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> count_for_names[:1000].sum()
          1320144
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

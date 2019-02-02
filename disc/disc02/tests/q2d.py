test = {
  'name': 'q2d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> female_name_count["Emily"]
          48093
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> female_name_count[:100].sum()
          48596
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> female_name_count["Isabella"]
          45232
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> female_name_count[:10000].sum()
          3914766
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

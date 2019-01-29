test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> fruit_info_original.columns
          Index(['Fruit', 'Color'], dtype='object')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fruit_info.columns
          Index(['fruit', 'color', 'rank1', 'rank2'], dtype='object')
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

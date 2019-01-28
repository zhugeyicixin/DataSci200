test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> fruit_info_original.shape
          (4, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fruit_info.shape
          (4, 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fruit_info_original.columns
          Index(['fruit', 'color'], dtype='object')
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

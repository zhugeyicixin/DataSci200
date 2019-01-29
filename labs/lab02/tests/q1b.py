test = {
  'name': 'q1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> fruit_info["rank2"].dtype
          dtype('int64')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fruit_info["rank2"] == fruit_info["rank1"]
          0    True
          1    True
          2    True
          3    True
          dtype: bool
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

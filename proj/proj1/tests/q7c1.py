test = {
  'name': 'q7c1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(list(ins_named.columns))
          ['business_id', 'score', 'date', 'type', 'new_date', 'year', 'name', 'address']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(ins_named) == len(ins)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ins_named['date'].equals(ins['date'])
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

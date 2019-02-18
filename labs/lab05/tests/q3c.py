test = {
  'name': 'q3c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> res_q3c.shape
          (5, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(res_q3c == res_q3c.sort_values('cand_name', ascending=False))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(sorted(map(str, res_q3c['cmte_nm'].unique())))
          ['CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT', 'JOE ZUCCOLO FOR CONGRESS', 'None', 'ZUKOWSKI FOR CONGRESS', 'ZUMWALT FOR CONGRESS']
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

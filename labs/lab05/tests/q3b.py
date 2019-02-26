test = {
  'name': 'q3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> res_q3b.shape
          (5, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(res_q3b == res_q3b.sort_values('cand_name', ascending=False))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(sorted(res_q3b['cmte_nm'].unique()))
          ['CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT', 'CONSTITUTIONAL COMMITTEE', 'JOE ZUCCOLO FOR CONGRESS', 'ZUKOWSKI FOR CONGRESS', 'ZUMWALT FOR CONGRESS']
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

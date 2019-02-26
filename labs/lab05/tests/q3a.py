test = {
  'name': 'q3a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> res_q3a.shape
          (5, 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(res_q3a == res_q3a.sort_values('count', ascending=False))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(sorted(res_q3a['total_amount'].unique()))
          [316019, 492567, 499659, 6989835, 25099091]
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

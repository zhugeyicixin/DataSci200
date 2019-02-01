test = {
  'name': 'q1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_of_names_per_year[2007]
          7248
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_of_names_per_year[:5].sum()
          35607
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_of_names_per_year[1910]
          363
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_of_names_per_year[:15].sum()
          103699
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

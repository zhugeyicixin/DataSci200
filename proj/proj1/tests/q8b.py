test = {
  'name': 'q8b',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(inspections_by_id_and_year['count'])
          14222
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(inspections_by_id_and_year.index.names)
          ['business_id', 'year']
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

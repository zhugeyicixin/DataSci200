test = {
  'name': 'q4c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(bus_strat_sample.isin(bus['name']))
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

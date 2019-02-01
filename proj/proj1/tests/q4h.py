test = {
  'name': 'q4h',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(bus_multi_sample.isin(bus['name']))
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

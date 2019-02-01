test = {
  'name': 'q1d',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> df_allclose(bus, bus_summary)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> df_allclose(ins, ins_summary)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> df_allclose(vio, vio_summary)
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

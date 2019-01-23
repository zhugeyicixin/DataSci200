test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> population_0 = np.random.randn(100);
          >>> np.isclose(mean(population_0), np.mean(population_0), atol=1e-6)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> population_0 = np.random.randn(100);
          >>> np.isclose(variance(population_0), np.var(population_0), atol=1e-6)
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

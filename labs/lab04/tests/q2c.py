test = {
  'name': 'q2c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(kde(gaussian_kernel, 1.0, 2.0, np.array([3.0, 4.0, 5.0, 7.0])), 0.075099)
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

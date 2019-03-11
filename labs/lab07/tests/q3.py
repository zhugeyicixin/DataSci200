test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> y = data['tip'];
          >>> x = data['total_bill'];
          >>> np.isclose(minimize_average_loss(squared_loss, model, x, y), 0.14373189123158361)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> y = data['tip'];
          >>> x = data['total_bill'];
          >>> np.isclose(minimize_average_loss(abs_loss, model, x, y), 0.1495886219625012)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(minimize_average_loss(squared_loss, model, data['total_bill'], data['tip']), 0.14373189229218733)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(minimize_average_loss(squared_loss, model, data['total_bill'], data['tip']), 0.14373189229218733)
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

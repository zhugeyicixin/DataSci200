test = {
  'name': 'q1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "|" not in regx2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'can').group()
          'can'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'fan').group()
          'fan'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'man').group()
          'man'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'dan') is None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'ran') is None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.match(regx2, 'pan') is None
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

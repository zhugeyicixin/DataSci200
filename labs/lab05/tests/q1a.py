test = {
  'name': 'q1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "|" not in regx1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.search(regx1, "abc").group()
          'abc'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.search(regx1, "abcde").group()
          'abcde'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.search(regx1, "abcdefg").group()
          'abcdefg'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> re.search(regx1, "c abc") is None
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

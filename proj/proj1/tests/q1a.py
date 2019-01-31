test = {
  'name': 'q1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(my_zip, zipfile.ZipFile)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(list_names, list)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([isinstance(file, str) for file in list_names]) 
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

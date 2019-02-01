test = {
  'name': 'q4a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> merged_df.loc[0, 'Count']
          371646
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> merged_df.loc[3, 'Count']
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> merged_df.loc[7, 'Count']
          7236
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> merged_df['Count'].sum()
          861694
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(merged_df)
          14
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

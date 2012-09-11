{
  'variables': {
    'expat_root': 'C:/Project/Expat-64'
  },
  'targets': [
    {
      'target_name': 'node_expat',
      'sources': [ 'node-expat.cc' ],
      'libraries': [
        '-l<(expat_root)/Source/win32/bin/Release/libexpat.lib'
      ],
	  'include_dirs': [
			'<(expat_root)/Source/lib'
		 ]
    }
  ]
}

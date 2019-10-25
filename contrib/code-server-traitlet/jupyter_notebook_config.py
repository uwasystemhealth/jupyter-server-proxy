c.ServerProxy.servers = {
  'code-server': {
    'command': [
      'code-server',
        '--auth=none',
        '--disable-telemetry',
        '--port={port}'
    ],
    'timeout': 20,
    'launcher_entry': {
      'title': 'VS Code'
    }
  }
}

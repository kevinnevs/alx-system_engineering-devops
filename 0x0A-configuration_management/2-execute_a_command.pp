# 2-execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -f "killmenow"',
  path        => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}

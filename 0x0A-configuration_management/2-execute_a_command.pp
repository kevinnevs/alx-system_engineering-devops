# 2-execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

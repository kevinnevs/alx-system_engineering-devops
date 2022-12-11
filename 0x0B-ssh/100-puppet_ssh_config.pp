# 100-puppet_ssh_config.pp

# Declare the ssh_config resource
file { '/etc/ssh/ssh_config':
  # Set the owner and group of the configuration file
  owner => 'root',
  group => 'root',
  # Set the permission of the configuration file
  mode  => '0644',
}

# Add a line to the configuration file to turn off password authentication
file { 'Turn off passwd auth':
  # Set the path to the configuration file
  path   => '/etc/ssh/ssh_config',
  # Set the line to be added to the configuration file
  line   => 'PasswordAuthentication no',
  # Ensure that the line is added to the configuration file
  ensure => 'present',
}

# Add a line to the configuration file to specify the identity file
file { 'Declare identity file':
  # Set the path to the configuration file
  path   => '/etc/ssh/ssh_config',
  # Set the line to be added to the configuration file
  line   => 'Identity ~/.ssh/school',
  # Ensure that the line is added to the configuration file
  ensure => 'present',
}

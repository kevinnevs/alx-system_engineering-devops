#Fixing Apache of a server that returns error 500, using strace
#Automate using puppet

exec { 'fix the config typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

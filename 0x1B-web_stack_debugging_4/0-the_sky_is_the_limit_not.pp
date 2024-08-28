# fix request errors

exec { 'fix-for-nginx':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

# Restart nginx

exec { 'nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix-nginx'],
}

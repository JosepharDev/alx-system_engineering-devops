# fix request errors
exec { 'fix-for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf && service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}


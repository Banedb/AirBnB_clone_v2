# Sets up the web server for the deployment of `web_static` using puppet.

package { 'nginx':
  ensure => installed,
  before => Service['nginx']
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default']
}

file { '/etc/nginx/sites-available/default':
  ensure => file
}

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>\n  <head>\n  </head>\n  <body>\nALX\n  </body>\n</html>\n"
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/'
}

exec { 'make-directories':
  command => '/usr/bin/mkdir -p /data/web_static/shared/ /data/web_static/releases/test/',
  before  => File['/data/web_static/releases/test/index.html']
}

exec { 'add-hbnb_static':
  command => '/usr/bin/grep -q "location /hbnb_static/" /etc/nginx/sites-available/default || \
  /usr/bin/sed -i "/server_name _;/a\\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
  \n\t\tindex index.html;\n\t}" /etc/nginx/sites-available/default'
}

# Kills a process named killmenow

exec { 'pkill -f kllmenow':
  path  =>  '/usr/bin/:/usr/local/bin/:/bin/'
}

# sudo netstat -tlnp | grep dockerd

# cat /etc/bind/named.conf.local
# vi /etc/bind/named.conf.local
zone "docker" {
    type master;
    file "/etc/bind/db.docker";
};

# vi /etc/bind/db.docker
$TTL 86400
@ IN SOA ns.docker. admin.docker. (
    2022050901 ; serial
    3600       ; refresh
    1800       ; retry
    604800     ; expire
    86400      ; default_ttl
)

@ IN NS ns.docker.
ns IN A 185.223.235.68
docker IN A 185.223.235.68

$
# sudo systemctl reload bind9

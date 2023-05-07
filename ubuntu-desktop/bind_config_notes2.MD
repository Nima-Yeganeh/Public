# vi /etc/bind/named.conf.options
forwarders {
  8.8.8.8;
  8.8.4.4;
};

# vi /etc/bind/db.example.org
$TTL 86400
@ IN SOA example.org. admin.example.org. (
    2022050901 ; serial
    3600       ; refresh
    1800       ; retry
    604800     ; expire
    86400      ; default_ttl
)

@ IN NS ns.example.org.
ns IN A 185.223.235.68
gitlab IN A 185.223.235.68


$
# vi /etc/bind/named.conf.local
zone "example.org" {
    type master;
    file "/etc/bind/db.example.org";
};

# sudo systemctl restart bind9
# dig gitlab.example.com

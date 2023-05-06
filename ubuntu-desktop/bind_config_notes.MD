# vi /etc/bind/named.conf.options
forwarders {
  8.8.8.8;
  8.8.4.4;
};

# vi /etc/bind/db.example.com
$TTL 86400
@ IN SOA example.com. admin.example.com. (
    2022050901 ; serial
    3600       ; refresh
    1800       ; retry
    604800     ; expire
    86400      ; default_ttl
)

@ IN NS ns.example.com.
ns IN A 185.223.235.68
gitlab IN A 185.223.235.68


$
# vi /etc/bind/named.conf.local
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com";
};

# sudo systemctl restart bind9
# dig gitlab.example.com

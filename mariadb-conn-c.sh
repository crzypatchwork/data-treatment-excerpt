curl -O https://downloads.mariadb.com/Connectors/c/connector-c-3.1.10/mariadb-connector-c-3.1.10-ubuntu-bionic-amd64.tar.gz

sudo su

tar xvf mariadb-connector-c-3.1.10-ubuntu-bionic-amd64.tar.gz --directory /usr --strip-components 1

echo "/usr/lib/mariadb/" > /etc/ld.so.conf.d/mariadb.conf
ldconfig

exit

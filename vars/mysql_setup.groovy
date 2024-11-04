def mysql_setup() {
    sh 'sudo docker run --name zabbix-server -t \
        -e DB_SERVER_HOST="zabbix-mysql" \
        -e MYSQL_DATABASE="zabbix" \
        -e MYSQL_USER="zabbix" \
        -e MYSQL_PASSWORD="$MYSQLCRED_PSW" \
        -e MYSQL_ROOT_PASSWORD="$MYSQLCRED_PSW" \
        -e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
        --network=monitoring -p 10051:10051 \
        --restart unless-stopped \
        -d zabbix/zabbix-server-mysql:alpine-7.0-latest'
}
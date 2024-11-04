def mysql_setup() {
    sh('sudo docker run --name zabbix-mysql -t \
        -e MYSQL_DATABASE="zabbix" \
        -e MYSQL_USER="zabbix" \
        -e MYSQL_PASSWORD="$MYSQLCRED_PSW" \
        -e MYSQL_ROOT_PASSWORD="$MYSQLCRED_PSW" \
        --network=monitoring --restart unless-stopped \
        -d mysql:8.0-oracle --character-set-server=utf8 --collation-server=utf8_bin \
        --default-authentication-plugin=mysql_native_password')
}

def zabbix_java_gateway() {
    sh('sudo docker run --name=zabbix-java-gateway -t --network=monitoring --restart unless-stopped \
        -d zabbix/zabbix-java-gateway:alpine-7.0-latest')
}

def zabbix_server() {
    sh('sudo docker run --name zabbix-server -t \
        -e DB_SERVER_HOST="zabbix-mysql" \
        -e MYSQL_DATABASE="zabbix" \
        -e MYSQL_USER="zabbix" \
        -e MYSQL_PASSWORD="$MYSQLCRED_PSW" \
        -e MYSQL_ROOT_PASSWORD="$MYSQLCRED_PSW" \
        -e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
        --network=monitoring -p 10051:10051 \
        --restart unless-stopped \
        -d zabbix/zabbix-server-mysql:alpine-7.0-latest')
}

def zabbix_web() {
    sh('sudo docker run --name zabbix-web-nginx -t \
        -e ZBX_SERVER_HOST="zabbix-server" \
        -e DB_SERVER_HOST="zabbix-mysql" \
        -e MYSQL_DATABASE="zabbix" \
        -e MYSQL_USER="zabbix" \
        -e MYSQL_PASSWORD="$MYSQLCRED_PSW" \
        -e MYSQL_ROOT_PASSWORD="$MYSQLCRED_PSW" --network=monitoring -p 8000:8080 \
        --restart unless-stopped \
        -d zabbix/zabbix-web-nginx-mysql:alpine-7.0-latest')
}
FROM neo4j:2025.01.0-enterprise

RUN echo "server.metrics.prometheus.enabled=true" >> /var/lib/neo4j/conf/neo4j.conf
RUN echo "server.metrics.prometheus.endpoint=neo4j:2004" >> /var/lib/neo4j/conf/neo4j.conf

RUN sed -i 's/#dbms.security.auth_enabled=true/dbms.security.auth_enabled=false/g' /var/lib/neo4j/conf/neo4j.conf
RUN sed -i 's/#dbms.security.auth_enabled=false/dbms.security.auth_enabled=false/g' /var/lib/neo4j/conf/neo4j.conf

RUN apt-get update && \
    apt-get install -y curl netcat

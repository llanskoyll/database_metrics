FROM alpine:latest

RUN apk update && apk add --no-cache prometheus curl

RUN addgroup -S prometheus && adduser -S -G prometheus prometheus
RUN chown -R prometheus:prometheus /etc/prometheus/prometheus.yml
USER prometheus

ENTRYPOINT ["/usr/bin/prometheus"]
CMD ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/prometheus"]

EXPOSE 9090

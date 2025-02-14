FROM arangodb:latest

RUN apk update && \
    apk add --no-cache curl


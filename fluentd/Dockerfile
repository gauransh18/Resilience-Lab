FROM fluent/fluentd:v1.11-1

USER root

RUN apk update && apk upgrade && \
    apk add --no-cache sudo make gcc g++ libc-dev && \
    sudo gem install faraday -v 2.8.1 && \
    sudo gem install faraday-net_http -v 3.0.2 && \
    sudo gem install elasticsearch-transport -v 7.13.3 && \
    sudo gem install fluent-plugin-elasticsearch -v 4.0.7 && \
    sudo gem sources --clear-all && \
    apk del sudo make gcc g++ libc-dev && \
    rm -rf /var/cache/apk/* && \
    rm -rf /home/fluent/.gem/ruby/2.6.0/cache/*.gem

USER fluent
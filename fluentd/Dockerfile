FROM fluent/fluentd:v1.11-1

USER root

# Use root account to use apk
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \
 && apk update \
 && apk upgrade \
 && apk add --no-cache $buildDeps \
 && sudo gem install oj -v 3.10.18 \
 && sudo gem install elasticsearch -v 7.13.1 \
 && sudo gem install fluent-plugin-elasticsearch -v 4.0.7 \
 && sudo gem sources --clear-all \
 && apk del $buildDeps \
 && rm -rf /var/cache/apk/*

# Copy configuration file
COPY conf/fluent.conf /fluentd/etc/

# Change the default user back to fluent
USER fluent
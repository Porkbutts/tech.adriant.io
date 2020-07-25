FROM ruby:2.7
LABEL maintainer="pumpadrian@gmail.com"

RUN gem install jekyll bundler

WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock ./

RUN bundle 

COPY ./ ./

EXPOSE 4000 35729
CMD ["/bin/bash", "./bin/serve", "dev"]

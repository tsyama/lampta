FROM php:7.2-apache

RUN apt-get update
RUN apt-get -y install git zlib1g-dev libicu-dev zip unzip
RUN docker-php-ext-install pdo pdo_mysql mysqli mbstring intl zip

RUN apt-get install -y ssmtp mailutils

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer self-update
RUN composer global require hirak/prestissimo

COPY ./conf/apache2/ /etc/apache2/sites-enabled/
COPY ./conf/ssmtp.conf /etc/ssmtp/ssmtp.conf

RUN a2enmod rewrite
RUN rm -f /etc/apache2/sites-enabled/000-default.conf
RUN rm -f /etc/apache2/sites-available/000-default.conf
RUN service apache2 start
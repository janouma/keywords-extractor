# base python image
FROM python:3.9.6-slim

# define environment variables
ARG AUTHOR
ARG NAME
ARG VERSION
ENV APP_HOME="/home/$NAME/app"
ENV PYTHON_PORT=3005

# install build dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# create app user
RUN groupadd -r python && useradd -rg python python && mkdir -p /home/python && \
  chown -R python:python /home/python

# create application folder and assign rights to the node user
RUN mkdir -p $APP_HOME && chown -R python:python $APP_HOME

# set the working directory
WORKDIR $APP_HOME

# copy requirement file from the host
COPY --chown=python:python requirements.txt $APP_HOME/

# install application modules
RUN pip install --no-cache-dir -r requirements.txt

# copy remaining files
COPY --chown=python:python . $APP_HOME/

# set the active user
USER python

# expose port on the host
EXPOSE $PYTHON_PORT

# application launch command
CMD export JWT_SECRET=`cat .jwt_secret`; export PASSWORD=`cat .password`; PORT=$PYTHON_PORT python server.py

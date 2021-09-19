FROM nikolaik/python-nodejs:python3.8-nodejs12

RUN useradd -ms /bin/bash vscode

# Install github cli
# https://github.com/cli/cli/blob/trunk/docs/install_linux.md

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt update 
RUN apt-get install gh

# install chrome for scraper

RUN mkdir -p /tmp/chrome \
   && cd /tmp/chrome \
   && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN cd /tmp/chrome \
   && ls \
   && dpkg -i google-chrome*.deb || true \
   && apt update \
   && apt --fix-broken install -y

# Install chromedriver

RUN mkdir -p /tmp/ && \
    cd /tmp/ && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/ && \
    # clean up the container "layer", after we are done
    rm /tmp/chromedriver.zip

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"

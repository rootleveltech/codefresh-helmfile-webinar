ARG HELM_VERSION=3.1.1

FROM codefresh/cfstep-helm:${HELM_VERSION}

ARG HELMFILE_VERSION=0.111.0
ARG HELM_DIFF_VERSION=3.1.1
ARG HELM_SECRETS_VERSION=2.0.2

# Install required Alpine packages

RUN apk add --update \
    linux-headers \
    git \
    gnupg \
    python3 && \
    rm -rf /var/cache/apk/*

# Install helmfile plugin deps

RUN helm plugin install https://github.com/databus23/helm-diff --version ${HELM_DIFF_VERSION} && \
    helm plugin install https://github.com/futuresimple/helm-secrets --version ${HELM_SECRETS_VERSION}

RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin

# Install helmfile
ADD https://github.com/roboll/helmfile/releases/download/v${HELMFILE_VERSION}/helmfile_linux_amd64 /bin/helmfile
RUN chmod 0755 /bin/helmfile

LABEL helm="${HELM_VERSION}"
LABEL helmfile="${HELMFILE_VERSION}"
LABEL helmdiff="${HELM_DIFF_VERSION}"

COPY lib/helmfile.py /helmfile.py

ENTRYPOINT ["python3", "/helmfile.py"]

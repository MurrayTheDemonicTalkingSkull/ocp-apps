# Extend the official httpd S2I builder image
FROM registry.redhat.io/rhscl/httpd-24-rhel7:latest

COPY .s2i/bin/ /usr/libexec/s2i/
# Become root to install additional packages


# Install curl for troubleshooting or build-time scripts
RUN yum install -y curl && yum clean all

# Switch back to the default user (important!)
USER 1001

# Base image with JDK and Maven
FROM registry.access.redhat.com/ubi8/openjdk-11:1.20

# S2I required labels
LABEL io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" \
      io.openshift.s2i.destination="/tmp" \
      io.k8s.description="Custom S2I builder for Java apps" \
      io.k8s.display-name="Java S2I" \
      io.openshift.tags="builder,java,maven"

# Install Maven (if not already present in base)
USER root
RUN microdnf install -y maven && microdnf clean all

# Create S2I scripts directory
RUN mkdir -p /usr/libexec/s2i
COPY .s2i/bin/ /usr/libexec/s2i

# Set working directory for builds
WORKDIR /opt/app-root/src

# Set default port (can be overridden by app)
EXPOSE 8080

USER 1001

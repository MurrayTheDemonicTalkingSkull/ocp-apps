oc new-project java-app
oc new-app openjdk-17~https://github.com/youruser/java-hello --name=java-hello
oc expose svc/java-hello

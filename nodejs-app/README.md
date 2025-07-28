# ocp-apps NodeJS

# Create project
oc new-project node-app

# Deploy using Node.js image stream (adjust version if needed)
oc new-app nodejs:14~https://github.com/youruser/nodejs-hello --name=nodejs-hello

# Expose route
oc expose svc/nodejs-hello

# Watch pods and route
oc get pods
oc get route

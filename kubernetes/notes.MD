# Kubernetes

Kubernetes (also known as "K8s") is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications. It was originally developed by Google, and is now maintained by the Cloud Native Computing Foundation (CNCF).

With Kubernetes, you can deploy and manage containerized applications across a cluster of nodes, abstracting away the underlying infrastructure and providing a consistent way to manage and scale applications. It provides features such as automatic scaling, rolling updates, self-healing, service discovery, and load balancing.

Kubernetes is becoming increasingly popular in the software industry, as it helps to streamline the deployment and management of modern, cloud-native applications. It is also being widely adopted by major cloud providers such as Amazon Web Services, Google Cloud Platform, and Microsoft Azure, which offer managed Kubernetes services.

# Kubernetes uses several port numbers for various components and services. Here are some of the commonly used port numbers in Kubernetes:

API server: Port 6443 (secure), 8080 (insecure)
etcd: Port 2379 (client communication), 2380 (server-to-server communication)
kubelet: Port 10250 (secure), 10255 (insecure)
kube-proxy: Port 10256 (insecure)
Container runtime interface (CRI): Port 10010 (secure)
Container networking interface (CNI): No standard port number, but typically uses a local socket file
Note that these are default port numbers, and they can be configured to use different port numbers if necessary. It's important to ensure that the necessary ports are open and accessible for proper functioning of Kubernetes components and services.

# Here are some key terms and concepts related to Kubernetes:

Pod: The smallest deployable unit in Kubernetes, representing a single instance of a running process in a cluster.

ReplicaSet: A Kubernetes object that ensures a specified number of pod replicas are running at any given time.

Deployment: A higher-level object that manages a ReplicaSet and provides features like rolling updates, rollbacks, and scaling.

Service: An abstraction layer that provides a stable IP address and DNS name for a group of pods, enabling communication between them.

Node: A worker machine in a Kubernetes cluster, responsible for running pods and containers.

Cluster: A set of nodes that run containerized applications, managed by Kubernetes.

Namespace: A logical grouping of Kubernetes resources, providing a way to partition and isolate resources within a cluster.

ConfigMap: A Kubernetes object used to store configuration data as key-value pairs, which can be injected into a pod as environment variables or mounted as files.

Secret: A Kubernetes object used to store sensitive information, such as passwords and API keys, which can be injected into a pod as environment variables or mounted as files.

Container: An isolated environment for running an application, packaged with all its dependencies, libraries, and runtime. Containers are deployed and managed as part of a pod in Kubernetes.

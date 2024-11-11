# Kubernetes Deployment with Minikube

This guide will help you deploy two microservices—a stateful and a stateless application—using managed kubeneretes i.e `aks`.

## Prerequisites

1. azure-cli installed
2. Kubectl installed

## Step-by-Step Guide

### 1. Creating cluster

#### Define your Environmental Varaibles:

windows
```bash
 MY_RESOURCE_GROUP_NAME="myAKSResourceGroup"
 ```
 ```bash
 REGION="centralindia"
 ```
 ```bash
 MY_AKS_CLUSTER_NAME="myAKSCluster"
 ```
 ```bash
 MY_DNS_LABEL="mydnslabel"
```
### 2. Create a resource group
```bash
az group create --name $MY_RESOURCE_GROUP_NAME --location $REGION
```
### 3. Create an aks cluster
```bash
az aks create --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_AKS_CLUSTER_NAME --node-count 1 --generate-ssh-keys
```
### 4. Connect to the cluster
```bash
az aks get-credentials --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_AKS_CLUSTER_NAME
```
#### 5. Verify the connection
```bash
kubectl get nodes
```
## Deploy application
#### Change directory
```bash
cd .\k8s-deploy
```
then, apply the below following

### 1. Create Namespace
Create a namespace for your deployments:

In my case, I created namespace manifest file as `namespace.yml` of having object `Namespace`
```bash
kubectl apply -f namespace.yml
```
### 2. create ConfigMap
Create a ConfigMap for Required Environmental variables to pass it to container while creating pod

In our case, It was `configMap.yml` with resource `ConfigMap`
#### Apply Configmap
```bash
kubectl apply -f configMap.yml
```
### 3. Deploy Stateful Application
Create StatefulSet YAML, Here i created a statefulset manifest file name as `books-db-sfs.yml`
with resources like `StatefulSet`,

 `Service` ->**Headless ClusterIP**: Which forwards request to specific database internally
#### Apply StatefulSet
```bash
kubectl apply -f books-db-sfs.yml
```
### 4. Deploy Stateless Application
Create Deployment YAML, Here i created a deployment manifest file name as `books-deploy.yaml` 
with resources like `Deployment`, 

`Service` ->**LoadBalancer**: To access appliction from outside

#### Apply deployment
```bash
kubectl apply -f books-deploy.yml
```



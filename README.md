# X-K8S - Deploy a Kubernetes Cluster for 5G NFV Cloud

X-K8S leverags plugins for the better NFV performance in 5G use senario, like CMK (Cpu Manager for Kubernetes), NFD (Node Feature Discovery), intel's userspace-cni-network-plugin, etc.  
And based on the kubespray v2.8.0 as its deploy tool.  

For the detail deploy instruction, check the kubespray's [readme](https://github.com/mJace/x-k8s/blob/develop/kubespray/README.md).  

## Spec

|    Package    |    version    |
|---------------|---------------|
|Kubernetes     |v1.12.3        |
|Docker         |v18.06.1-ce    |
|CMK            |v1.3.1         |
|NFD            |v0.3.0         |
|Multus         |v3.1           |
|Flannel        |v0.10.0        |
|Flannel-Cni    |v0.3.0         |

## Requirement

1. Python3  
2. pip3  

## Usage  

### Install x-k8s  

1. Install requirement.

    ```=bash
    cd x-k8s
    sudo pip3 install -r requirements.txt
    ```  

2. Edit hosts.ini in `/x-k8s/kubespray/inventory/mycluster/hosts.ini`  

3. Enable root on nodes, and setup no-password login for deploy node.

4. Disable swap on nodes.  

5. Deploy  

   ```=bash
   su -
   ./x-k8s install
   ```

## CLI  

```=python
X-K8S Installer
Usage:  
    ./x-k8s install [--i=<hosts>]
    ./x-k8s reset [--i=<hosts>]
    ./x-k8s list inventory [--vars]
    ./x-k8s ( -h | --help)
    ./x-k8s ( -v | --version)

Examples:
    ./x-k8s install                     Install x-k8s.
    ./x-k8s install --i kubespray/inventory/custom/hosts.ini
                                        Install x-k8s using custom inventory.
    ./x-k8s reset                       Reset host environment listed in inventory.
    ./x-k8s reset --i kubespray/inventory/custom/hosts.ini
                                        Reset host environment using custom inventory.
    ./x-k8s list inventory              List hosts inventory.
    ./x-k8s list inventory --vars       List hosts inventory with all variables.
    ./x-k8s -h  
    ./x-k8s --help
    ./x-k8s -v
    ./x-k8s --version

Options:
    -h, --help                          Show this message.
    -v, --version                       Show version.
    --vars                              List hosts inventor with all variables.
    --i=<hosts>                         Path to custom inventory hosts.ini
```
from docs.base import Base


class K8s(Base):

    _doc = {
        "apply": """
kubectl apply -f file.yaml

kubectl apply -f - <<EOF
...
EOF
""",
        "delete": """
kubectl delete -f file.yaml
kubectl delete pods -A --field-selector=status.phase=Failed
""",
        "api": """
kubectl get apiservices
""",
        "pod": """
kubectl get pods
kubectl describe pod <podname>

kubectl exec --stdin --tty <podname> -- /bin/sh

# custom
kubectl get pod -o=custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName --all-namespaces

# delete pods by status
kubectl get pods | grep -i evicted | awk '{print $1}' | xargs -i kubectl delete pods {}

# for pods hang on terminating
kubectl get pods | grep -i terminating | awk '{print $1}' | xargs -i kubectl delete --grace-period=0 --force pods {}
""",
        "node": """
kubectl get node

kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces
""",
        "deploy": """
kubectl get deploy
kubectl scale deploy <deployment> --replicas=0
kubectl scale deploy <deployment> --replicas=1
""",
        "statefulset": """
kubectl scale statefulset <statefulset> --replicas=0
kubectl scale statefulset <statefulset> --replicas=1
""",
        "svc": """
kubectl get svc
""",
        "namespace": """
kubectl create namespace <namespace-name>
kubectl delete namespace <namespace-name>
""",
        "label": """
kubectl get pods --show-labels
kubectl label pods <podname> <key>=<value>

kubectl get namespaces --show-labels
kubectl label namespace <namespace> istio-injection=enabled
""",
        "top": """
kubectl top node
kubectl top pods
kubectl top pod <podname> --containers
""",
        "istio": """
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
export TCP_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="tcp")].port}')
""",
        "gateway": """
kubectl get gateway --all-namespaces
kubectl get gateway -o yaml
""",
        "ingress": """
kubectl get ingress --all-namespaces
""",
        "virtualservices": """
kubectl get virtualservices
kubectl get virtualservices -o yaml
""",
        "destinationrules": """
kubectl get destinationrules
kubectl get destinationrules -o yaml
""",
    }


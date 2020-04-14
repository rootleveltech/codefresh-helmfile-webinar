### Helm Diff

#### Deploy Fixed Version of MyApp Helm Chart
```
cd ~/codefresh-helmfile-webinar/code-01/helm/charts/myapp/
helm upgrade --install myapp . 
kubectl get po -w

```

#### Show Diff to see deploying old version
```
cd /Users/braden/codefresh-helmfile-webinar/code-02/helm/helmfile/myapp
helmfile diff
```

#### Show Diff to see deploying fixed version
```
cd /Users/braden/codefresh-helmfile-webinar/code-03/helm/helmfile/myapp
helmfile diff
helmfile destroy
```

#### Helm Hook (create namespace)
```
/Users/braden/codefresh-helmfile-webinar/code-04/helm/helmfile/myapp
helmfile apply
kubectl get po -w -n dev
helmfile destroy
```

#### Helm Dependencies (create namespace)
```
/Users/braden/codefresh-helmfile-webinar/code-05/helm/helmfile/myapp
helmfile apply
kubectl get po -w -n dev
helmfile destroy
```


#### Helm Advanced Templating
```

```
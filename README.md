# testproduct04-d20
a precursor to credibility

## Kubernetes ingress template

The [sample Ingress](src/deployment/kubernetes_manifests/ingress.yaml) uses `my-app.example.com` and a placeholder certificate issuer. Before deploying, set the hostname and issuer, and verify that the selected ingress class points to a maintained controller that supports the manifest's annotations. Confirm that the deployed controller image includes current security fixes for its bundled NGINX build.

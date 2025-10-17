#  **ORBINA Fleet Cloud**

![Go](https://img.shields.io/badge/go-1.22-blue)
![MQTT](https://img.shields.io/badge/protocol-MQTT-orange)
![Kubernetes](https://img.shields.io/badge/deploy-cloud--native-green)

**Manage, monitor, and update thousands of autonomous devices from one dashboard.**

---

###  Intro

ORBINA connects fleets of edge mains to your cloud.
It provides real-time telemetry, firmware updates, and task orchestration.

Live demo: [cloud.orbina.app](https://cloud.orbina.app)

---

### 🪶 Quick Deploy

```bash
helm install orbina ./charts/orbina \
  --set cloud.mqttBroker=broker.orbina.net
```

---

###  Architecture

```
[device] ⇄ [edge-agent] ⇄ [broker] ⇄ [orbina-api] ⇄ [dashboard]
```

* Agents written in Go, <5MB footprint
* gRPC streaming telemetry
* Built-in alert rules

---

### API Example

```bash
curl https://api.orbina.app/v1/devices | jq .
```

---

### Plans

| Tier       | Devices   | Price   |
| ---------- | --------- | ------- |
| Hobby      | 20        | Free    |
| Startup    | 500       | $25/mo  |
| Enterprise | Unlimited | Contact |

Apache-2.0 © [orbina.app](https://orbina.app)
*authored by: L. Simatupang — “devops pragmatist”*

# PR Merge: 2025-10-17 - feature/merge-3477

# PR Merge: 2025-10-17 - enhancement/merge-3922

# PR Update: 2025-10-17 - docs/update-5904

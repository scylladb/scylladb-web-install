import json
jobj = [
  {
    "product":"scylla",
    "version":"4.5"
  },
  {
    "product":"scylla",
    "version":"4.6"
  },
  {
    "product":"scylla-enterprise",
    "version":"2020.1"
  },
  {
    "product":"scylla-enterprise",
    "version":"2021.1"
  }
]
distro = ["ubuntu:18.04", "ubuntu:20.04", "debian:10", "centos:7", "rockylinux", "rhel:7", "rhel:8", "oraclelinux:8", "amazonlinux:2"]
jobj_full = []
for d in distro:
  for o in jobj:
    jobj_full.append({**o, **{"distro": d}})
jtxt = json.dumps(jobj_full, indent=2)
with open('../.github/workflows/matrix_includes.json', 'a+') as f:
  f.write(jtxt)
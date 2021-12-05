#!/bin/bash

cat > /ssl/target.json <<EOF
{
	targets:[
		{
			"names": [
				"allenyou.wang",
				"*.allenyou.wang"
			],
			"type": "rsa",
			"dnsapi": "dns_cf"
		},
		{
			"names": [
				"allenyou.wang",
				"*.allenyou.wang"
			],
			"type": "ec-256",
			"dnsapi": "dns_cf"
		}
	]
}
EOF

python3 ./entry.py
# Run Logs Insight Query

fields requestURI, verb, responseStatus.Code, userAgent
| filter @LogStream like "kube-apiserver-audit"
| stats count(*) as count by requestURI, verb, responseStatus.Code, userAgent
| sort count desc

# Sample Screenshot

<img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/411953a5-616f-4c1f-8cf1-8ff880f99cdc" />

<img width="940" height="442" alt="image" src="https://github.com/user-attachments/assets/22595110-74fd-4825-9e7a-9f147a5d6e15" />


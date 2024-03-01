#!/bin/bash
#!/bin/bash
# Sends a request t o a URL passed as an argument, and displays only the status code of the response
curl -s -o /dev/null -w "%{http-code}" "$1"

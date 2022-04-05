# AutoWifi 
Auto Login to BITS-STAFF/BITS-STUDENT Captive Portal

## Instructions (For Windows Only)
1. Download zip from releases and extract it.
2. Open creds.txt. Change fxxxxxxxx -> your username. Change password -> your password
3. If you use cloudflare warp, open warp-path.txt and ensure that the path for warp-cli.exe is correct. If not, replace it with the correct path.
4. Create a task in task scheduler and point it to the exe file in loginscript folder. Refer to this [post](https://www.groovypost.com/howto/automatically-run-script-on-internet-connect-network-connection-drop/) (Will be automated soon).
5. Voila!

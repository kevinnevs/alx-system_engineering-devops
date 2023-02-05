# This is a postmortem incident report based on the project Webstack debugging project #1. Where the web server's port 80 was to open for Nginx sessions to be active.

NGINX SERVER OUTAGE INCIDENT REPORT

Issue Summary:
* Duration of the outage: 1hr
* Impact: Nginx was not listening on port 80, causing a failure to access the web server. 100% of users were affected.
* Root Cause: Nginx was not configured to listen on port 80 of all active IPv4 IPs.

Timeline:
* 6:00 PM: Configuration push begins
* 6:10 PM: Outage begins
* 6:23 PM: Pagers alerted teams
* 6:30 PM: Debug and file cross-checking
* 6:58 PM: Server restarts begin
* 7:00 PM: 100% of traffic back online

Root Cause and Resolution:
* The issue was caused by Nginx not being configured to listen on port 80 of all active IPv4 IPs. To resolve the issue,
  a bash script was created that updated the Nginx configuration to listen on all active IPv4 IPs on port 80 and started Nginx.
  The script checked if Nginx was already running and stopped it if it was. The script also verified that Nginx was listening on port 80 after starting it.

Corrective and Preventative Measures:
* Improve server configuration management to ensure that all necessary ports are open and services are configured correctly.
* Implement monitoring on the server to alert on any changes to the Nginx configuration and its status.
* Regularly review and update the server configuration to ensure that it is up-to-date and secure.

Tasks:
* Update server configuration management process to include checking for open ports and necessary service configurations.
* Implement monitoring on the server to track Nginx configuration and status.
* Schedule regular review and updates to the server configuration.

Sincerly,

ALX Holberton #Cohort-7 Student.

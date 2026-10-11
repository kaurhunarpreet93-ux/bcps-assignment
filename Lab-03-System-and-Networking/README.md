# Lab 3: System Configuration and Networking Commands

## Aim
To demonstrate basic system-information, IP-configuration, and network-diagnostic commands.

## Procedure
1. Open Command Prompt or Terminal.
2. Run the system-information and hostname commands.
3. Display the network configuration.
4. Test connectivity using `ping`.
5. Use the route-tracing command if available.

## Windows Command Prompt
```bat
hostname
systeminfo
ipconfig
ipconfig /all
ping example.com
tracert example.com
```

## Linux Terminal
```bash
hostname
uname -a
ip addr
ip route
ping -c 4 example.com
traceroute example.com
```

## Expected Output
System details and network configuration are displayed. The ping command may show replies and round-trip times if the host is reachable. Network policies, DNS, firewalls, or lack of internet can affect results.

## Conclusion
Basic system configuration and network troubleshooting commands were demonstrated.

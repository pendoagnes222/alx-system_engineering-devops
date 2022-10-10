Firewall is a system that is designed to prevent unauthorized access from entering a private network.

Firewall create a barrier between a private network and the public internet.

Firewalls rules can be based on:
   
   Ip addresses
   
   Protocals
   
   Domain names 
   
   Programs
   
   Ports
  
   Key words

TYPES OF FIREWALL

1.Host-based firewalls
 
   Software firewall that is installed on computers
  
   Protect that computer only


2.Network-based firewalls
  
   Combination of hardware and software and it operates at the network
  
   It is placed between private network and public internet
  
   Protect the entire network 



0. 0-block_all_incoming_traffic_but
  Installing the ufw firewall and setup a few rules on web-0 
  
  Configure ufw so that it blocks all incoming traffic, 

       22 (SSH)
      
       443 (HTTPS SSL)
    
       80 (HTTP)


1. 100-port_forwarding
  
  Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP

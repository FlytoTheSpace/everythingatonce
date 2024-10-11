# BASH (Bourn Again Shell), Linux

## Commands:
    
### General

- `echo "<Message>"`: Logs The Message in The Terminal, Prints The Message to The stdout
    ```bash
    echo "Hello, World"
    # Hello, World
    ```
    - `-n` Removes Trailing \n from the end
    - `-e` Enable Escape Characters
    - `-n` Disable Escape Characters

- `clear`: clear your terminal

- `date`: returns the current Date
- `sleep <n>`: pauses any further execution for `n` number of seconds (usefull in bash scripts)
- `man <command>`: shows you the full documentation of the Specified Command if Available (External Packages Included)
- `whatis <command>`: give you a quick summary of what the Specified command does
- `which <commands / packages / variable>`: tells you where things are Located in the System
- `whereis <commands / packages / variable>`: tells you exactly where things are Located in the System and also if They are located on multiple places
- `wget <URL>`: let's you get Files from the Internet
- `curl <URL>`: same as wget
- `exit`: can be used to exit out of a lot of places
- `reboot`: reboots your system
- `shutdown -h now`: shutdowns your system

### Navigation
    
- `ls` Lists all the Files in the Current Working Directory

    - `-l` Also Displays Meta Data About the File such as Permissions, Creation Date, name, etc.
    - `-a` Displays Hidden Files

- `pwd` prints the Current Working Directory

- `cd <PATH>` changes your Current Working to the Path

    - `cd` changes your Current Working Directory to Your Home Directory

- `ln -s <Path+Name> <Link>` Create a link/Shortcut file that leads to the Specified file-   (iii) Files and Directories
-`touch <Path+Name...>` Creates a File, You can create multiple files by just typing their -h and Name side by sid-    - `-d <Date>` Schedule a File to be Created in the Future on <Date>

- `cat <Path+Name>` -plays Contents of the File
- `cp <Path+Name> <N-ath>` Copies The File to The Specified New Path
- `mv <Path+Name> <N-ath>` Copies The File to The Specified New Path
- `mkdir <Path+Name>-reates a new Directory on the Path
(f) `shred <Path+Nam- Obfuscates the File
- `rm <Path+Name>` Deletes The File on the Path
- 
- () `-r` Let's you Delete Folder even If they are not Empty

- `rmdir <Path>` Deletes The Directory on the Path, Only if  The Directory  is Empty
- `chmod <+ or -><permission> <Path>`: Adds or Removes File Permissions
-  $ # Executable File
- $ chmod +x script.sh-j) `chown <username> <Path>` Changes Ownership of the File/Directory
(k) `zip <Path+Name>.zip <files...>` Zips the Specified files with the Specified name
(l) `unzip <Path+Name>.zip` Unzips the Files
(m) `find <Path> -name "<Name>"` searches for Files in the Specified Directory
(n) `head <Path+Name>` Displays Heading of the File
(o) `less <Path+Name>` Displays Contents of the One Page at a Time
(p) `tail <Path+Name>` Displays Tail of the File

(q) `cmp <Path+Name> <Path+Name>` compares Both Files
(r) `diff <Path+Name> <Path+Name>` compares Both Files and tell you the Difference between Both Files

(m) `locate <fileName>` searches for the File Everywhere

    (iv) Users

- `whoami` The User who you are Logged in as

- `useradd <username>`: simply adds a new user by the name of <username> (Requires ROOT)

- `adduser <username>`: let's you configure settings for the new user such as Passwords etc. (Requires ROOT)

- `su <username>`: Switch to the Specified User, add prefix `sudo` and don't specify the -rname to log in as ROOT
- `exit` exits out of the current user If is switched from a different user-f) `passwd <username>` changes password of the User, leave the username Empty to change-ur own Password (Requires ROOT)-   (v) Network- `ping <domain/IP>` Let's you know if something is up running
-  - `-c <Count>` Limits the amoung of Pings
- - `-s <Size>` Sets the Size of the Packets in Bytes- `ssh <user>@<IPAddress>`

    - `-p <PORT>` stands for PORT (default 22)

- `ifconfig` or `ip address` Let's you view your IP Details
- `resolvectl status` Show you Details about Your DNS
- `traceroute <domain/IP>` Displays all of the Proxies you are passing through to get at the destination
- `netstat` or `ss` Displays all the Network Activity-   - `-t` or `--tcp`: limits to TCP Network Activit-   - `-u` or `--udp`: limits to IP Address Ports etc
    - `-l` or `--listening`: limits to Current Activity or if Enabled or Not
    (IV) `-p` o---programm`: limits to Programs Only
    (V) `-n` or--numeric`: limits to Numberic
    (VI) `-tulp-limits to Open Ports Only -g) `iptables` Your Firewall Settings on the different Port-(h) `ufw` builds on top of `iptables` for making things easier 

    - `ufw allow <PORT>` Opens up the Specified Port
    - `ufw status` Check Firewall Status
    - `ufw enable` enable Firewall
    (IV) `ufw disable` disable Firewall

    (vi) Utilities for Other Commands

- `sudo <command>` runs the command with Root Privelages
- `| sort <text>` sorts in Alphabetical Order
- `| grep <word>` let's you get Lines that starts with The `<word>`
- `| bc0` evaluates an Arithemetic Expression
- `$(<command>)` let's you get the return values of the Commands

```bash
flytothespace@debian:~$ me=$(whoami)
flytothespace@debian:~$ echo $me
flytothespace
flytothespace@debian:~$ -f `<Command> > <Path+Name>` creates a File on the path and inserts the Return Value- The Command into that file
```
-  $ echo "Hello, World" > file.txt
- $ cat file.txt
- Hello, World

- `<command1> | <command2>` passes the output of the first command and to the second command
- `<command> &` makes the command run in the background

    (vii) Operating System

- `uname` Information About your OS
- `free` Information About RAM and Swap
- `df -H` Information About Storage
- `ps -aux` Information About Running Processes on Your System
- `top` Information About CPU and RAM
- `htop` Information About CPU and RAM in a prettier way
- `kill -9 <ProcessID>` Kills the Process by It's ID
- `pkill -f <ProcessName>` Kills the Process by It's Name-i) `systemctl` Services

    - `systemctl status <ServiceName>` Shows Status of - Specified Service
    - `systemctl start <ServiceName>` Starts The Speci-d Service
    - `systemctl stop <ServiceName>` Stops The Specif- Service-. Package Managers-   (i) apt

- `apt update` updates your Package Repositories
- `apt upgrade` installs your updates your Package Repositories
- `apt install <name>` installs the Specified Package by Name

3. External Packages
    
    (i) finger

- Let's You Inspect Other Users

- installation

```bash
# Debian based
sudo apt install finger
```
- `finger <username>` Inspects the Specified user

### neofetch

- Let's you get some About your Computer and OS

- installation
```bash
    $ # Debian based
    $ sudo apt install neofetch
```
- `neofetch` Information about your Computer and OS
    
    (iii) cal

- Gives you a Calender in Your terminal

-  installation

    $ # Debian Based
    # sudo apt install cal

- `cal` Displays a Calender

4. Comments

    (i) Comments are peices of text that are Ignored by the interpreter/Compiler for Guidance and Other Purposes

### in Bash Comments can be defined by making a Line start with "#", and all the text after that "#" sign will be ignored until the line ends

# This is a Comment
echo "hello, World"

$ bash script.sh
hello, World

5. Permissions:

    (i) Ownerships: There are 3 types of Ownerships in Linux:

User
Group
Other

### Permissions: There are 3 types of Permissions for each Type of Owner of the File

r : Read permission
w : Write permission
x : Execute permission
– : No permission set

    (iii) A Linux Permission Consists of 9 Characters They Follow this Order: r (Read), w (Write) and x (Execute) and to Represent, that the permission is defined they are replace by '-'.
    (iii) Example:-

rwxrw-r--


User       Group
Owner      Owner     Other Users
 ↓           ↓           ↓
rwx         rw-         r--

6. Variables

    (i) Variables Contains Peices of Data that can be used when Referenced the Variable
### In Bash Variables can be defined by starting with the name of the Variables followed by an Equal Sign "=" and then The Value to be Assigned

    (iii) Syntax:

<variableName> = <value>
    
    (iv) In Bash Variable can be Used by first adding `$` sign then the name of the Variable

    (v) Example:- 

$ name="James"
$ echo "Hello, It's nice to Meet you $name"
Hello, It's nice to Meet you James
    
    (vi) Built-in Variables:

- Built-in Variables in Bash are Variables which does not need to be defined by the User and rather is provided by the bash interpreter to Help us

- `$SHELL`: Returns The Value of The Current Shell You are Using

- `$USER`: Returns Name of The Current User

- `$PWD`: Returns Current Working Directory-e) `$HOSTNAME`: Returns Your Computer Name
-) `$RANDOM`: Returns a Random Number in-between 0 and 32765
- 
- - `$(($RANDOM % <n>))` Returns Random Number in-between 0 and <n>

- (vii) The Variables Provided by the Bash interpreter are `Enviorment Variables` meaning they - be used Everywhere and are Permanent Variables
- (viii) The Variables Defined by you The User are `Child Process` Variables meaning they -not be used outside of where they are define-    (ix) `export <VariableName>` makes the `Child Process` variable a `Enviorment Variable` meaning It makes that Variable Available Everywhere, but It doesn't make them Permanent meaning they can be lost after Shutdown/Restart
    (x) To Make a Enviorment Variable Permanent You'll need to be one your Home Directory and Open a File named ".bashrc" which is Hidden and Then Add Declaration for your File, export it, and finally logout and Log in Again, now That Variable is an Enviorment Variable and is Permanent unless you remove it from there

$ cd
$ nano .bashrc

```.bashrc

export <variableName>=<Value>

```
KEY: Ctrl + X
KEY: Y
KEY: Enter

$ sudo pkill -u $USER

7. Text Editors:

    (i) Text-Editors in Bash let's you edit text/script files without leaving your terminal

### `nano <filePath>` most simple and built-in Text-Editor

8. Conditions

    (i) if

if [[ <condition> ]]; then
    # If the condition is Met
fi

### If..else:

if [[ <condition> ]]; then
    # If the condition is Met
else
    # If the condition is Not Met
fi

    (iii) If..else:

if [[ <condition> ]]; then

    # If the condition is Met

elif [[ <DifferentCondition> ]]; then

    # If The First condition is Not Met this Condition will be checked
else

    # If none of the conditions is Met

fi

    (i) Case

case $<variable> in 
    <value1>)
#Commands to run if $variable == <value1>
;;
    <value2>)
#Commands to run if $variable == <value2>
;;
    <value3>)
#Commands to run if $variable == <value3>
;;
esac

9. Loops

    (i) While Loops

- Runs a Peice of Commands Over and Over While The Condition is True

- Syntax:

    while [[ <condition> ]]
    do
# Commands to run while the <condition> is true
    done

- While Loops doesn't uses normal Comparison Operators instead uses Flags:

    - `<a> -lt <b>` returns true if `a` is less than `b`
    - `<a> -gt <b>` returns true if `a` is greater than `b`
    - `<a> -le <b>` returns true if `a` is less than `b` or equals to `b`
    - `<a> -ge <b>` returns true if `a` is greater than `b` or equals to `b`- Example:
-  i=1
- while [[ $i -le 100 ]]
- do
echo $i
-i ++ )) # Increasing The Value of `i` by 1
- done
-  # Prints Every Line in a file One by One-   while read -r line; do
echo $line # <-- `$line` represets the curr- line of the file
    done < file.txt # <-- File Name

### Until Loops

- Runs a Peice of Commands Over and Over Until The Condition is True

- Syntax:

    while [[ <condition> ]]
    do
# Commands to run while the <condition> is true
    done

- Until Loops doesn't uses normal Comparison Operators instead uses Flags:

    - `<a> -le <b>` returns true while `a` is less than `b`

    - `<a> -gt <b>` returns true while `a` is greater than `b`

- Example:

    i=1
    until [[ $i == 100 ]]
    do
echo $i
(( i ++ )) # Increasing The Value of `i` by 1
    done

    (iii) For Loops

- For Loops doesn't uses any Bytes and instead uses a Range based Loop

- Syntax:

    for <iterator> in <list>; do
# Commands to run
    done

- Example:

    for i in {1..10}
echo "This Loop has ran $i Times!"
    done

    $ ./script.sh

    This Loop has ran 1 Times!
    This Loop has ran 2 Times!
    This Loop has ran 3 Times!
    This Loop has ran 4 Times!
    This Loop has ran 5 Times!
    This Loop has ran 6 Times!
    This Loop has ran 7 Times!
    This Loop has ran 8 Times!
    This Loop has ran 9 Times!
    This Loop has ran 10 Times!

    (iv) Loop Controls

- Loops Controls are Keywords that Controls the Flow of the Loops

- `continue` skips the Current Iteration

- `break` breaks/exits the Loop

Scripts:

10. Creating Scripts

    (i) File Extention for a Bash Script is "sh"

script.sh <-- Bash Script

### add "#!/bin/bash" to the first line of the Script to Define that it must be run by Bash and not any other kind of Scripting Language

#!/bin/bash
echo "Hello, World"

    (iii) Running a Bash Script: `bash <path>` or `<path>`

$ bash script.sh
Hello, World

$ # Make the File Executable
$ chmod +x script.sh
$ ./script.sh
Hello, World

11. More About Scripts

    (i) `read <variableName>` while the Script is Running It takes An Input from the User and Stores it in the given Variable

#!/bin/bash
echo "What's Your Name?:"
read name
echo "Hello, $name!"

$ bash script.sh
What's Your Name?:
FlytoTheSpace
Hello, FlytoTheSpace!

### `$<Count>` Represets the Arguments Given to The Script Before Running The Script

#!/bin/bash
name=$1
profession=$2
echo "Hello, My name's $name!"
echo "and I'm a $profession!"

    (iii) `$(<command>)` let's you get the return values of the Commands

#!/bin/bash
name=$(whoami)
echo "Hello, $name!"

flytothespace@ubuntu:~$ script.sh
Hello, flytothespace

    (iv) `exit <0 or 1>` exits The Script with The Status of 0 or 1, 1 stands for Success and 0 stands for Error

==========================================================================================================
											Command Prompt (CMD), Windows
==========================================================================================================

1. Commands

    (i) general

- `help`: helps you
- `<cmd> /?`: shows the manual of the command
- `<cmd> >> <file>`: writes stdout of the command to the file
- `doskey <switches?>`
- 
    - `/history`: Shows The Command Cline History
-) `start <URL>`: Opens Up the Specified URL in the default Browser
- Command Line Interface (CLI)-   - `prompt <MSG>$G`: sets prompt

(Note: leaving everthing empty-sets the prompt)-   - `title <MSG>`: Changes window title
    - `color <bg><fg>`: Changes Background/-eground Color-olors:-A) 0: Black
(B) 1: Blue
(C) 2: Green
(D) 3: Aqua/Cyan
(E) 4: Red
(F) 5: Purple
(G) 6: Yellow
(H) 7: White
- 8: Gray

Bright Colors:

(J) 9: Bright Blue
(K) A: Bright Green
(L) B: Bright Aqua/Cyan
(M) C: Bright Red
(N) D: Bright Purple
(O) E: Bright Yellow
(P) F: Bright White

(g) Programs

    - `explorer <path?>`: opens explorer
    - `notepad <file>`: opens file with notepad
    - `powershell <path?>`: opens powershell
    
### Navigation and File System

- `cd <path?>`: changes current working directory to path
- `dir <switches?>`: Lists Files/Folders, linux equivalent of `ls`

    - `/r`: Shows ADS Files

- `del <switches?> <path>`: Deletes

    -   `/q`:
    -  `/f`:
    - `/s`:

- `cipher <switches>`: Encrypts Files/Folders-   - `/E`: Encrypting everything in the Current Working Directory
-) `attrib <modifiers+attribute> <path>`-   - modifiers: +, -
    - Attribute-(A) `h`: hidden
(B) `s`: 
(C) `r`:-(f) `subst <letter>: <path>`: mounts a path as a drive-   - `/d <letter>`: unmounts a drive-   (iii) Network- `ping <options?> <URI>`: Pings The Server on URI 4 times-   - `-t`: ping Infinitely unless exited

- `ipconfig <switches?>`: show network info

    - `/all`: all information about your network
    - `/release`: Releases Your Private IPv4
    - `/release6`: Releases Your Private IPv6
    (IV) `/renew`: get a new Private IPv4 from DHCP
    (V) `/renew6`: get a new Private IPv6 from DHCP
    (VI) `/displaydns`: every DNS record fetched
    (VI) `/flushdns`: flushes DNS Records

- `nslookup <domain> <DNS server?> <options?>`: looks up the Domain based on query

    - `-type=<record>`: find a specific type of DNS record

- `getmac <options?>`: Get's your MAC Addresses-   - `/v`: Shows Every MAC Address of your Machine
-) `netsh <subcommands/flags?>`: networking related things-   subcommands:-   - `interface`

(A) `show-    I. `interface`: shows all network interfaces-B) `ip`
-  I. `show`-. `address`: shows IP Addresses
B. `dnsserve-: shows DNS servers

    - `wlan`

(A) `show`

    I. `wlanreport`: wlan status report (HTML)
    II. `profile <SSID?>`: shows Network Profile

A. `key=<clear>`: shows Password in <clear> Text

    - `advfirewall`

(A) `set`

    I. `allprofiles`

A. `state <on/off>`: turns on/off the windows defender firewall

    Flags:

    (IV) `-e`: Network Stastics
    (V) `-t <seconds>`: runs every <seconds> 
    (VI) `-af`: ports open
    (VII) `-o`: Network Processes

(f) `tracert <address> <flags?>`: traces network traffic and routers it's passing through and measures everything

    - `-d`: traces faster

(g) `route <subcommands?>`: network routes

    - `print`: prints all the network routes
    - `add <IP> mask <subnetmask> <newRoute>`: adds a new network route to IP
    - `delete <IP>`: removes IP from the network routes

(h) `scp <path> <user>@<host>:<remotepath>`: Copies File/Folder to The SSH Server, as user, on host, to remote-path

(i) `curl <flags?> <URI>`: fetches Data.

    - `--head`: find Redirected Destination
    - `--location <URI>`: Specify Location

    - Some servers:

(A) `wttr.in/<city>`: city weather
(B) `ASCII.live/can-you-hear-me`: Rick ROLLLLLLLLLL!!!
(C) `checkip.amazonwas.com`: your Public IP Address
(D) `qrenco.de/<MSG>`: generate a QR code
(E) `dict.org/d:<word>`: define a new word (fake) in the dictionary.

(j) `telnet <URI>`: Connects to The Telnet Server on the URI

    - Some servers

(A) `telehack.com`: some fun games and short films in CommandLine

    (iv) System

- `systeminfo` Shows System Info

- `powercfg <switches>`:

    - `/energy` : Energy Consumption Report (HTML)
    - `/batteryreport` : Battery Health Report (HTML)

- `assoc <switches?>`: File Type Associations with Programs

    - .<ext>=<program>: change File Type Association to a Program

- `chkdsk <switches?>`: checks up on your disk-   - `/f`: goes through each disk and fixes Issues
    (- `/r`: fixes physical sector issues-e) `sfc <switches?>`: System File Checker-   - `/scannow`: checks System Files and fixes corruptions-f) `DISM <switches?>`: Deploying Image Servicing Managemen-    - `/Online`: Online Mode
    - `/Cleanup-Imag- Cleans up the System Image
    - `/CheckHealth-Checks System Image Health
    (IV) `/RestoreHealt- restore System Image Health

(g) `tasklist`: lists running tasks
(h) `taskkill <options>`: kills tasks

    - `/f`: Force Kills a Task
    - `/pid <PID>`: Specifies Unique PID of the Task

(i) `shutdown <switches?>`

    -    `/?`:  Display help. This is the same as not typing any options.
    -   `/i`:  Display the graphical user interface (GUI). This must be the first option.
    -  `/l`:  Log off. This cannot be used with /m or /d options.
    (IV)   `/s`:  Shutdown the computer.
    (V)   `/sg`: Shutdown the computer. On the next boot, if Automatic Restart Sign-On is enabled, automatically sign in and lock last interactive user. After sign in, restart any registered applications.
    (VI)   `/r`:  Full shutdown and restart the computer.
    (VII)  `/g`:  Full shutdown and restart the computer. After the system is rebooted, if Automatic Restart Sign-On is enabled, automatically sign in and lock last interactive user. After sign in, restart any registered applications.
    (VIII) `/a`:  Abort a system shutdown. This can only be used during the time-out period. Combine with /fw to clear any pending boots to firmware.
    (IX)   `/p`:  Turn off the local computer with no time-out or warning. Can be used with /d and /f options.
    (X)    `/h`:  Hibernate the local computer. Can be used with the /f option.
    (XI) `/hybrid`: Performs a shutdown of the computer and prepares it for fast startup. Must be used with /s option.
    (XII)    `/fw`: Combine with a shutdown option to cause the next boot to go to the firmware user interface.
    (XIII)    `/e`: Document the reason for an unexpected shutdown of a computer.
    (XIV)     `/o`: Go to the advanced boot options menu and restart the computer. Must be used with /r option.
    (XV) `/m <host>`: Specify the target computer.
    (XVI) `/t <xxx>`: Set the time-out period before shutdown to xxx seconds. The valid range is 0-315360000 (10 years), with a default of 30. If the timeout period is greater than 0, the /f parameter is implied.
    (XVII) `/c "<comment>"`:  Comment on the reason for the restart or shutdown. Maximum of 512 characters allowed.
    (XVIII) `/f`:     Force running applications to close without forewarning users. The /f parameter is implied when a value greater than 0 is specified for the /t parameter.
    (XIX) `/d <[p|u:]xx:yy>`: Provide the reason for the restart or shutdown. p indicates that the restart or shutdown is planned. u indicates that the reason is user defined. If neither p nor u is specified the restart or shutdown is unplanned. xx is the major reason number (positive integer less than 256). yy is the minor reason number (positive integer less than 65536).
    
    (v) Piped

- `findstr <string>`: searches for the string inside the stdout of the Piped command
- `clip`: copies stdout to the Clipboard


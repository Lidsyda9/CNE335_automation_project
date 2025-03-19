Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\lidsy> ssh
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]
           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]
           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]
           [-J destination] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-Q query_option]
           [-R address] [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           destination [command [argument ...]]
PS C:\Users\lidsy> ssh -i C:Users\lidsy\downloads\Lidsyda_cne335_PEM.pem ece-user@ec2-34-219-149-76.us-west-2.compute.amazonaws.com
Warning: Identity file C:Users\lidsy\downloads\Lidsyda_cne335_PEM.pem not accessible: No such file or directory.
ssh: connect to host ec2-34-219-149-76.us-west-2.compute.amazonaws.com port 22: Connection timed out
PS C:\Users\lidsy> ssh -i C:\Users\lidsy\Downloads\Lidsyda_cne335_PEM.pem ec2-user@ec2-44-246-125-111.us-west-2.compute.amazonaws.com
The authenticity of host 'ec2-44-246-125-111.us-west-2.compute.amazonaws.com (44.246.125.111)' can't be established.
ED25519 key fingerprint is SHA256:oT3BgQ2o+89kw/ajF3/qsRKSGcWaDkK+t4KDDXt+B/c.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ec2-44-246-125-111.us-west-2.compute.amazonaws.com' (ED25519) to the list of known hosts.
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
[ec2-user@ip-172-31-16-72 ~]$

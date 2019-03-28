#!/usr/bin/env python

message = ["tangrong","network1301","18321432222","8151222"]

name,classroom,*phone = message

print(name,classroom,*phone)

passfile = "nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin"

print(passfile.split(':'))

user,*userinfo,bash = passfile.split(':')

print(user,bash)

user,*_,bash = passfile.split(':')

print(user,bash,_)

#废弃名称，比如 _ 或者 ign （ignore)
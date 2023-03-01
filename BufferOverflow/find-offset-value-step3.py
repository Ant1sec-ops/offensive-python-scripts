Find the offset value:

what we have :

EIP value: 76413176

Method 1: 
msf-pattern_offset  -q 76413176


or
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 76413176

Method 2: Note: same paused Immunity debugger . do not restart.
!mona findmsp -distance 1000

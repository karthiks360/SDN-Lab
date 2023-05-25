## To apply firewall rules

sudo ovs-ofctl add-flow s1 priority=100,dl_type=0x800,nw_src=10.0.0.1,nw_dst=10.0.0.3,action=drop

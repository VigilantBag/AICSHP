"""
swat-s1 utils.py
"""

from minicps.utils import build_debug_logger

PLC_SAMPLES = 100000000     # set the number of samples to be taken for the mainloop
PLC_PERIOD_SEC = 0.04       # plc update period in seconds
PATH = 'swat_s1_db.sqlite'  # set the path for the sqlite data file
NAME = 'swat_s1'            # name the network

SCHEMA = """
CREATE TABLE swat_s1 (
    name            TEXT NOT NULL,
    pid             INTEGER NOT NULL,
    value           TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO swat_s1 VALUES ('L001', 0, '1');
    INSERT INTO swat_s1 VALUES ('SW001', 0, '1');
"""

# Set the state of the network
STATE = {
    'name' : NAME,
    'path' : PATH
}

# Set the IPs of the PLC's on the network
IP = {
    'plc0' : '192.168.56.105',
    'plc1' : '192.168.56.106',
    'attacker' : '192.168.56.110',
}

# Set the mac addresses of the PLC's on the network
MAC = {
    'plc0': '00:1D:9C:C6:A0:60',
    'plc1': '00:1D:9C:C7:B0:70',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}

# Set the netmask of the network
NETMASK = '/24'

# TODO
PLC0_DATA = {
    'TODO' : 'TODO'
}

# Extract plc0 address from ip
PLC0_ADDR = IP['plc0']

# Information marking which PLC the information is comming from 
PLC0_TAGS = (
    ('L001', 0, 'INT'),
)

# Infrastructure for broadcasting information from PLC0 on the network
PLC0_SERVER = {
    'address' : PLC0_ADDR,
    'tags' : PLC0_TAGS
}

# Infrastructure for the protocol PLC0 will use
PLC0_PROTOCOL = {
    'name' : 'enip',
    'mode' : 1,
    'server' : PLC0_SERVER
}

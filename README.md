Assumptions made:
1. default flow logs(version 2 and above) and not custom format
2. flow logs do not contain column names
3. Possible list of protocols that could be found in VPC flow logs
4. Every log in flow logs file contains 14 or more space separated fields. The 14 fields are:
    # Version
    # Account ID
    # Network Interface ID
    # Source IP Address
    # Destination IP Address
    # Source Port
    # Destination Port
    # Protocol
    # Packets
    # Bytes
    # Start Time
    # End Time
    # Action
    # Log Status
    If some line doesn't contain 14 or more field values, it will be skipped by my parser code.
5. Outputs - Count of matches for each tag and count of matches for each port/protocol combination need to be CSV files
   without any blank line between any two consecutive lines.


Some comments:
1) I haven't used non default libraries but have used default libraries



References:
1) https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html
2) https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

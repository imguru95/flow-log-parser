# Assumptions made
1. The flow logs are in default format(versions 2 and above) and not custom format
2. Flow logs do not contain column names
3. Possible list of protocols that could be found in the input VPC flow logs - icmp, gmp, ggp, tcp, udp, rdp, rsvp, gre, esp, ah, icmpv6, sctp
4. Every log in flow logs file contains 14 or more space separated fields(default format version 2 has 14 fields with
   more additions for higher versions).
   The 14 fields are:
   1. Version
   2. Account ID
   3. Network Interface ID
   4. Source IP Address
   5. Destination IP Address
   6. Source Port
   7. Destination Port
   8. Protocol
   9. Packets
   10. Bytes
   11. Start Time
   12. End Time
   13. Action
   14. Log Status
   If some line doesn't contain 14 or more field values, it will be skipped by my parser code.
5. Outputs:
   1. Count of matches for each tag and count of matches for each port/protocol combination need to be CSV files
      without any blank line between any two consecutive lines.
   2. In the output file containing count of matches for each tag, the tag can be displayed in all lowercase.


# Some comments
1) No non default libraries have been used but default libraries have been used
2) Tests done - 
   1) Case-insensitive matching of tags and port/protocol combinations
   2) Verified that the program correctly generates output files for the given samples 
   3) Confirmed that flow log entries that do not match any entry in the lookup are categorized as "Untagged".
   4) Confirmed correct mapping of protocol numbers with protocol names


# How to run the program
1) Download the code. It can be done in two ways:
   1) Using git
      1) Open your command prompt(Windows) or Terminal in Linux/Mac and navigate to a specific folder using cd.
      2) Execute - "git clone https://github.com/imguru95/flow-log-parser.git"
      3) The code is downloaded
   2) Download code as zip
      1) Go to https://github.com/imguru95/flow-log-parser
      2) Click on Code(Green button) and under HTTPS click on "Download Zip"
      3) Unzip the downloaded "flow-log-parser-main" folder
2) Add flow logs and look up files
   1) In the folder - "flow-log-parser-main" that was downloaded in 2), add the flow logs and look up tables(do not create a subfolder for these files). Both these files should be .txt files
3) Ensure you have Python installed on your system. You can check if Python is installed by executing python --version in Terminal/Command Prompt
4) If Python is not installed, install it by following instructions from - https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/
5) Run the Python file run.py
   1) If you are on Windows, right click in folder and choose "Open in Terminal";
      If you are on Mac/Linux, open terminal and navigate to the folder - "flow-log-parser-main" using cd command. For
      example, if the "flow-log-parser-main" folder is in "Downloads", you can execute cd Downloads/flow-log-parser-main
      and navigate to the folder containing run.py
   2) Once in the appropriate folder, execute python run.py <flow_log_file_name> <lookup_table_file_name> <tag_counts_file_name> <port_protocol_counts_file_name>;
      note that <tag_counts_file_name> <port_protocol_counts_file_name> should have .csv extensions.
      For example the run command can be - python run.py flow_log.txt lookup_table.txt tag_counts.csv port_protocol_counts.csv
6) At the end of the code execution, two files are generated in the "flow-log-parser-main" folder - <tag_counts_file_name> and <port_protocol_counts_file_name> csv files
   <tag_counts_file_name> contains count of matches for each tag and <port_protocol_counts_file_name> contains count of matches for each port/protocol combination.
   Open these files in Excel.


# References:
1) https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html
2) https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

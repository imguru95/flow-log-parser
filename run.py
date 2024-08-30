import csv
import sys
from collections import defaultdict

protocols_dict = {
    "1": "icmp",
    "2": "igmp",
    "3": "ggp",
    "6": "tcp",
    "17": "udp",
    "27": "rdp",
    "46": "rsvp",
    "47": "gre",
    "50": "esp",
    "51": "ah",
    "58": "icmpv6",
    "132": "sctp",
}


def load_lookup_table(lookup_table_file):
    lookup_table = {}
    with open(lookup_table_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dstport = row["dstport"].strip()
            protocol = row["protocol"].strip().lower()
            tag = row["tag"].strip().lower()
            lookup_table[(dstport, protocol)] = tag
    print("Lookup table loaded!")
    return lookup_table


def parse_flow_logs(flow_log_file, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(flow_log_file, mode="r") as file:
        for line in file:
            if line != "\n":
                parts = line.split(" ")
                if len(parts) == 14:
                    dstport = parts[6].strip()
                    protocol_number = parts[7].strip()

                    # Map protocol number to protocol name
                    protocol_name = protocols_dict[protocol_number]

                    tag = lookup_table.get((dstport, protocol_name), "Untagged")
                    tag_counts[tag] += 1
                    port_protocol_counts[(dstport, protocol_name)] += 1
    print("Flow logs parsed successfully!")
    return tag_counts, port_protocol_counts


def generate_results(
    tag_counts, port_protocol_counts, tag_counts_file, port_protocol_counts_file
):
    with open(tag_counts_file, mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(["Tag", "Count"])
        for tag, count in sorted(tag_counts.items()):
            writer.writerow([tag, count])

    with open(port_protocol_counts_file, mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Protocol", "Count"])
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            writer.writerow([port, protocol, count])
    print("Output files generated!")


def run_parser(
    flow_log_file, lookup_table_file, tag_counts_file, port_protocol_counts_file
):
    lookup = load_lookup_table(lookup_table_file)
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup)
    generate_results(
        tag_counts, port_protocol_counts, tag_counts_file, port_protocol_counts_file
    )


if __name__ == "__main__":
    # run_parser("flow_logs.txt", "lookup_table.csv", "tag_counts.csv", "port_protocol_counts.csv")

    if len(sys.argv) != 5:
        print("Incorrect command!!!")
        print()
        print(
            f"Usage: python run.py <flow_log_file> <lookup_table_file> <tag_counts_file> <port_protocol_counts_file>"
        )
        sys.exit(1)

    flow_log_file, lookup_table_file, tag_counts_file, port_protocol_counts_file = sys.argv[1:5]

    run_parser(
        flow_log_file, lookup_table_file, tag_counts_file, port_protocol_counts_file
    )

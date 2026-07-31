# Importing analysis functions from analyzer.py
from analyzer import top_ips, top_statusCode, error_analysis

# Prints the report header banner
def print_header():
    print("=" * 40)
    print("ARJUN v0.3 REPORT")
    print("=" * 40)

# Prints a section title followed by a divider line
def print_section(title):
    print(title)
    print("-" * 40)

# Runs the full report: pulls data from analyzer.py and prints it section by section
def run_report():
    print_header()

    # Section: Top 5 IPs by request count
    print_section("Top IPs")
    print(top_ips())
    print()

    # Section: Breakdown of all status codes
    print_section("Status Codes")
    print(top_statusCode())
    print()

    # Get all error-related results from analyzer.py in one call
    error_summary, error_ip, error_endpoints = error_analysis()

    # Section: Count of each error status code
    print_section("Error Summary")
    print(error_summary)
    print()

    # Section: Top 5 IPs causing errors
    print_section("Top Error IPs")
    print(error_ip)
    print()

    # Section: Top 5 endpoints causing errors
    print_section("Top Error Endpoints")
    print(error_endpoints)
    print()

# Only run the report if this file is executed directly (not imported)
if __name__ == "__main__":
    run_report()
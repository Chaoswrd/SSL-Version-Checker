import ssl
import socket


def get_ssl_version(domain_name: str, port: int) -> int:
    context = ssl.create_default_context()
    with socket.create_connection((domain_name, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
            return ssock.version()


if __name__ == "__main__":
    import csv

    # Expects a file called services.csv and expects there to be a header (Domain Name & Port)
    csv_file_path = "services.csv"
    # Open the CSV file
    with open(csv_file_path, mode="r", newline="") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Loop over each row in the CSV
        for row in csv_reader:
            # Get the website from the current row
            domain_name = row["Domain Name"]
            port = row["Port"]
            ssl_version = get_ssl_version(domain_name, port)

            # Print the website or perform any other operation
            print(f"{domain_name}: {ssl_version}")

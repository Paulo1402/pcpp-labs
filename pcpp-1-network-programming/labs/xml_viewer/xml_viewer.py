import sys
import xml.etree.ElementTree as et


class XMLDataViewer:
    PADDING_SIZE = 5

    def __init__(self, file_path):
        self._file_path = file_path

        self._headers = None
        self._collumn_width_helper = None

    def view(self, container_selector, headers, node_value_header=None):
        if node_value_header and node_value_header not in headers:
            raise ValueError(
                f"Node value header {node_value_header} must be in headers"
            )

        # Save reference for further usage
        self._headers = headers

        tree = et.parse(self._file_path)
        root = tree.getroot()

        container = root.find(container_selector)

        if container is None:
            raise RuntimeError("Container selector didn't return any elements")

        container_data = self._get_container_data(container, node_value_header)

        self._print_header()
        self._print_body(container_data)

    def _get_container_data(self, container: et.Element, node_value_header: str):
        data = []
        self._collumn_width_helper = {}

        for node in container:
            # Get node attributes
            node_data = list(node.items())

            # Get node value if header is set
            if node_value_header:
                node_value = node.text
                node_data.append((node_value_header, node_value))

            # Iterate by index to update the item later
            for i in range(len(node_data)):
                header, value = node_data[i]

                # Get match header using the real header name (header_name == HEADER_NAME)
                # The match header will be used everywhere else so it matches headers param
                match_header = self._get_match_header(header)

                # Skip if the node attribute isn't included in the given headers
                if not match_header:
                    continue

                # Update collumn width based on the value width
                if match_header not in self._collumn_width_helper:
                    self._collumn_width_helper[match_header] = 0

                width = len(value)

                if width > self._collumn_width_helper[match_header]:
                    self._collumn_width_helper[match_header] = width

                # Overwrite node data to use match header
                node_data[i] = (match_header, value)

            # Sort data by headers order
            node_data.sort(key=lambda row: self._headers.index(row[0]))
            data.append(node_data)

        return data

    def _get_match_header(self, header):
        for h in self._headers:
            if h.lower() == header.lower():
                return h

        return None

    def _print_header(self):
        for header in self._headers:
            width = self._collumn_width_helper[header]
            self._print_with_padding(header, width)

        divider_length = sum(
            self._collumn_width_helper.values()
        ) + self.PADDING_SIZE * len(self._headers)

        print()
        print("-" * (divider_length))

    def _print_body(self, container_data):
        for row in container_data:
            for header, value in row:
                width = self._collumn_width_helper[header]
                self._print_with_padding(value, width)

            print()

    def _print_with_padding(self, value, width):
        print(value, end="")
        print(" " * (width - len(value) + self.PADDING_SIZE), end="")


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print("XML file path must be informed")
        exit(1)

    file = sys.argv[1]

    try:
        viwer = XMLDataViewer(file)
        viwer.view(
            container_selector=".",
            headers=["COMPANY", "LAST", "CHANGE", "MIN", "MAX"],
            node_value_header="COMPANY",
        )
    except FileNotFoundError as e:
        print("File not found: ", e)
        exit(1)
    except et.ParseError as e:
        print(f"File at {file} can't be parsed: ", e)

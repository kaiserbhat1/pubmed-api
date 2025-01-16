# PubMed Paper Fetcher

This Python program fetches research papers from PubMed based on a user-specified query. It identifies authors affiliated with pharmaceutical or biotech companies and exports the results as a CSV file.

## Installation

1. Install Poetry (if not already installed).
2. Run `poetry install` to install dependencies.

## Usage

```bash
get-papers-list "<your_query>" [-f <output_filename>] [-d]
```
## Arguments

- <your_query>: Search query for PubMed.

- -f <output_filename>: Save results to a CSV file.

- -d: Enable debug output.

Example
```bash
get-papers-list "cancer immunotherapy" -f results.csv -d
```
This will fetch papers related to cancer immunotherapy, filter out authors from pharmaceutical companies, and save the results to results.csv.

## Tools Used

- [PubMed E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25497/#chapter2.The_Nine_Eutilities_in_Brief)

- [Poetry](https://python-poetry.org/docs/)

### Conclusion

This implementation provides a complete Python program to fetch and filter PubMed papers, identify non-academic authors, and export the results to a CSV file. The code is organized, reusable, and supports a command-line interface for flexible use.
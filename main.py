# importing necessary modules
from fetch import Fetch
from savefile import Save
import argparse

# file = Fetch.fetch_pub_med_data("cancer",100)
# Save.save_to_csv(file,"data.csv")

def run():

    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query",type=str,help=" eg: 'cancer'")
    parser.add_argument("-f","--file",type=str,help="File name to save results. eg: 'data.csv'")
    parser.add_argument("-d","--debug",action="store_true",help="Enable debug output.")
    args = parser.parse_args()
    if args.debug:
        print(f"Running with the current: {args.query}")
    query = args.query
    if query:
        papers = Fetch.fetch_pub_med_data(query,100)
        if args.file:
            Save.save_to_csv(papers,args.file)
            print(f"Results Saved as {args.file}")
        else:
            print(papers)

# initializing main
if __name__ == "__main__":
    run()
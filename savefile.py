import csv
from typing import List

class Save:
    @staticmethod
    def save_to_csv(papers:List[dict],filename:str):
        """
         Saves the filtered papers to a CSV file.

         Args:
             papers (List[dict]): List of filtered papers.
             filename (str): The filename to save the results.
         """

        fieldnames = ["PubmedID","Title","Publication Date","Non-academicAuthors","CompanyAffiliations","Corresponding Author Email"]
        with open(filename,"w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for paper in papers:
                writer.writerow({
                    "PubmedID":paper["PubmedID"],
                    "Title":paper["Title"],
                    "Publication Date":paper["Publication Date"],
                    "Non-academicAuthors":paper["Non-academicAuthor(s)"],
                    "CompanyAffiliations":paper["CompanyAffiliation(s)"],
                    "Corresponding Author Email": paper["Corresponding Author Email"],

                })

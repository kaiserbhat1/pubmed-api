from typing import List
from utility import NON_ACADEMIC_KEYWORDS,PUBMED_URL
import xml.etree.cElementTree as et

import requests
class Fetch:


    @staticmethod
    def fetch_pub_med_data(query:str,max_results: int = 10)-> List [dict]:
        """
            Fetches PubMed papers based on a user-defined query.

            Args:
                query (str): The search query to be used in PubMed.
                max_results (int): The maximum number of results to fetch.

            Returns:
                 List[dict]: Filtered papers with relevant authors and company affiliations.
            """

        search_url = f"{PUBMED_URL}esearch.fcgi"

        search_params = {
            "db":"pubmed",
            "term":query,
            "retmode":"json",
            "retmax":max_results
        }
        with requests.get(search_url,params=search_params) as response:

            paper_ids=[each_id for each_id in response.json()["esearchresult"]["idlist"]]

        fetch_url = f"{PUBMED_URL}efetch.fcgi"
        fetch_params = {
            "db": "pubmed",
            "id":",".join(paper_ids),
            "retmode": "xml",
            "rettype":"abstract"

        }
        papers = []
        with requests.get(fetch_url,params=fetch_params) as response:
            response.raise_for_status()

            root = et.fromstring(response.text)


            for doc in root.findall(".//PubmedArticle"):

                paper = {}

                paper["PubmedID"] = doc.find(".//PMID").text
                paper["Title"] = doc.find(".//ArticleTitle").text

                if doc.find('.//PubDate/Year') is not None:
                    year = doc.find('.//PubDate/Year').text
                else:
                    year = "Null"
                if doc.find('.//PubDate/Month') is not None:
                    month = doc.find('.//PubDate/Month').text
                else:
                    month = "Null"
                paper["Publication Date"] = f"{month}-{year}"
                authors = [author for author in doc.find(".//AuthorList")]

                aff = []
                author = []
                email = []

                # Filters out authors affiliated with pharmaceutical or biotech companies.
                for affiliations in authors:
                    for affiliation in affiliations.findall(".//Affiliation"):
                        for keyword in NON_ACADEMIC_KEYWORDS:
                            if keyword.lower() in affiliation.text.lower().replace(",","").split():
                               author.append(f"{affiliations.find(".//ForeName").text} {affiliations.find(".//LastName").text}" )
                               if affiliation.text not in aff:
                                   if "@" in affiliation.text:
                                       words = affiliation.text.split()
                                       length = len(words)
                                       text = ""
                                       for i in range(length):
                                           if i != length-1:
                                             text+= f"{words[i]} "
                                           else:
                                             email.append(words[i])
                                       aff.append(text)

                                   else:
                                       aff.append(affiliation.text)


                if author:
                    paper["Non-academicAuthor(s)"] = author
                else:
                    paper["Non-academicAuthor(s)"] = None
                if aff:
                    paper["CompanyAffiliation(s)"] = aff
                else:
                    paper["CompanyAffiliation(s)"] = None
                if email:
                    paper["Corresponding Author Email(s)"] = email
                else:
                    paper["Corresponding Author Email(s)"] = "Null"

                if author and aff:
                    if paper not in papers:
                        papers.append(paper)


            return papers



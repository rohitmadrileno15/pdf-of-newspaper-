from pathlib import Path
from datetime import datetime
from PyPDF2 import PdfFileMerger
import requests

  


def get_newspaper ( dt , dwn_path ):

	for i in range(1,9):
		filename = Path(dwn_path + '/' + str(i) + '.' + 'newspaper.pdf')
		url = "https://www.tripuraobserver.com/PDFs/" + dt + "." + str(i)  + ".pdf"
		response = requests.get(url)
		filename.write_bytes(response.content)
	print( "Merging the files ... ")


def merge_pdf ( dwn_path ):
	pdfs = [ ]

	for i in range(1, 9):
		pdfs.append(  str(i) + ".newspaper.pdf")

	merger = PdfFileMerger()

	for pdf in pdfs:
	    merger.append( dwn_path + "/" + pdf)

	merger.write(dwn_path+ "/" + "tripuraobserver.pdf")

	merger.close()
	
	for i in pdfs:
		Path( dwn_path + "/" + i ).unlink()

	print("Get the file in " + dwn_path+ "/" + "tripuraobserver.pdf")


if __name__ == "__main__":
	print("Tripura Observer Newspaper on " , datetime.now().date() )
	dwn_path = str(input("Enter Download Path"))
	# "C:/Users/HP WORLD/Desktop/SCREENSHOTS"
	dt_value = datetime.now().strftime("20"+'%y%m%d')
	get_newspaper( dt_value ,  dwn_path )
	merge_pdf( dwn_path )
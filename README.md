# HRMelthylation
This is my first real program ever written. 

HRM-AUC calculator

Present files:

--> PyHRMelt.ipynb
	# Contains the functional script for doing all the calculations. Relies on Numpy, Pandas and matplotlib.
	Input = CSV with the melting temperatures of each well.
		First row contains well number.
		First column contains the temperature when fluorescence read was made.
		The rest contains the RFU-reads for each well at a specific temperature.
	Output= For now it outputs all the calculated AUC (of the normalized dataset) in a row.

	TO-DO:  [X] Output the values as a CSV file.
		[ ] Output the values next to the well number.
		[ ] Output the values as a 96-well plate.

	ADDED CHANGES:

	LAST THING TRIED:
  
  
  
  --> PyQt5-fileopensavedialogs.py
	# Template file downloaded from: https://pythonspot.com/en/pyqt5-file-dialog/
	  Contains the functions for PyQt5 to "open a file", "open multiple files" and "saving file(s)".
	
	TO-DO: [ ] 
  
  
--> PyQt5w_Matplot-template.py
	# Template file containing a randomly generated matplotlib graph and a button that does not do anything.

	TO-DO: (Hiearchial order)
		[ ] Make the button open a file dialog when pressed
		[ ] Make two windows that asks for the max/min temp for the Normalization.
		[ ] Make a slide/multiple buttons that will allow you to change view from
			*RAW RFU values
			*d(RFU)/dT (of RAW)
			*Normalized RFU values
			**d(RFU)/dT (of Normalized)

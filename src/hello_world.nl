ACC 00000001x00000000		 	//allocate one byte in 0th registry
MV  00000000 00000001 			//move value from the 0th registry to the 1st
ACC 00000001x00000010 			//allocate one byte in 2nd registry
SUM 00000010 00000001 			//sum values from 1st and 2nd registry, The sum will be stored in the first available registry, unless specified					
					//The registry to store sum might be specified, look example below.
SUM 00000010 00000001 x00000100      	//This will store the sum in the 3rd registry
					//The other way to specify result's address is by using variables:

ASN 'MYVAR' SUM 00000010 00000001  	//assign the value of the sum to the variable 'MYVAR'.This will be held in temporary registry
MV  'MYVAR' x00010000 			//This will be moved to the specified memory address.


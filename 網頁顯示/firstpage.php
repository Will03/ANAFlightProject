<!DOCTYPE html>
<html>
<head>
	<title>NAN Flight</title>
</head>
<body>

 <div class="MainPicture">
   <img src="./images/ANAlogo.png" alt="An Image">
 </div>



<div>
	<form method = "POST" action=firstpage.php>
		<dl class="m_retDateDl" style="display: block;">
		<dt>
			<br><br>Start Date
		</dt>
		<dd>
		<input type="text" name="sdate" id="sdate" class="Date" value="2017,07,19" >
		<dt>
			<br><br>End Date
		</dt>

		<dd>
		<input type="text" name="edate" id="edate" class="Date" value="2017,07,19" >
		<dt>
			<br><br>Departure Airport
		</dt>
		<dd>
		<input id="departureAirport" type="text" name="departureAirport" value="高知">
		<dt>
			<br><br>Arrival Airport
		</dt>
		<dd>
		<input id="arrivalAirport" type="text" name="arrivalAirport" value="福岡">
		</dd>
			<br><br>
		<dd>
		<input type="submit" name="btn" id="submit" value="submit">
		</dd>
		</dl>
	</form>	
</div>

<div>
<?php

$StartDate = $_POST["sdate"];
$EndDate = $_POST["edate"];
$DepartureAirport = $_POST["departureAirport"];
$arrivalAirport = $_POST["arrivalAirport"];
if($StartDate != "")
{
	$mystring = system("python algorithm.py $StartDate $EndDate $DepartureAirport $arrivalAirport", $retval);
	// print "<br>Data<br>";
	// print "
	// StartDate = $StartDate<br>
	// EndDate = $EndDate<br>
	// DepartureAirport = $DepartureAirport<br>
	// arrivalAirport = $arrivalAirport<br>
	// ";
}


?>
</div>
</body>
</html>




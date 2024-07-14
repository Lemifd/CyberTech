<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table</title>
</head>
<body>
    <?php

$servername = "localhost";
$username = "lemi";
$password = "password";
$database="myDB";


// Create connection
$connected = new mysqli($servername, $username, $password, $database);


$sql = "SELECT id, user, passw, reg_date FROM MyGuests";
$result = mysqli_query($connected, $sql);

if (mysqli_num_rows($result) > 0) {
  echo "<table><tr><th>Id</th><th>Username</th><th>Password</th><th>Date<th></tr>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr><td>". $row["id"] . "</td> <td>". $row["user"]. "</td> <td>". $row["passw"]. "</td><td>". $row["reg_date"] . "</td></tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}

mysqli_close($conn);

    ?>


</body>
</html>
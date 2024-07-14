<!DOCTYPE html>
<html>
  <head>
    <title>Admin Login</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
      }

      #container {
        width: 400px;
        margin: 0 auto;
        margin-top: 100px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        padding: 20px;
      }

      h1 {
        text-align: center;
        margin: 0 0 20px 0;
      }

      input[type="text"],
      input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 16px;
        box-sizing: border-box;
      }

      input[type="submit"] {
        background-color: #4CAF50;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
      }

      input[type="submit"]:hover {
        background-color: #3e8e41;
      }

      .error {
        color: red;
        margin-bottom: 10px;
      }
    </style>
  </head>
  <body>
    <div id="container">
      <h1>Admin Login</h1>
      <?php
        if (isset($_POST['submit'])) {
          $username = $_POST['username'];
          $password = $_POST['password'];
          // Connect to the database
          $conn = mysqli_connect('localhost', 'admin', 'password', 'my_database');
          if (!$conn) {
            die('Could not connect to the database: ');
          }
          // Query the database for the user's credentials
          $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
          $result = mysqli_query($conn, $query);
          if (mysqli_num_rows($result) == 1) {
            // Credentials are valid, redirect to the admin page
            header('Location: admin.php');
            exit();
          } else {
            // Credentials are invalid, display an error message
            echo '<p class="error">Invalid username or password</p>';
          }
          mysqli_close($conn);
        }
      ?>
      <form method="post" action="#">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <input type="submit" name="submit" value="Login">
      </form>
    </div>
  </body>
</html>
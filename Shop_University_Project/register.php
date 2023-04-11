<?php
    session_start();
    if ($_SESSION['user']) {
        header('Location: profile.php');
    }
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Authorization and Registration</title>
    <link rel="stylesheet" href="assets/css/main.css">
</head>
<body>

    <!-- Форма регистрации -->

    <form action="vendor/signup.php" method="post" enctype="multipart/form-data">
        <label>Full name</label>
        <input type="text" name="full_name" placeholder="Enter your full name">
        <label>Login</label>
        <input type="text" name="login" placeholder="Enter your login">
        <label>Mail</label>
        <input type="email" name="email" placeholder="Enter your email">
        <label>Password</label>
        <input type="password" name="password" placeholder="Enter the password">
        <label>Password confirmation</label>
        <input type="password" name="password_confirm" placeholder="Confirm password">
        <button type="submit">Log in</button>
        <p>
            Do you already have an account? - <a href="/">log in</a>!
        </p>
        <?php
            if ($_SESSION['message']) {
                echo '<p class="msg"> ' . $_SESSION['message'] . ' </p>';
            }
            unset($_SESSION['message']);
        ?>
    </form>

</body>
</html>

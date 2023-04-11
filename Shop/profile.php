<?php
session_start();
if (!$_SESSION['user']) {
    header('Location: /');
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

    <!-- Профиль -->

    <form>
        <img src="<?= $_SESSION['user'] ?>" width="200" alt="">
        <h2 style="margin: 10px 0;">Welcome <?= $_SESSION['user']['full_name'] ?></h2>
        <p></p>
        <a href="#">Electronic box : <?= $_SESSION['user']['email'] ?></a>
                <p></p>
        <a href="vendor/logout.php" class="logout">Go back</a>
        <p></p>
        <li><a href="index.html"><i class="fa fa-sign-in" aria-hidden="true"></i>Go to the main page</a></li>
    </form>

</body>
</html>

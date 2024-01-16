
<!-- Sindi Gurakuqi -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Good day!</title>
    <link rel="stylesheet" href="styles8.css">
</head>
<body>
    
<?php

function getSetHitCount() {
    $count = 1;

    if (isset($_COOKIE['hit_count'])) {
        $count = $_COOKIE['hit_count'] + 1;
    }

    setcookie('hit_count', $count, time() + 86400 * 30); 

    return $count;
}

$hitCount = getSetHitCount();
?>

<?php

function getCustomImage() {
    if (isset($_GET['image'])) {
        $imageName = $_GET['image'];
        $allowedImages = ['moonwitch.gif', 'skeldance.gif', 'jackwalk.gif'];

        if (in_array($imageName, $allowedImages)) {
            return $imageName;
        }
    }
}

$customImage = getCustomImage();
?>

<?php
date_default_timezone_set('America/Toronto'); 

$hour = date('G');

if ($hour >= 5 && $hour < 12) {
    $class = 'morning';
    $greeting = 'Good morning!';
    $background_image = 'morning.jpg';
} elseif ($hour >= 12 && $hour < 18) {
    $class = 'afternoon';
    $greeting = 'Good afternoon!';
    $background_image = 'afternoon.jpg';
} elseif ($hour >= 18 && $hour < 21) {
    $class = 'evening';
    $greeting = 'Good evening!';
    $background_image = 'evening.jpg';
} else {
    $class = 'night';
    $greeting = 'Good night!';
    $background_image = 'night.jpg';
}
?>


<header style="background-image: url('<?= $background_image ?>');" alt="<?= $class ?> background image">
    <h1><?= $greeting ?></h1>
    <?php if (isset($customImage)) : ?>
        <img id="custom-image" src="<?= $customImage ?>" alt="Custom Halloween Image">
    <?php endif; ?>
</header>

<form action="lab08b.php" method="post" target="_blank">
    <label for="number1">Enter first number (3-12): </label>
    <input type="number" name="number1" id="number1">

    <label for="number2">Enter second number (3-12): </label>
    <input type="number" name="number2" id="number2">

    <button type="submit">Generate Table</button>
</form>

<div id="hit-counter">Hits: <?= $hitCount ?></div>

</body>
</html>
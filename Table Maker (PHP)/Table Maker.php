<!-- Sindi Gurakuqi -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiplication Table</title>
    <link rel="stylesheet" href="styles8.css">
</head>
<body>

<?php
    $number1 = isset($_POST['number1']) ? intval($_POST['number1']) : 0;
    $number2 = isset($_POST['number2']) ? intval($_POST['number2']) : 0;

    if ($number1 < 3 || $number1 > 12 || $number2 < 3 || $number2 > 12) {
?>
        <p class="error">Please enter numbers between 3 and 12. <a href="lab08.php">Go back to the form</a>.</p>
<?php
    } else {
?>
        <table>
            <?php
            for ($i = 1; $i <= $number1; $i++) {
                echo '<tr>';
                for ($j = 1; $j <= $number2; $j++) {
                    echo '<td>' . $i * $j . '</td>';
                }
                echo '</tr>';
            }
            ?>
        </table>
<?php
    }
?>

</body>
</html>
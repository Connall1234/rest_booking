$(document).ready(function() {
    // Initialize date picker for meal_day field with id "id_meal_day"
    $('#id_meal_day').datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: 0 // Prevent selection of past dates
    });

    // Initialize date picker for meal_day field with id "meal_day_filter"
    $('#meal_day_filter').datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: 0 // Prevent selection of past dates
    });
});


// Check the type of the value
console.log(typeof mealDayValue);

// This will hide the first choice for the meal time dropdown element"
var dropdown1 = document.getElementById("id_meal_time");
dropdown1.options[0].style.display = "none"; 


// This will hide the first choice for the special occasion dropdown element"
var dropdown2 = document.getElementById("id_special_occasion");
dropdown2.options[0].style.display = "none";






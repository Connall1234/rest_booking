$(document).ready(function() {
    // Initialize date picker for meal_day field with id "id_meal_day"
    $('#search_button').prop('readonly', true)

    $('#id_meal_day').datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: 0 // Prevent selection of past dates
    });

    // Initialize date picker for meal_day field with id "meal_day_filter"
    $('#meal_day_filter').datepicker({
        dateFormat: 'yy-mm-dd',
        //Will not be adding present day only, so admin can look at past bookings
        onSelect: function(dateText) {
            // Enable the search button when a valid date is selected
            $('#search_button').prop('disabled', false);
        }
    });
});

    $('#search_button').prop('disabled', true);
        
// This will hide the first choice for the meal time dropdown element"
var dropdown1 = document.getElementById("id_meal_time");
dropdown1.options[0].style.display = "none"; 

// This will hide the first choice for the special occasion dropdown element"
var dropdown2 = document.getElementById("id_special_occasion");
dropdown2.options[0].style.display = "none";

// Add an event listener to the navbar toggler button
document.querySelector('.navbar-toggler').addEventListener('click', function () {
    // Toggle the 'show' class on the collapsible navbar content
    document.querySelector('#navbarNav').classList.toggle('show');
});

// Close the navbar when a nav-link is clicked (optional)
document.querySelectorAll('.nav-link').forEach(function (element) {
    element.addEventListener('click', function () {
        // Check if the collapsible navbar content is currently shown
        if (document.querySelector('#navbarNav').classList.contains('show')) {
            // Hide the collapsible navbar content
            document.querySelector('#navbarNav').classList.remove('show');
        }
    });
});
// Add confirmation to our delete button
function confirmDelete() {
    return confirm("Are you sure you want to delete this booking?");
}

//document.addEventListener("DOMContentLoaded", function() {
    // Your JavaScript code goes here
//});


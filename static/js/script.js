$(document).ready(function() {
    
});

function add_ingredient() {
    let ingredients = ($("#ingredientsList").html());
    let totalIngredients = $("#ingredientsList").find(".form-control").length + 1;
    $("#ingredientsList").append("<label class='stepLabel' for='instruction" + totalIngredients + "'>Ingredient " 
    + totalIngredients + "</label><input id='ingredient" + totalIngredients
    + "' name='ingredient" + totalIngredients
    + "' type='text' class='form-control'>");
}
    
    function add_cooking_step() {
        
    }
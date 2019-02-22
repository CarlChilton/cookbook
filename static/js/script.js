$(document).ready(function() {
    $("#ingredientsList").find(".ingredient")
});

$("#addRecipeForm").on("submit", function(e) {
    e.preventDefault();
    console.log("Stopped it");
    return false;
});

function add_ingredient() {
    let totalIngredients = $("#ingredientsList").find(".form-control").length + 1;
    $("#ingredientsList").append("<label class='stepLabel' for='ingredient" + totalIngredients + "'>Ingredient " 
    + totalIngredients + "</label><input id='ingredient" + totalIngredients
    + "' name='ingredient" + totalIngredients
    + "' type='text' class='form-control'>");
}

function add_instruction() {
    let totalInstructions = $("#instructionsList").find(".form-control").length + 1;
    $("#instructionsList").append("<label class='stepLabel' for='instruction" + totalInstructions + "'>Step " 
    + totalInstructions + "</label><input id='ingredient" + totalInstructions
    + "' name='instruction" + totalInstructions
    + "' type='text' class='form-control'>");
}
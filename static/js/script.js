$(document).ready(function() {
    $("body").on("click", ".removeInput", function() {
        let currentList = $(this).closest(".form-group");
        $(this).closest(".addedInputGroup").remove();
        let totalInputs = $(currentList).find(".addedInputGroup").length;
        for (i=0; i < totalInputs; i++) {
            currentLabel = $(currentList).find(".addedInputGroup").eq(i).find("label").text();
            currentLabel = currentLabel.substr(0, currentLabel.length - 1);
            $(currentList).find(".addedInputGroup").eq(i).find("label").text(currentLabel + (i + 2));
        }
    });
});

function add_ingredient() {
    let totalIngredients = $("#ingredientsList").find(".form-control").length + 1;
    $("#ingredientsList").append("<div class='addedInputGroup'><label class='stepLabel' for='ingredient" + totalIngredients + "'>Ingredient " 
    + totalIngredients + "</label><input id='ingredient" + totalIngredients
    + "' name='ingredient" + totalIngredients
    + "' type='text' class='addedInput form-control'><div " 
    + "class='removeInput btn btn-danger'><i class='fas fa-times'></i></div></div>");
}

function add_instruction() {
    let totalInstructions = $("#instructionsList").find(".form-control").length + 1;
    $("#instructionsList").append("<div class='addedInputGroup'><label class='stepLabel' for='instruction" + totalInstructions + "'>Step " 
    + totalInstructions + "</label><input id='ingredient" + totalInstructions
    + "' name='instruction" + totalInstructions
    + "' type='text' class='addedInput form-control'><div " 
    + "class='removeInput btn btn-danger'><i class='fas fa-times'></i></div></div>");
    
}

// function removeInput(element) {
//     console.log(element);
//     // console.log("YAY");
//     // console.log($(this).closest(".addedInputGroup"));
//     $(this).closest(".addedInputGroup").remove();
// }


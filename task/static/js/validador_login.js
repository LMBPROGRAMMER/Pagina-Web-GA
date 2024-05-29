// objeto.metodo(json)

$(document).ready(function () {
    $("#formulario_ingresar").validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 5,
            },
        
        }, // --> Fin de reglas
        messages: {
            email: {
                required: "El email es un campo requerido",
                email: "El email no cumple el formato de un correo",
            },
            
            password: {
                required: "La contraseña es una campo obligatorio",
                minlength: "Mínimo 5 caracteres",
            },
        },
    });
});
// objeto.metodo(json)

$(document).ready(function () {
    $("#formulario_ingresar").validate({
        rules: {
            nombre: {
                required: true,
            },
            password: {
                required: true,
                minlength: 5,
            },
        
        }, // --> Fin de reglas
        messages: {
            
            nombre: {
                required: "El Nombre es un campo requerido",
                nombre: "El Nombre no es válido",
            },
            
            password: {
                required: "La contraseña es una campo obligatorio",
                minlength: "Mínimo 5 caracteres",
            },
        },
    });
});
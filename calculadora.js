function calculadora() {
    while (true) {
        console.log("1 sumar. ");
        console.log("2 resta. ");
        console.log("3 multiplicacion. ");
        console.log("4 division. ");
        console.log("5 salir. ");
    
        let operacion = prompt("elije una operacion del 1 al 5: ");
        
        if (operacion === "5") {
            console.log("saliendo de la calculadora...");
            break;
        }

        let numero1 = parseFloat(prompt("ingresa el primer numero: "));
        let numero2 = parseFloat(prompt("ingresa el segundo numero: "));

        let resultado;

        if (operacion === "1") {
            resultado = numero1 + numero2;
            console.log("el resultado de la suma es: " + resultado);
        } else if (operacion === "2") {
            resultado = numero1 - numero2;
            console.log("el resultado de la resta es: " + resultado);
        } else if (operacion === "3") {
            resultado = numero1 * numero2;
            console.log("el resultado de la multiplicacion es: " + resultado);
        } else if (operacion === "4") {
            resultado = numero1 / numero2;
            console.log("el resultado de la division es: " + resultado);
        } else {
            console.log("esta opcion no se encuentra en la lista. Vuelva a intentarlo!");
        }

    }

}

calculadora();
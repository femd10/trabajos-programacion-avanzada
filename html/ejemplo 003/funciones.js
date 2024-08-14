function saludar(){
	var nombre = document.getElementById("txtNombre").value;
	var edad = parseInt(document.getElementById("txtEdad",10).value);
	var msg = "";
	
	document.getElementById("txtNombre").value = "";
	document.getElementById("txtEdad").value = "";
	
	if(edad > 18){
		msg = "eres mayor de edad, puedes continuar";
	}else{
		msg = "eres muy joven para este sitio";
	}
	
	alert("Hola " + nombre + " tienes " + edad);
	document.getElementById("divSaludo").innerHTML = msg;
	
	
}

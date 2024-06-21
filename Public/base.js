
// Função para aplicar máscara ao campo de entrada celular
function applyMaskToPhoneInput() {
	$("#userFone").mask("(00) 00000-0000");
}


// Aplicar as máscaras quando o documento estiver pronto
$(document).ready(function () {
	applyMaskToPhoneInput();
});

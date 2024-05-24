// Función para procesar los mensajes recibidos del nodo MQTT de entrada function procesarMensaje(msg) {
// Extraer el valor numérico de la intensidad lumínica del mensaje
var light intensity = msg.payload.light_intensity;
// Ajustar el valor de la intensidad lumínica al rango esperado
var adjusted_intensity = Math.min(Math.max(light_intensity, 0), 100); // Ajustar al rango 0-100
// Enviar el valor ajustado de la intensidad lumínica al siguiente nodo
msg.payload= adjusted_intensity;
return msg;
}
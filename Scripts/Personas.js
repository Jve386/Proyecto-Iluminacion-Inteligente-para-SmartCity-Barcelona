// Convertir msg.payload a cadena JSON si no lo es
const payloadString = typeof msg.payload == 'string' ? msg.payload: JSON.stringify(msg.payload);
// Parsear el mensaje MQTT recibido
const data = JSON.parse(payloadString);
// Obtener el número de personas detectadas del mensaje
const numberOfPeople = data.persons_detected;
// Configurar el mensaje MQTT de salida
msg.topic= "sensores/iluminacion"; // Tema MQTT al que se enviarán los datos
msg.payload={ "persons_detected": numberOfPeople }; // Datos de detección de personas return msg;
boolean activado, deteccion;
void setup() {
  Serial.begin(9600);
  pinMode(9,OUTPUT);
  digitalWrite(9,LOW);
  activado= false;
  deteccion = false;
  
  

}

void loop() {
  if (Serial.available()){
    String lectura = Serial.readString();
    Serial.print(lectura);
    if (lectura == "123"){
      activado = (!activado);
      if(activado){
        tone(10,200,100);
        delay(1000);
        tone(10,200,100);
        delay(1000);
        tone(10,200,100);
        digitalWrite(9,HIGH);
        Serial.println("Alarma activada");
        delay(1000);
      }
      else{
        digitalWrite(9,LOW);
        deteccion= false;
        noTone(10);
        Serial.println("Alarma desactivada...");
      }
      lectura= "";
    }
  }
  if(activado){
    int luz= analogRead(A1);
    if(luz > 500 or deteccion==true){
      deteccion= true;
      sonido();
    }
  }

}

void sonido(){
  for (int i=200;i<500; i++){
    tone(10,i,10000);
  }
}

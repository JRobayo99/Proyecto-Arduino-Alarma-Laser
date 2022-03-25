# Proyecto Sensor Detector Arduino ODS
### Pregunta.

------------

¿Como se pude hacer un sistema de seguridad simple y económico?¿Esto puede garantizar el sentido de binestar general o un desarrollo tecnológico?




### Introducción.
------------

A lo largo de estos años  se ha buscado unas solución mas eficiente para las problemáticas de la humanidad y el medio ambiente, hacia los objetivos de desarrollo sostenible. Hoy en día, gracias al manejo de estos objetivos se están generando avances que  construyen una visión del futuro que se desea. Con este proyecto que se enfoca en la seguridad se quiere apoyar algunos de estos objetivos para solucionar algunas de estas problemáticas que plantea en el desarrollo sostenible.

### Descripcion de la problematica

------------


En un cojunto residencial, se observa la falta de sistemas de monitoreo, pues los robos y atracos aumentaron con el paso del tiempo, amenzando la sensación de bienestar de los residentes, también por la poca presencia de vigilantes, en los horarios en que suceden los robos, estos manifiestan que no tienen medios en los poder mejorar su eficacia de vigilacia y los medios de vigilacia son demsiado caros, para que la comunidad los compre.

###  Descripcion de la solucion

------------

Mediante el uso de la plataforma de arduino y de python, también de componentes fiisicos como el laser o la celda por ejemplo, podemos hacer un sistema de deteccion que nos pueda garantizar una mejora en los niveles de seguridad y que esta sirva de apoyo para la labor de los vigilantes, mejorando así el bienestar en seguridad que tanto a aquejado a esta comunidad.

#### ODS que se utilizaron el el proyecto

------------


Los ODS (objetivos de desarrollo soostenible), en los que el proyecto esta enfocado serían dos.
El número 3 que seria el de salud y bienestar.

![image](https://user-images.githubusercontent.com/98995639/160111319-f9613f4f-50fd-496d-b1be-130dad9f4c92.png)

Link imagen: https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2018/07/S_SDG-goals_icons-individual-rgb-09.png

El número 9 que es Industria,Innovación e infraestructura.

![image](https://user-images.githubusercontent.com/98995639/160111344-631c948e-ac58-4f3a-b75a-f18a62ced990.png)

Link imagen: https://www.fundacionlealtad.org/wp-content/uploads/2021/03/S-WEB-Goal-03-1024x1024.png

### Diagrama Relacional
------------
![image](https://user-images.githubusercontent.com/98995639/160110153-b2a7e814-d8aa-4413-b035-d780b6f8b496.png)

### Diagrama De Conecciones
------------
![image](https://user-images.githubusercontent.com/98995639/160053819-548298ea-30ab-4b05-aea2-f58f3604611a.png)

Imagen obtenida de: https://www.youtube.com/watch?v=MMOGGFUamFg&ab_channel=LaBuhardillaDelLoco

### Código Python
------------

![image](https://user-images.githubusercontent.com/98995639/160125337-f3745c15-c22a-466e-bd9f-241d8da1d909.png)

https://colab.research.google.com/drive/1AH9IdFNH7dHWIEaQ4LMIjZW5ShW78IRL?usp=sharing

### Código Arduino

boolean activado, deteccion;
void setup() {
  Serial.begin(9600);
  pinMode(9,OUTPUT); //laser
  digitalWrite(9,LOW);
  activado = false;
  deteccion = false;
}
void loop() {
  if( Serial.available()!= -1 ){

    String lectura = Serial.readString();

    if (lectura == "1234"){
      activado = !activado;
      if (activado){
        tone(10,200,100);
        delay(1000);
        tone(10,200,100);
        delay(1000);
        tone(10,200,100);
        digitalWrite(9,HIGH);
        Serial.println("Alarma activada!");
        delay(1000);
      }
      else{
        digitalWrite(9,LOW);
        deteccion = false;
        noTone(10);
        Serial.println("Alarma desativada...");         
      }
      lectura="";
    }  
  }  


  if(activado){
    int luz = analogRead(A1);
    Serial.println(luz);
    if(luz > 500 or deteccion == true){
      deteccion == true;
      sonido();
    }
  }
} 


void sonido(){
  for(int i = 200;i<500;i++){
    tone(10,i,10000);
  }
}
 
### Herramientas necesarias para el desarrollo de la solución
------------
![WhatsApp Image 2022-03-25 at 7 49 42 AM](https://user-images.githubusercontent.com/102251544/160124310-d568d204-dda0-449a-9574-6baa6410f9d7.jpeg)
#### Arduino IDE

El software Arduino de código abierto (IDE) facilita la escritura de código y la carga en la placa. Este software se puede utilizar con cualquier placa Arduino. (Arduino, 2022)

#### Arduino UNO
Es una placa que tiene todos los elementos necesarios para conectar periféricos a las entradas y salidas de un microcontrolador. Es decir, es una placa impresa con los componentes necesarios para que funcione el microcontrolador y su comunicación con un ordenador a través de la comunicación serial. (BeJob, 2017)

#### Laser
El módulo KY-008 es un emisor de luz láser de color rojo y que cuenta con un pin de alimentación (S), un pin GND (-) y un tercer pin central que no sirve para nada. (El Octavo Bit, 2021)

#### Protoboard
La protoboard es una placa de pruebas con numerosos orificios en los cuales se pueden insertar diferentes cables y componentes facilitando la creación de circuitos. Los orificios de la placa están conectados a través de pequeñas laminas metálicas de manera que los orificios de una misma fila están conectados entre sí. (Ferrer, 2020)

#### Fotocelda
La fotocelda es un dispositivo electrónico capaz de producir una pequeña cantidad de corriente eléctrica al ser expuesta a la luz. Esta variación es debido a una resistencia, cuyo valor en ohmios varia ante las variaciones de la luz que la fotocelda percibe (Electrotec, 2022)

#### Buzzer
es un pequeño transductor capaz de convertir la energía eléctrica en sonido. Se basa en el efecto piezoeléctrico de los materiales, este efecto funciona de tal manera que cuando se aplica un voltaje el volumen del material cambia ligeramente. (UAEH, 2021)
#### resistor
Un resistor es uno de los componentes electrónicos más usados en la práctica, y está diseñado con diferentes propósitos, como lo pueden ser la disipación de potencia, la generación de calor, la limitación de corriente, entre otros. Estos tienen un código de barras de colores con el cual se puede encontrar su valor y así ser usados de forma precisa en un circuito. (Anaya, 2022)

#### Python
Es un lenguaje de programación sencillo de leer y escribir que permite el desarrollo de software de manera fácil y no necesita ser compilado para ejecutar las aplicaciones escritas.  (Santander Becas, 2022)

### Conclusiones
------------
-	Se implementaron conocimientos adquiridos de forma autónoma en el desarrollo de un proyecto que ayuda a la sostenibilidad.
-	Se aprendieron nuevos conceptos acerca de la programación de Arduino.
-	Los instrumentos utilizados se ensamblaron adecuadamente, dando un resultado satisfactorio.
-	La herramienta desarrollada puede ser en relación utilidad-costo muy efectiva.


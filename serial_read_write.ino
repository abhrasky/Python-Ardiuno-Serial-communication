
String data;
char EOM='\n'; //end of message; 
float dat;
void setup( )  
{  
Serial.begin(9600);  
}  
void loop( )  
{  
data=Serial.readStringUntil(EOM);

dat=data.toFloat();

dat=dat*2.5;


Serial.println(dat);
delay(100);
} 

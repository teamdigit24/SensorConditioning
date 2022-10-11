void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
}

float V0[3] = {0}; 
int R0; 
float V1[3] = {0}; 
int R1;
float V2[3] = {0}; 
int R2;  
float V3[3] = {0}; 
int R3; 
float V4[3] = {0}; 
int R4; 
  
void loop() {
  // put your main code here, to run repeatedly:
 
 R0 = analogRead(A0);  //Read data from analog pin
 R1 = analogRead(A1); 
 R2 = analogRead(A2); 
 R3 = analogRead(A3); 
 R4 = analogRead(A4); 
 
 for(int ii = 0; ii < 2; ii++) //Save 3 points for moving average on each channel 
 {
    V0[ii] = V0[ii+1]; 
    V1[ii] = V1[ii+1]; 
    V2[ii] = V2[ii+1]; 
    V3[ii] = V3[ii+1]; 
    V4[ii] = V4[ii+1]; 
 }
 
 V0[2] = (float) R0*5/1023; //Convert AtoD integer to voltage level 
 V1[2] = (float) R1*5/1023;
 V2[2] = (float) R2*5/1023;
 V3[2] = (float) R3*5/1023;
 V4[2] = (float) R4*5/1023;
 
 Serial.print((V0[0]+V0[1]+V0[2])/3); //Compute moving average for each channel and send via serial port 
 Serial.print(',');
 Serial.print((V1[0]+V1[1]+V1[2])/3); 
 Serial.print(',');
 Serial.print((V2[0]+V2[1]+V2[2])/3); 
 Serial.print(',');
 Serial.print((V3[0]+V3[1]+V3[2])/3); 
 Serial.print(',');
 Serial.println((V4[0]+V4[1]+V4[2])/3); 

// Serial.println(V0[2]); //Optional raw data for comparison
// Serial.println(V1[2]); 
// Serial.println(V2[2]); 
// Serial.println(V3[2]); 
// Serial.println(V4[2]); 
 
  delay(33); //Set sample rate to ~30Hz 

}

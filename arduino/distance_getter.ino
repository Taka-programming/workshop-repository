
#define TRG 10
#define ECH 11
#define HIGHTIME 10

void setup() {
Serial.begin(9600);
pinMode(TRG, OUTPUT); //TRGピンを出力に設定
pinMode(ECH, INPUT); //ECHピンを入力に設定
}

void loop() {
int diff;
float dis;
digitalWrite(TRG,HIGH); //プルアップ抵抗を有効化
delayMicroseconds(HIGHTIME); //超音波とばす
digitalWrite(TRG, LOW); //プルアップ抵抗を無効化
diff = pulseIn(ECH, HIGH); //ECHピンに入力されるパルスを検出
dis = (float)diff * 0.01715; 
Serial.print(dis); //距離を表示
Serial.println("cm"); //単位を表示
delay(1000);
}

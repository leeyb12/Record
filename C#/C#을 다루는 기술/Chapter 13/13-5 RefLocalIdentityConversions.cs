// 참조 지역 변수 선언 시 ID 변환

(int x, int y) tuple1 = (10, 20);
ref (int a, int b) tuple2 = ref tuple1;
tuple2.a = 30;
Console.WriteLine(tuple1.x);
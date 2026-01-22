// 두 개의 변수를 통해 증가 연산을 두 번 수행

int x = 10;
ref int y = ref x;
x++;
y++;
Console.WriteLine(x);
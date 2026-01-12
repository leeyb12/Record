# 03. 데이터 보관하기

## 3.1 다양한 데이터 종류
- 모든 데이터의 형식의 근간을 이루는 "기본 데이터 형식(Primitive Type)"과 상수(Constants), 열거형(Enumerator)를 배운다.
- "기본 데이터 형식(Primitive Type)"과 "복합 데이터 형식(Complex Data Type)"이 있다. 
  ```mermaid
  flowchart LR
  subgraph T1["데이터 형식"]
    A["기본 데이터 형식"]
    B["복합 데이터 형식"]
  end
  ```
- 복합 데이터 형식에는 구조체와 클래스, 배열 등이 있다.
- 데이터 형식은 기본 데이터 형식과 복합 데이터 형식, 값 형식과 참조 형식으로 분류할 수 있다.

<br><br>

## 3.2 변수 
- 제일 먼저 데이터의 형식을 명시하고 변수 식별자(이름)을 명시한 후 `;`로 문장을 종결하여 변수를 선언한다. 예) `int x;`
  - 이렇게 하면 컴파일러는 int 형식을 위해 메모리 공간을 할당하고 x라는 식별자가 사용할 수 있도록 준비한다. 
- 선언된 변수 x는 대입 연산자를 통해 데이터를 입력할 수 있다. 예) `x = 100;`
  - 이를 통해 x에 할당된 메모리 공간에 데이터 100이 기록된다. 
  - 초기화란, 변수에 최초의 데이터를 할당하는 것을 의미한다. 
```cs
int x; x = 100;
int y = 100;
int a = 30, b, c = 0, d;
```

<br><br>

## 3.3 값 형식과 참조 형식
- 값 형식(Value Type)은 변수가 값을 담는 데이터 형식을 말한다.
- 참조 형식(Reference Type)은 변수가 값 대신 값이 있는 곳의 위치를 담는 데이터 형식이다.
- C#에서 사용하는 두 가지 메모리 영역인 스택(Stack), 힙(Heap)
- 값 형식과 관련있는 것은 스택 메모리 영역, 참조 형식과 관련있는 것은 힙 메모리 영역이다.

### 3.3.1 스택과 값 형식

```cs
{ // 코드 블록 시작
    int a = 100;
    int b = 200;
    int c = 300;
} // 코드 블록 끝
```
- 코드에 선언된 세 변수 a, b, c는 차례로 스택에 쌓였다가 코드블록이 끝나면서 스택에 걷혀 제거된다. a > b > c 순으로 스택에 쌓였다가, c > b > a 순으로 스택에 빠져 나간다.
- 코드블록 안에 생성된 모든 값 형식의 변수들은 프로그램 실행이 중괄호"}"를 만나면 메모리에서 제거된다.
- 아래 표는 스택 메모리에 할당되는 과정을 보여준다.

| { | int a = 10; | int b = 20; | int c = 30; |    }   |        |   |
|:-:|:-----------:|:-----------:|:-----------:|:------:|:------:|---|
|   |             |             | c : 30      |        |        |   |
|   |             | b : 20      | b : 20      | b = 20 |        |   |
|   | a : 10      | a : 10      | a : 10      | a : 10 | a : 10 |   |

<br>

### 3.3.2 힙과 참조 형식

- 힙은 저장된 `데이터를 스스로 제거하는 메커니즘을 갖고 있지 않다.`
- 대신 CLR 가비지 컬렉터(Garbage Collector)가 제거한다.
  - 가비지 컬렉터는 프로그램 뒤에 숨어서 동작하면서, 힙에 더 이상 사용하지 않는 객체가 있으면 그 객체를 쓰레기로 간주하고 수거하는 기능을 한다.
- 힙은 코드블록이 끝나는 시점에 상관없이 데이터를 유지한다.
- 따라서 CLR에 메모리 영역을 제공한다.
- 힙 영역에는 데이터를 저장하고, 스택 영역에는 데이터가 저장된 힙 메모리의 주소를 저장한다.
- 이를 "참조"한다고 한다.
  ```cs
  {
    object a = 10;
    object b = 20;
  }
  ```
- CLR이 이 코드를 실행하면, 실제 값은 힙에 저장되고, a와 b는 값이 저장된 힙 주소만 스택에 저장된다.

| 스택      |   | 힙 | 메모리 주소 |
|-----------|---|----|--------|
|           |   |    | 1000   |
|           |   | 20 | 2000   |
|           |   |    | 3000   |
| b : &2000 |   | 10 | 4000   |
| a : &4000 |   |    | …      |

- 코드가 마치는 "}"에 스택 메모리 데이터는 삭제된다. 하지만 힙에는 여전히 데이터가 저장되어 있다. 
- 이후 가비지 컬렉터가 더이상 참조하는 곳이 없을 때 데이터를 정리한다. 


<br><br>

## 3.4 기본 데이터 형식

- C#에 제공하는 기본 데이터 형식에는 모두 15가지가 있다. 
- 숫자, 논리, 문자열, 오브젝트 형식으로 나뉘어진다.

<br>

### 3.4.1 숫자 데이터 형식

#### 정수 계열 형식

| 데이터 형식 | 설명    | 크기(바이트) | 값의 범위    |
|:------:|:------------:|:-----------:|:-------------|
| byte   | 부호x 정수                 | 1(8비트)  | 0~255                                          |
| sbyte  | signed byte<br>정수         | 1(8비트)  | -128~127                                       |
| short  | 정수                     | 2(16비트) | 0~65,535                                       |
| ushort | unsigned short<br>부호없는 정수 | 2(16비트) | -32,768~32767                                  |
| int    | 정수                     | 4(32비트) | -2,147,483,648~2,147,483,647                   |
| usint  | 부호없는 정수                | 4(32비트) | 0~4,294,967,295                                |
| long   | 정수                     | 8(64비트) | -922,337,203685,477,58~922,337,203,685,477,507 |
| ulong  | 부호없는 정수                | 8(64비트) | 0~18,446,744,073,709,551,615                   |
| char   | 유니코드 문자                | 2(16비트) |        |

#### 정수 예제 프로그램 
```cs
using System;

namespace IntegralTypes
{
  class MainApp
  {
    static void Main(string[] args)
    {
      sbyte a = -10;
      byte b = 40;

      Console.WriteLine($"a={a}, b={b}");

      short c = -30000;
      ushort d = 60000;

      Console.WriteLine($"c={c}, d={d}");

      int e = -1000_0000;  // 0이 7개
      uint f = 3_0000_0000;  // 0이 8개

      Console.WriteLine($"e={e}, f={f}");

      long g = -5000_0000_0000;  // 0이 11개
      ulong h = 200_0000_0000_0000_0000;  // 0이 18개

      Console.WriteLine($"g={g}, h={h}");
    }
  }
}
```

>>> 
### 실행 결과 
a=-10, b=40
c=-30000, d=60000
e=-10000000, f=300000000
g=-500000000000, h=20000000000000000
>>>


#### 2진수, 10진수, 16진수 리터럴

```cs
using System;

namespace IntegerLiterals
{
  class MainApp
  {
    static void Main(string[] args)
    {
      byte a = 240;  // 10진수 리터럴
      Console.WriteLine($"a={a}");

      byte b = 0b1111_0000;  // 2진수 리터럴
      Console.WriteLine($"b={b}");

      byte c = 0XF0;  // 16진수 리터럴
      Console.WriteLine($"c={c}");

      uint d = 0x1234_abcd;  // 16진수 리터럴
      Console.WriteLine($"d={d}");
    }
  }
}
```

>>> 
### 실행 결과
a=240
b=240
c=240
d=305441741
>>>

#### 부호 있는 정수와 부호 없는 정수
- byte의 경우 1바이트, 8비트로 이루어진 값이다. 이는 8개의 0과 1로 이루어진 값이다.
- 1은 0000_0001, 3은 0000_0010, 127은 0111_1111 이다.
- 음수는 가장 첫 번째 비트를 통해 나타내며, 부호비트(Sign Bit)라고 한다.
- 음수 비트는 다음 과정을 거쳐 이루어진다.
  1. 먼저 수 부분 비트를 채운다.
  2. 그 후 전체 비트를 반전시킨다.
  3. 반전된 비트에 1을 더한다. 
- 즉, -1은 1111_1111이다.

```cs
using System;

namespace SignedUnsigned
{
  class MainApp
  {
    static void Main(string[] args)
    {
      byte a = 255;
      sbyte b = (sbyte)a;

      Console.WriteLine(a);
      Console.WriteLine(b);
    }
  }
}
```

>>> 
### 실행 결과
255
-1
>>>

#### 데이터가 넘쳐 흘러요
- 데이터 형식의 크기를 넘어선 값을 담으면 넘친다.
- 이를 오버플로(Overflow)라고 한다.

```cs
using System;

namespace Overflow
{
  class MainApp
  {
    static void Main(string[] args)
    {
      uint a = uint.MaxValue;

      Console.WriteLine(a);

      a = a + 1;

      Console.WriteLine(a);
    }
  }
}
```

>>> 
### 실행 결과
4294967295
0
>>>

<br>

### 3.4.2 부동 소수점 형식

- 부동: 뜰 부 + 움직일 동, 떠서 움직인다는 뜻으로, 소수점이 고정 되지 않고 움직이면서 수를 표현한다는 뜻에서 지어진 이름이다.

| 데이터 형식 | 설명               | 크기(바이트) | 값의 범위                                    |
|:------:|:----------------:|:-------:|------------------------------------------|
| float  | 단일 정밀도 부동 소수점 형식 | 4(32비트) | -3.402823e38~3.402823e38                 |
| double | 복수 정밀도 부동 소수점 형식 | 8(64비트) | -1.7976313486232e308~1.7976313486232e308 |

- float라는 이름은 Floating Point
- double은 Double Precision Floating Point Format 이다.
- C#의 float와 double은 IEEE754라는 표준 알고리즘에 기반한 데이터 형식이다.
- IEEE754에 따르면 4바이트(32비트)의 float를 표현할 때, 앞 1비트는 부호전용, 가수부 23비트는 수를 표현할 때, 나머지 지수부 8비트는 소수점의 위치를 나타내기 위해 사용한다.
- float의 유효숫자는 7자리이다.
- double의 유효숫자는 15~16자리이다.

```cs
using System;

namespace FloatingPoint
{
  class MainApp
  {
    static void Main(string[] args)
    {
      float a = 3.1415_9265_3589_7932_3846f;
      Console.WriteLine(a);

      double b = 3.1415_9265_3589_7932_3846;
      Console.WriteLine(b);
    }
  }
}
```
>>>
### 실행 결과
3.1415927
3.141592653589793
>>>

#### decimal 형식
- decimal도 실수를 다루는 데이터 형식이지만, 부동소수점과는 다른 방식으로 소수를 다루며 정밀도가 훨씬 높다.

| 데이터 형식 | 설명               | 크기(바이트) | 값의 범위                                    |
|:------:|:----------------:|:-------:|------------------------------------------|
| decimal | 복수 정밀도 부동 소수점 형식 | 16(128비트) | -1.0x10e~ ±7.9x10e28 |

```cs
using System;

namespace Decimal
{
  class MainApp
  {
    static void Main(string[] args)
    {
      float a = 3.1415_9265_3589_7932_3846_2643_3832_79f;
      double b = 3.1415_9265_3589_7932_3846_2643_3832_79;
      decimal c = 3.1415_9265_3589_7932_3846_2643_3832_79m;

      Console.WriteLine(a);
      Console.WriteLine(b);
      Console.WriteLine(c);
    }
  }
}
```
>>>
### 실행 결과
3.1415927
3.141592653589793
3.1415926535897932384626433833
>>>

<br>

### 3.4.3 문자 형식과 문자열 형식

- char 형식의 변수에 문자 데이터를 담는다. ' '로 표현한다.

```cs
using System;

namespace Char
{
  class MainApp
  {
    static void Main(string[] args)
    {
      char a = '안';
      char b = '녕';
      char c = '하';
      char d = '세';
      char e = '요';

      Console.Write(a);
      Console.Write(b);
      Console.Write(c);
      Console.Write(d);
      Console.Write(e);
      Console.WriteLine();
    }
  }
}
```
>>> 
### 실행 결과
안녕하세요
>>>

- string 형식은 여러개의 문자를 묶어서 처리한다. " "로 표현한다.

```cs
using System;

namespace String
{
  class MainApp
  {
    static void Main(string[] args)
    {
      string a = "안녕하세요?";
      string b = "박상현입니다.";

      Console.WriteLine(a);
      Console.WriteLine(b);
    }
  }
}
```
>>> 
### 실행 결과
안녕하세요?
박상현입니다.
>>>

<br>

### 3.4.4 논리 형식

- 논리 형식이 다루는 데이터는 참(True)와 거짓(False) 두 가지이다.

| 데이터 형식 | 설명 | 크기(바이트) | 값의 범위 |
|:------:|:------:|:-------:|-------|
| bool  | 논리 형식 | 1(8비트) | true,false |

- `if (result == 0)`와 같이 0이 어떤 의미인지를 헷갈릴 수 있기 때문에 `if (result)`와 같이 사용한다.

```cs
using System;

namespace Bool
{
  class MainApp
  {
    static void Main(string[] args)
    {
      bool a = true;
      bool b = false;

      Console.WriteLine(a);
      Console.WriteLine(b);
    }
  }
}
```
>>> 
### 실행 결과
True
False
>>>

<br>

### 3.4.5 object 형식

- object는 물건, 객체라는 뜻이다. 어떤 데이터든지 다룰 수 있는 데이터이다.
- 이는 "상속"의 료과를 활용할 수 있다.
- C#에서는 object 형식으로부터 상속받게 하여, 모든 데이터 형식을 담아 처리할 수 있다.
- object 형식은 참조 형식이기 때문에 힙에 데이터를 저장한다.

```cs
using System;

namespace Object 
{
  class Program
  {
    static void Main(string[] args)
    {
      object a = 123;
      object b = 3.14159265358979328462643383279m;
      object c = true;
      object d = "안녕하세요.";

      Console.WriteLine(a);
      Console.WriteLine(b);
      Console.WriteLine(c);
      Console.WriteLine(d);
    }
  }
}
```
>>> 
### 실행 결과
123
3.1415926535897932384626433833
True
안녕하세요.
>>>

<br>

### 3.4.6 박싱과 언박싱

- object 형식은 값 형식의 데이터를 할당하기 위한 "박싱(Boxing)" 기능을 제공한다.
- object 형식에 값 형식의 데이터를 할당하려는 시도가 이루어지면 object 형식은 박싱을 수행해서 해당 데이터를 힙에 할당한다.
- `object a = 20;` 이 코드에서 20를 박스에 담아 힙에 할당된다. a는 그 주소를 참조한다.
- 힙에 있던 값 형식의 데이터를 값 형식 객체에 다시 할당해야 하는 경우, `int b = (int)a;`와 같은 경우, b는 a가 참조하고 있는 메모리로부터 값을 복사한다.
- 이때 박싱된 값을 건 값 형식 변수에 저장하는 과정을 "언박싱(unboxing)"이라고 한다.

```cs
using System;

namespace BoxingUnboxing
{
  class MainApp
  {
    static void Main(string[] args)
    {
      int a = 123;
      object b = (object)a;  // a에 담긴 값을 박싱해서 힙에 저장
      int c = (int)b;  // b에 담긴 값을 언박싱해서 스택에 저장

      Console.WriteLine(a);
      Console.WriteLine(b);
      Console.WriteLine(c);

      double x = 3.1414213;  
      object y = x;  // x에 담긴 값을 박싱해서 힙에 저장
      double z = (double)y;  // y에 담긴 값을 언박싱해서 스택에 저장

      Console.WriteLine(x);
      Console.WriteLine(y);
      Console.WriteLine(z);
    }
  }
}
```
>>>
### 실행 결과 
123
123
123
3.1414213
3.1414213
3.1414213
>>> 

<br>

### 3.4.7 데이터 형식 바꾸기
- 변수를 다른 데이터 형식의 변수에 옮겨 담는 것을 형식 변환(Type Conversion)이라고 한다.
- 박싱과 언박싱도 값 형식과 참조 형식간의 형식 변환이라 할 수 있다.
- 다음과 같은 5가지 형식변환을 공부한다.
  1. 크기(표현 범위)가 서로 다른 정수 형식 사이의 변환
     - 작은 정수 형식의 변수에 있는 데이터를 큰 정수로 옮길 때는 문제 없다.
     - 반대의 경우 데이터 형식 변환하려는 대상 변수의 용량보다 큰 경우에는 오버플로우가 발생한다. (특별한 메시지는 없다.)
     ```cs
     using System;

     namespace IntegralConversion
     {
      class MainApp
      {
        static void Main(string[] args)
        {
          sbyte a = 127;
          Console.WriteLine(a);

          int b = (int)a;
          Console.WriteLine(b);

          int x = 128;  // sbyte의 최대값 127보다 1 큰 수
          Console.WriteLine(x);

          sbyte y = (sbyte)x;
          Console.WriteLine(y);
        }
      }
     }
     ```
     >>> 
     ### 실행 결과
     127
     127
     128
     -128
     >>>

  2. 크기가 서로 다른 부동 소수점 형식 사이의 변환
     - 부동 소수점 형식의 특성상 오버플로가 존재하지 않는다.
     - 정밀성에 손상이 이루어진다.
     - 2진수로는 소수를 완전히 다루지 않는다. 따라서 손상이 발생할 수 있다.
     ```cs
     using System;

     namespace FloatConversion
     {
      class MainApp
      {
        static void Main(string[] args)
        {
          float a = 69.6875f;
          Console.WriteLine("a : {0}", a);

          double b = (double)a;
          Console.WriteLine("b : {0}", b);
          Console.WriteLine("69.6875 == b : {0}", 69.6875 == b);

          float x = 0.1f;
          Console.WriteLine("x : {0}", x);

          double y = (double)x;
          Console.WriteLine("y : {0}", y);

          Console.WriteLine("0.1 == y : {0}", 0.1 == y);
        }
      }
     }
     ```
     >>>
     ### 실행 결과
     a : 69.6875
     b : 69.6875
     69.6875 == b : True
     x : 0.1
     y : 0.10000000149011612
     0.1 == y : False
     >>>

  3. 부동이 있는 정수 형식과 부호 없는 정수 형식 사이의 변환
     ```cs
     using System;

     namespace SignedUnsignedConversion
     {
       class MainApp
       {
         static void Main(string[] args)
         {
           int a = 500;
           Console.WriteLine(a);

           uint b = (uint)a;
           Console.WriteLine(b);

           int x = -30;
           Console.WriteLine(x);

           uint y = (uint)x;
           Console.WriteLine(y);
         }
       }
     }
     ```
     >>> 
     ### 실행 결과
     500
     500
     -30
     4294967266
     >>>

  4. 부동 소수점 형식과 정수 형식 사이의 변환
     - 소수점에서 정수로 변환될 때 반올림은 존재하지 않는다. 예) 0.9 > 0
     ```cs
     using System;

     namespace FloatToIntegral
     {
      class MainApp
      {
        static void Main(string[] args)
        {
          float a = 0.9f;
          int b = (int)a;
          Console.WriteLine(b);

          float c = 1.1f;
          int d = (int)c;
          Console.WriteLine(d);
        }
      }
     }
     ```
     >>> 
     ### 실행 결과
     0
     1
     >>>

  5. 문자열과 숫자 사이의 변환
     - 문자-숫자의 변환은 자주 이루어진다.
     - 숫자 > 문자는 변수.ToString()을 통해 이루어진다.
     - 문자 > 숫자는 형식.Parse(문자)를 통해 이루어진다.
     ```cs
     using System;

     namespace StringNumberConversion
     {
      class MainApp
      {
        static void Main(string[] args)
        {
          int a = 123;
          string b = a.ToString();
          Console.WriteLine(b);

          float c = 3.14f;
          string d = c.ToString();
          Console.WriteLine(d);

          string e = "123456";
          int f = Convert.ToInt32(e);
          Console.WriteLine(f);

          string g = "1.2345";
          float h = float.Parse(g);
          Console.WriteLine(h);
        }
      }
     }
     ```
     >>> 
     ### 실행 결과
     123
     3.14
     123456
     1.2345
     >>>

<br><br>

### 3.5 상수와 열거 형식

- 변수는 담고 있는 데이터를 얼마든지 변경할 수 있는 메모리 공간이다.
- 상수(Constants)와 열거 형식(Enumerator)은 변수와 달리 안에 담긴 데이터를 절대 바꿀 수 없는 메모리 공간이다.
- 이는 값을 바꾸지 말아야 할 변수를 실수로 건드리는 것을 방지해준다.

<br>

### 3.5.1 상수 - 언제나 변하지 않을 거예요

- 데이터 형식 앞에 const 키워드가 위치하고, 반드시 상수가 가져야 하는 데이터를 반드시 대입해주어야 한다.
- `const 자료형 상수명 = 값;`
- 한 번 선언한 뒤로는 바꿀 수 없다. 바꾸려고 하면 에러 메시지를 쏟아낸다.
```cs
using System;

namespace Constant
{
  class MainApp
  {
    static void Main(string[] args)
    {
      const int MAX_INT = 2147483647;
      const int MIN_INT = -2147483648;

      Console.WriteLine(MAX_INT);
      Console.WriteLine(MIN_INT);
    }
  }
}
```
>>>
### 실행 결과
2147483647
-2147483648
>>>

<br>

### 3.5.2 열거 형식 - 여러 개의 상수를 정리합니다.

- 종류는 같지만 다른 값을 갖는 상수를 선언해야 할 때가 가끔 있다.
  ```cs
  const int RESULT_YES = 1;
  const int RESULT_NO = 2; 
  const int RESULT_CONFIRM = 3;
  const int RESULT_CANCLE = 4;
  const int RESULT_OK = 5;
  ```
- 실수를 방지하기 위해 enum 이라는 키워드를 사용한다. (첫번째 요소는 0이다)
- `enum 열거 형식명 : 기반자료형 { 상수1, 상수2, 상수3, ... }` 
- `enum DialogResult { YES, NO, CANCEL, CONFIRM, OK }`
  ```cs
  using System;

  namespace Enum
  {
    class MainApp
    {
      enum DialogResult { YES, NO, CANCEL, CONFIRM, OK }

      static void Main(string[] args)
      {
        Console.WriteLine((int)DialogResult.YES);
        Console.WriteLine((int)DialogResult.NO);
        Console.WriteLine((int)DialogResult.CANCEL);
        Console.WriteLine((int)DialogResult.CONFIRM);
        Console.WriteLine((int)DialogResult.OK);
      }
    }
  }
  ```
  >>> 
  ### 실행 결과
  0
  1
  2
  3
  4
  >>>

- `DialogResult result = DialogResult.YES;`
  ```cs
  using System;

  namespace Enum2 
  {
    class MainApp
    {
      enum DialogResult { YES, NO, CANCEL, CONFIRM, OK }

      static void Main(string[] args)
      {
        DialogResult result = DialogResult.YES;

        Console.WriteLine(result == DialogResult.YES);
        Console.WriteLine(result == DialogResult.NO);
        Console.WriteLine(result == DialogResult.CANCEL);
        Console.WriteLine(result == DialogResult.CONFIRM);
        Console.WriteLine(result == DialogResult.OK);
      }
    }
  }
  ```
  >>> 
  ### 실행 결과
  True
  False
  False
  False
  False
  >>>

- 열거형식에서 각 요소별 특별한 값을 직접 할당할 수 있다. 할당 안 하게 되면 컴파일러가 자동으로 값을 할당한다. 이전 요소로부터 1씩 더한 값이다.
```cs
using System;

namespace Enum3
{
  class MainApp
  {
    enum DialogResult { YES = 10, NO, CANCEL, CONFIRM = 50, OK }

    static void Main(string[] args)
    {
      Console.WriteLine((int)DialogResult.YES);
      Console.WriteLine((int)DialogResult.NO);
      Console.WriteLine((int)DialogResult.CANCEL);
      Console.WriteLine((int)DialogResult.CONFIRM);
      Console.WriteLine((int)DialogResult.OK);
    }
  }
}
```
>>>
### 실행 결과
10 
11
12
50
51
>>>

<br><br>

## 3.6 Nullable 형식

- 어떤 값도 아닌 비어있는 상태를 저장해야 할 때, Nullable 형식을 사용한다.
- Nullable 형식의 변수를 선언할 때는 형식 이름 뒤에 '?'만 붙여주면 된다.
- `데이터 형식 ? 변수 이름;`
- `int? a = null;` `float? b = null;` `double? c = null;`
- 이는 `int a`와는 다른 의미이다. `int?`와 달리 `int`는 비워둘 수 없는 데이터 형식이다.
- Nullable의 형식은 HasValue와 Value 속성을 지니고 있다. 이를 통해 변수가 있는지 없는지, 그 값이 무엇인지 나타낼 수 있다.
```cs
using System;

namespace Nullable
{
  class MainApp
  {
    static void Main(string[] args)
    {
      int? a = null;

      Console.WriteLine(a.HasValue);
      Console.WriteLine(a != null);

      a = 3;

      Console.WriteLine(a.HasValue);
      Console.WriteLine(a != null);
      Console.WriteLine(a.Value);
    }
  }
}
```
>>>
### 실행 결과
False
False
True
True
3
>>>

<br><br>

## 3.7 var : 데이터 형식을 알아서 파악하는 똑똑한 C# 컴파일러
- C#은 변수나 상수에 대해 깐깐하게 형식 검사를 하는 강력한 형식의 언어(Strong Typed Language)이다.
- 강력한 형식의 검사는 프로그래머의 실수를 줄여주는 장점이 있다.
- 하지만 귀찮게 모든 형식을 알아야 하고 지정해주는 단점이 존재한다.
- 이러한 문제를 var 키워드를 통해 해결한다.
- 단, var 키워드를 이용해 변수를 선언할 때는 반드시 선언과 동시에 초기화를 해줘야 한다.
- `var a = 3; var b = "Hello";`
- var는 암시적 형식으로써 지역 변수로만 사용할 수 있다.(코드 블록 내에서만 존재 가능)
- object는 힙에 메모리를 저장하면, var는 스택에 메모리를 저장한다.

```cs
using System;

namespace UsingVar
{
  class MainApp
  {
    static void Main(string[] args)
    {
      var a = 20;
      Console.WriteLine("Type: {0}, Value: {1}", a.GetType(), a);

      var b = 3.1414213;
      Console.WriteLine("Type: {0}, Value: {1}", b.GetType(), b);

      var c = "Hello, World!";
      Console.WriteLine("Type: {0}, Value: {1}", c.GetType(), c);

      var d = new int[] { 10, 20, 30 };
      Console.WriteLine("Type: {0}, Value: ", d.GetType());
      foreach (var e in d)
          Console.WriteLine("{0} ",e);

      Console.WriteLine();
    }
  }
}
```
>>> 
### 실행 결과
Type: System.Int32, Value: 20
Type: System.Double, Value: 3.1414213
Type: System.String, Value: Hello, World!
Type: System.Int32[], Value: 10 20 30
>>>

<br><br>

## 3.8 공용 형식 시스템

- C#의 모든 데이터 형식 체계는 공용 형식 시스템(Common Type System)이라는 .NET의 형식 체계 표준을 그대로 따르고 있다.
- 공용 형식 시스템은 "모두가 함께 사용하는 데이터 형식 체계"라는 의미이다.
- "모두"는 C#을 비롯한 .NET을 지원하는 모든 언어들끼리 서로 호환성을 갖도록 하기 위한 범위이다.
- "C#의 데이터 형식 체계가 CTS 표준을 따르고 있다."
- 다음은 각 요소별 형식의 차이를 몇가지 보이는 표이다.
[책 : 92쪽](https://books.google.co.kr/books?id=VQoUEAAAQBAJ&pg=PA91&lpg=PA91&dq=%EA%B3%B5%EC%9A%A9+%ED%98%95%EC%8B%9D+%EC%8B%9C%EC%8A%A4%ED%85%9C+%ED%91%9C&source=bl&ots=8Inxtut0t1&sig=ACfU3U3Xazi8yY7igzVR4V43cx3AtNq1xw&hl=ko&sa=X&ved=2ahUKEwi7zr-xyM_5AhVlGaYKHWvaBEkQ6AF6BAgoEAM#v=onepage&q=%EA%B3%B5%EC%9A%A9%20%ED%98%95%EC%8B%9D%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%ED%91%9C&f=false)

| 클래스 이름         | C# 형식  | C++ 형식          | 비주얼 베이직 형식 |
|----------------|--------|-----------------|------------|
| System.Byte    | byte   | unsigned char   | Bute       |
| System.Sbyte   | sbyte  | char            | Sbyte      |
| System.Int16   | short  | short           | Short      |
| System.UInt64  | ulong  | unsigned__int64 | Ulong      |
| System.Single  | float  | float           | Single     |
| System.Boolean | bool   | bool            | Boolean    |
| System.Object  | object | Object*         | Object     |
| System.String  | string | String*         | String     |

```cs
using System;

namespace CTS
{
  class MainApp
  {
    static void Main(string[] args)
    {
      System.Int32 a = 123;
      int b = 456;

      Console.WriteLine("a type: {0}, value: {1}", a.GetType().ToString(), a);
      Console.WriteLine("b type: {0}, value: {1}", b.GetType().ToString(), b);

      System.String c = "abc";
      string d = "def";

      Console.WriteLine("c type: {0}, value: {1}", c.GetType().ToString(), c);
      Console.WriteLine("d type: {0}, value: {1}", d.GetType().ToString(), d);
    }
  }
}
```
>>> 
### 실행 결과
a type: System.Int32, value: 123
b type: System.Int32, value: 456
c type: System.String, value: abc
d type: System.String, value: def
>>>

<br><br>

## 3.9 문자열 다루기

- string 형식은 단순히 문다열을 담는 것 뿐만 아니라, 문자열을 가공하기 위한 다양한 기능도 제공된다.

<br>

### 3.9.1 문자열 안에서 찾기

- string 형식이 제공하는 탐색 메소드의 종류와 역할을 다음과 같다.
  - IndexOf() : 현재 문자열 내에서 찾고자 하는 지정된 문자 또는 문자열의 위치를 찾는다. 위치하는 문자 순번을 반환한다.
  - LastIndexOf() : IndexOf()를 뒤에서부터 찾는다. 위치하는 문자 순번을 반환한다.
  - StartWith() : 현재 문자열이 지정된 문자열로 시작하는지 평가한다. True, False를 반환한다.
  - EndsWith() : 현재 문자열이 지정된 문자열로 끝나는지를 평가한다. (True, False)
  - Contains() : 현재 문자열이 지정된 문자열을 포함하는지 평가한다. (True, False)
  - Replace() : 현재 문자열에서 지정된 문자열이 다른 지정된 문자열로 모두 바뀐 새 문자열을 반환한다. `문자열.Replace("A", "B");` : A를 B로 바꾼다.
  ```cs
  using static System.Console;

  namespace StringSearch
  {
    class MainApp
    {
      static void Main(string[] args)
      {
        string greeting = "Good Morning";

        WriteLine(greeting);
        WriteLine();

        // IndexOf
        WriteLine("IndexOf 'Good' : {0}", greeting.IndexOf("Good"));
        WriteLine("IndexOf 'o' : {0}", greeting.IndexOf('o'));

        // LastIndexOf()
        WriteLine("LastIndexOf 'Good' : {0}", greeting.LastIndexOf("Good"));
        WriteLine("LastIndexOf 'o' : {0}", greeting.LastIndexOf('o'));

        // StartsWith()
        WriteLine("StartsWith 'Good' : {0}", greeting.StartsWith("Good"));
        WriteLine("StartsWith 'Morning' : {0}", greeting.StartsWith("Morning"));

        // EndsWith()
        WriteLine("EndsWith 'Good' : {0}", greeting.EndsWith("Good"));
        WriteLine("EndsWith 'Morning' : {0}", greeting.EndsWith("Morning"));

        // Contains()
        WriteLine("Contains 'Evening' : {0}", greeting.Contains("Evening"));
        WriteLine("Contains 'Morning' : {0}", greeting.Contains("Morning"));

        // Replace()
        WriteLine("Replaced 'Morning' with 'Evening': {0}", greeting.Replace("Morning", "Evening"));
      }
    }
  }
  ```
  >>>
  ### 실행 결과
  >StringSearch.exe
  Good Morning [Enter]

  IndexOf 'Good' : 0
  IndexOf 'o' : 1
  LastIndexOf 'Good' : 0
  LastIndexOf 'o' : 6
  StartsWith 'Good' : True
  StartsWith 'Morning' : False
  EndsWith 'Good' : False
  EndsWith 'Morning' : True
  Contains 'Evening' : False
  Contains 'Morning' : True
  Replaced 'Morning' with 'Evening': Good Evening
  >>>

<br>

### 3.9.2 문자열 변형하기

- string 형식의 문자열 변형 기능 관련 메소드를 제공한다.
  - ToLower() : 현재 문자열의 모든 대문자를 소문자로 바꾼 새 문자열을 반환합니다. 
  - ToUpper() : 현재 문자열의 모든 소문자를 대문자로 바꾼 새 문자열을 반환합니다.
  - Insert() : 현재 문자열의 지정된 위치에 지정된 문자열이 삽입된 새 문자열을 반환합니다.
  - Remove() :  현재 문자열의 지정된 위치로부터 지정된 수만큼의 문자가 삭제된 새 문자열을 반환합니다.
  - Trim() : 현재 문자열의 앞/뒤에 있는 공백을 삭제한 새 문자열을 반환합니다.
  - TrimStart() : 현재 문자열의 앞에 있는 공백을 삭제한 새 문자열을 반환합니다.
  - TrimEnd() : 현재 문자열의 뒤에 있는 공백을 삭제한 새 문자열을 반환합니다.
  ```cs
  using static System.Console;

  namespace StringModify
  {
    class MainApp
    {
      static void Main(string[] args)
      {
        WriteLine("ToLower() : '{0}'", "ABC".ToLower());
        WriteLine("ToUpper() : '{0}'", "abc".ToUpper());

        WriteLine("Insert() : '{0}'", "Happy Friday!".InSert(5, " Sunny"));
        WriteLine("Remove() : '{0}'", "I Don't Love You.".Remove(2, 6));

        WriteLine("Trim() : '{0}'", " No Spaces ".Trim()); 
        WriteLine("TrimStart() : '{0}'", " No Spaces ".TrimStart()); 
        WriteLine("TrimEnd() : '{0}'", " No Spaces ".TrimEnd()); 
      }
    }
  }
  ```
  >>>
  ### 실행 결과
  ToLower() : 'abc'
  ToUpper() : 'ABC'
  Insert() : 'Happy Sunny Friday!'
  Remove() : 'I Love You.'
  Trim() : 'No Spaces'
  TrimStart() : 'No Spaces '
  TrimEnd() : ' No Spaces'
  >>>

  <br>

### 3.9.3 문자열 분할하기

- "MSFT, GOOG, AMZN, AAPL, RHT"와 같은 문자열이 있을 때, 콤마(,)로 구분된 부분을 제외한 내용을 단번에 배열로 만들 수 있다.
  - Split() : 지정된 문자를 기준으로 현재 문자열을 분리한 다음, 분리한 문자열의 배열을 반환한다. `string[] arr = 문자열.Split(new String[] {" "}, StringSplitOptions.None);`
  - SubString() : 현재 문자열의 지정된 위치로부터 지정된 수만큼 문자로 이루어진 새 문자열을 반환한다. `문자열.Substring(a, b);` 문자열의 a번째부터 b번째를 반환한다.
  ```cs
  using System;
  using static System.Console;

  namespace StringSlice
  {
    class MainApp
    {
      static void Main(string[] args)
      {
        string greeting = "Good morning.";

        WriteLine(greeting.Substring(0, 5));  // "Good"
        WriteLine(greeting.Substring(5));  // "morning"
        WriteLine();

        string[] arr = greeting.Split(new string[] {" "}, StringSplitOptions.None);
        WriteLine("Word Count : {0}", arr.Length);

        foreach (string element in arr)
            WriteLine("{0}", element);
      }
    }
  }
  ```
  >>> 
  ### 실행 결과
  >StringSlice.exe
  Good
  morning.

  Word Count : 2
  Good
  morning.
  >>>

  <br>

### 3.9.4 문자열 서식 맞추기

- 여기에서 서식은 글꼴, 색상, 모양새와 달리, 문자열이 일정한 틀과 모양을 갖추는 것을 의미한다.

#### Format() 메소드
- 문자열 틀에 입력하는 {0}, {1} -- 를 "서식항목(Format Item)"이라 한다.
  - `{첨자, 맞춤 : 서식 문자열}`
  - 왼쪽/오른쪽 맞춤
    `string.Format("{0, -10}DEF","ABC")`; // "ABC.......DEF" D가 10번째 시작
    `string.Format`
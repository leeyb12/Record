// in 매개변수를 안전하게 사용하려면

// 값 매개변수를 취하는 public 메서드
public static double PublicMethod(
    LargeStruct first,
    LargeStruct second)

{
    double firstResult = PrivateMethod(in first);
    double secondResult = PrivateMethod(in second);
    return firstResult + secondResult;
}

// in 매개변수를 취하는 private 메서드
private static double PrivateMethod(
    in LargeStruct input)

{
    double scale = GetScale(in input);
    return (input.X + input.Y + input.Z) * scale;
}

private static double GetScale(in LargeStruct input) =>   // in 매개변수를 취하는 또 다른 메서드
    input.Weight * input.Score;
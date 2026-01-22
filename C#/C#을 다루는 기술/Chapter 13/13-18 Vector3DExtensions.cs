//  ref와 in을 사용하는 확장 메서드

public static double Magnitude(this is Vector3D vec) =>
    Math.Sqrt(vec.X * vec.X + vec.Y * vec.Y + vec.Z * vec.Z);

public static void OffsetBy(this ref Vector3D orig, in Vector3D off) =>
    orig = new Vector3D(orig.X + off.X, orig.Y + off.Y, orig.Z + off.Z);
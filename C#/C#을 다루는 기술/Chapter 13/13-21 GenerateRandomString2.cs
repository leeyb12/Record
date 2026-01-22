// stackalloc과 포인터를 이용해서 랜덤 문자열 생성

unsafe static string Generate(string alphabet, Random random, int length)
{
    char* chars = stackalloc char[length];
    for (int i = 0; i < length; i++)
    {
        chars[i] = alphabet[random.Next(alphabet.Length)];
    }
    return new string(chars);
}
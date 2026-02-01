def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word

        for sound in sounds:
            if sound in temp:
                # 각 발음은 최대 한 번만 사용
                temp = temp.replace(sound, " ")
        
        # 공백 제거 후 아무것도 안 남으면 발음 가능
        if temp.strip() == "":
            count += 1
    
    return count
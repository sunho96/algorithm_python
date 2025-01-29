def find_long_word(s):
    char_map = {} # 문자와 그 마지막 위치를 저장하는 해시 테이블
    start = 0 # 현재 부분 문자열의 시작 위치
    max_length = 0  # 가장 긴 부분 문자열의 길이

    for end in range(len(s)):  # end는 문자열을 순회하면서 탐색하는 인덱스
        if s[end] in char_map and char_map[s[end]] >= start:
            # 중복된 문자가 발생했으면, start를 갱신하여 중복이 발생한 문자의 바로 다음 위치로 이동
            start = char_map[s[end]] + 1
        char_map[s[end]] = end  # 현재 문자의 위치를 갱신

        # 현재 윈도우의 길이를 계산하고, 최대 길이를 갱신
        max_length = max(max_length, end - start + 1)

    return max_length
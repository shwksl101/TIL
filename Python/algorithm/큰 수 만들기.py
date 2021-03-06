"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1이상 number의 자릿수 미만인 자연수입니다.
"""

# solution1(시간초과)
# 숫자를 1개 뺀다 -> 그 중에서 제일 큰 수만 가져간다.
# 숫자 하나를 더 뺀다 -> 그 중에서 제일 큰 수만 가져간다
# ...
# 숫자 k개를 뺀다 -> 그 중에서 제일 큰 수를 return한다.

# solution2
# stack에 첫번째 숫자를 넣는데 두번째 숫자 부터는 stack의 길이가 0보다 크고 num이 마지막 stack보다 크고 k >0이면
# k를 -1하고 stack에서 마지막 숫자를 pop하고 num을 append한다

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
Procedures
----------

이 문서에서는 각 함수의 일반적인 실행 절차를 서술한다. 또한 몇 가지 상수를 정의하고 있다.

## Constants

```python
PRINT_NEWLINE = -1
PRINT_RESET = -2

# 개인적으로 각 라인 마지막에 공백이 포함되지 않는 것을 선호하므로
# 공백 유무에 따른 두 가지 경우를 모두 고려하여 프로그램이 작성되어 있다.
END_WITH_SPACE = True

EASY_PRINT = True
```

## Functions
함수 내에서 값을 반환했다면 그 값을 함수 값으로 취급하며 더 이상의 실행을 진행지키지 않는다.

### evalTerm(a, x, e)
```
1. a 가 0 이라면 0 을 반환한다.
2. x 가 0 이라면 다음을 실행한다.
  1. e 가 0 이라면 a 를 반환한다.
  2. 0 을 반환한다.
3. x 가 1 이라면 a 를 반환한다.
4. v 에 a 을 할당한다.
5. 다음을 e 번 반복한다.
  1. v 에 v * x 을 할당한다.
6. v 을 반환한다.
```

### print_rows(n)
```
1. j 에 compueted_needed_rows(n) 반환 값를 할당한다.
2. printer_state 에 PRINT_RESET 을 할당한다.
3. i 에 1 을 할당한다.
4. v 에 1 을 할당한다.
5. 다음을 j - 1 번 반복한다.
  1. 다음을 v 번 반복한다.
    1. printer_state 에 printer(printer_state, i) 반환 값을 할당한다.
    2. i 를 1 증가시킨다.
  2. printer_state 에 printer(printer_state, PRINT_NEWLINE) 반환 값을 할당한다.
  3. v 에 2*v 를 할당한다.
6. i < n + 1 을 만족한다면 다음을 반복한다.
  1. printer_state 에 printer(printe하r_state, i) 반환 값을 할당한다.
  2. i 를 1 증가시킨다.
7. printer_state 에 printer(printer_state, PRINT_NEWLINE) 반환 값을 할당한다.
8. 종료
```

### compute_needed_rows(n)
```
1. j = 1
2. v = 2
3. n 을 1 증가시킨다.
4. v < n 을 만족한다면한 다음을 반복한다.
  1. v 에 v * 2 을 할당한다.
  2. j 를 1 증가시킨다.
5. j 를 반환한다.
```

### printer_without_space(old_state, new_state)
```
1. new_state == PRINT_NEWLINE 이라면 다음을 실행한다.
  1. old_state 를 출력한다.
  2. 한 줄을 출력한다.
  3. PRINT_RESET 을 반환한다.
2. old_state >= 0 이라면 다음을 실행한다.
  1. old_state 를 출력한다.
  2. 공백 한 칸을 출력한다.
  3. 한 줄을 출력한다.
3. new_state 을 반환한다.
```

### printer_with_space(old_state, new_state)
```
1. new_state >= 0 이라면 다음을 실행한다.
  1. new_state 를 출력한다.
  2. 공백 한 칸을 출력한다.
  3. 한 줄을 출력한다.
2. new_state 가 PRINT_NEWLINE 이라면 한 줄을 출력한다.
3. PRINT_RESET 을 반환한다.
```

### printer(x, y)
```
1. END_WITH_SPACE 가 True 라면 printer_with_space(x, y) 의 반환 값을 반환한다.
2. printer_without_space(x, y) 의 반환 값을 반환한다.
```


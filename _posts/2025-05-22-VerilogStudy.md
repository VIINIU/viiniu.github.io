---
layout: post
title:  "[Verilog] Verilog Basics"
date:   2025-05-22 10:00:00 +0900
image: 
  path: /images/blog_logo_1600x600.jpg
  thumbnail: /images/blog_logo_1600x600.jpg
categories: LINUX Certification
author: VINI
tag: Verilog
--- 


## Verilog HDL

---
- HDL description : 내가 작성한 코드
    <img src="/images/Verilog/image.png" width="49%">

- library : 각 게이트에 대한 라이브러리
- Constrain : 해당 모듈이 silicon에서 차지할 Area, timing, power, testability

## Module

---

- Systems & Circuit/logic Designs are represented as **module** unit in Verilog HDL
    - Module 은 C에서 함수 정도의 위치
    - 각 Module끼리는 Signal로 연결 됨
- **Structure of Module**
    
    <img src="/images/Verilog/image 1.png" width="49%">
    
- **Name of a Module**
    - Start with letter or underscre
    - `$`, `_` , `letter`, `digit` can be used
- comment : `//(한줄)` , `/* (블럭) */`
- Description : 협업 시 필수, 개인 작업시 있으면 좋음 (개발이나 하고 보십쇼)
- Module interface
    
    <img src="/images/Verilog/image 2.png" width="49%">
    
    - 두꺼운 화살표 = multibit, 얇은거 = single (당연)
    - out인지 in인지 direction 지정
    - multi인 경우 [3:0]과 같이 MSB, LSB순으로 지정
    - signal type(`wire` or `reg`)도 지정해줘야 하는데 사실 위에 모듈 명 이후의 괄호에서 모두 해결해도 괜찮음
    - 다양한 port sig type 지정 방법
        
    <img src="/images/Verilog/image 3.png" width="49%">
        

- **Different Type of Module BODY**
    - 어떤 추상화 레벨로 게이트를 묘사하느냐에 따라 다양한 레벨의 코딩 방법이 존재함
    - 4 to 1 Multiflexer를 예시로 살펴보면
        - Structural Style (제일 LOW)
            - physical circuit을 그냥 스트레잇하게 말로 표현
                
                <img src="/images/Verilog/image 4.png" width="49%">
                
        - Dataflow Style
            - input signal의 transformtation으로 output을 묘사
                
                <img src="/images/Verilog/image 5.png" width="49%">
                
        - Behavioral Style
            - 예상되는 행동을 묘사
            - 제일 natural language에 가까워 추상화 정도가 가장 높음
                
                <img src="/images/Verilog/image 6.png" width="49%">
                

## Signals

---

- Available Values of Signals
    - Verilog 시그널은 4개뿐
        - 0 : logic zero or false condition
        - 1 : logic one or True Condition
        - X : interpreted ‘0’ or ‘1’ or ‘Z’ or in the state of change
        - Z : HIGH IMPEDANCE 물리적 cut off
- Classes of Signals
    Signal의 클래스는 여러개가 있는데 모든걸 저장하는건 불가능이니 저장 필요 여부에 따라 시그널의 클래스를 나눔
    - Net
        - 그냥 소자간의 물리적 연결을 나타냄
    - Register(Variable)
        - C에서 변수와 동일.
        - 새거 할당하기 전까지는 유지임
- NET signal type
    
    <img src="/images/Verilog/image 7.png" width="49%">
    
    - wire : single driver nets
    - tri : High impedance가 가능함. tri는 nets with multiple sources
    - wand, wor = 논리합성 불가 → 시뮬레이션용
- Scalar Signals And Vectors
    - Scalar
        - single wire connection → single logical value at one time
        (e.g. `clock`)
    - Vectors (=Buses)
        - multiple-line signal → complex values and codes can be sent and recieved ( e.g. `32-bit microprocessor`)
- Vector Specification
    - Vector가 기본형이고, 
    Scalar가 special case of vector (MSB=LSB인 vector)
    - [-5 : 0] 도 문법적으로는 허용~
- External Signal
    - module 내부에서 정의된 signal들은 전부 internal signal
    - External Signal은 module ports로 정의해야함
    - module port
        - input
            - environment에서 모듈이 data를 읽어옴
            system 내부의 포트에 쓰는 건 불가능
        - output
            - data가 모듈에서 environment로 보내짐
            system에서 읽는 건 불가능
        - inout
            - 둘 다 됨. bi-directional

### A Structural View of System

---

**Module Instantiation**

- module provides a template
- module template에서 object를 만드는 것 : instantiation
각각의 object = instance
- C언어에서 함수처럼 한 모듈에서 다른 모듈을 호출 가능
    
    <img src="/images/Verilog/image 8.png" width="49%">
    
- 호출(invoke)시 verilog가 알아서 instance를 만듦
이름은 직접 정해줘야 함 (왜냠 여러개 불러 올 수도 있자너~)
- **Port Connecting Rules**
    
    **module instantiation flexibility**를 위해서 outside와 포트 연결 시, Rule이 필요 
    모든 포트는 internal part 와 external part가 존재
    
    <img src="/images/Verilog/image 9.png" width="49%">
    
    - **input port**
        
        **internal : `net`
        external : `net or reg`**
        
    - **inout** **port** : must be **`net** (**both**)`
    - **output** port
        
        **internal : `reg or net`
        external : `net`**
        
    - 받는 쪽 = WIRE라고 생각하면 좋음!!
- port maping
    - ordered port list
        - 따로 정의된 모듈을 새로 불러와서 INSTANCE로 만든 후 로컬포트와 인스턴스 포트를 맵핑하는 방법
        - 원래 모듈의 포트정의 순서대로 로컬 포트를 명시하면 됨~ (C 함수와 유사)
    - Connecting Ports by Name
        - 로컬 포트명을 인스턴스 포트명 옆에 괄호를 열고 표시
        
        <img src="/images/Verilog/image 10.png" width="49%">
        
    - Unconnected Ports
        - 안 쓰고 싶은 포트가 있는 경우 인스턴스 불러올 때 포트를 안 쓰면 됨!!
        name, order 모두 동일!!

베릴로그 기본 제공 모듈 = 인스턴스명 안 써도 ㄱㅊ
직접 만든 모듈 = 인스턴스명 명시 꼭!!

### Specification with Signal Transformation

---

**Posible Operand Types for Expression**

- Constant
    - literal : 23, 0.1, 2’b01
    - Named Constant : ‘define A 10, parameter A=10;
        - parameter = 로컬, define = 글로벌
- Signal
- Function call : f1(s)

<aside>
📝

**Integer Constant 표기 방법**

e.g)  2’b01

Verilog의 숫자 표현 방식 2 = 비트수, b = binary, 01 = binary 숫자

| Value | Unsized Decimal Integer |
| --- | --- |
| size ‘ base value | sized integer in a specific radix(base(진수요.. 진수)) |

| Base | Symbol | Legal Values |
| --- | --- | --- |
| unsigned binary | ‘b | 0,1,x(X), z(Z), ?, _ |
| unsigned octal | ‘o | 0-7, x(X), z(Z), ?, _ |
| unsigned decimal | ‘d | 0-9,_ |
| unsigned hexadecimal | ‘h | 0-f(F),  x(X), z(Z), ?, _ |
- singed의 경우 ‘sb, ‘so, ‘sd, ‘sh 이외 동일
- **’b와 ‘B는 동일**
- ? = Z의 다른 표현 방법
- underscore는 무시됨. ONLY 인간의 가독성 때문에 씀(첨에는 못온단다)
- 사이즈를 넘어가는 수가 담기면 상위비트 짤림(당연…)
</aside>

- Bit-Select and Part-Select
    - `reg [7:0] DataBus;` 라고 시그널이 선언되었을 때,
        
        **`DataBus [3];`** 혹은 **`DateBus[5:2];`** 와 같은 방식으로 선택할 수 있음
        
- Operator
    - Relational Operators
        - `<` , `>` , `<=` , `>=` 등을 이용할 수 있으나, X 혹은 Z가 포함된 경우 모두 알수없음(X)가 됨
        - `===` ,`!==`  비트 단위로 비교함 → 따라서 `0xx0===0xx0` 은 `1`
        - `==` ,`!=`  값을 비교 → 따라서 X나 Z가 있는 경우 X
    - Bitwise Operators
        
        <img src="/images/Verilog/image 11.png" width="49%">
        <img src="/images/Verilog/image 12.png" width="49%">
        <img src="/images/Verilog/image 13.png" width="49%">
        
    - Shift Operators
        - `<<` , `>>`
            - e.ㅎ. regA << 3 을 하면 regA의 비트들이 왼쪽으로 3칸 이동 후 빈곳은 0으로 채워짐
            - `>>>` 의 경우 왼쪽으로 옮기고 0으로 채우되, sign bit는 유지
- Continous Assignment
    - 논리합성 안 됨
    - assign #3 ChipOut = Switch;
        - #3 ⇒ delay 3
        - ChipOut ⇒ Target으로 net만 가능
        - 우변은 암끼나 가능
- Conditional Assignment
    - 논리합성 가능
        
        <img src="/images/Verilog/image 14.png" width="49%">
        
- Delay
    - #t 와 같은 방식으로 사용
    - 실제 회로에서 딜레이를 원한다면 회로를 합성해야 함
        
        → 고로 온리 시뮬용
        
    - 1로 바뀌어서 어사인 하려다가 딜레이 동안 우변값이 바뀌면 어사인 안함요


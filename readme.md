<html>

<head>
    <title>아티팩트2</title>
    <style type="text/css">
        table {
            border: outset 2px black;
            border-collapse: collapse;
        }

        th {
            border-bottom: double 2px black;
        }

        td {
            border-bottom: solid 1px black;
        }

        .first_col {
            border-right: double 2px black;
        }

        .div_frame {
            border-style: solid;
            border-width: 1px;
        }
    </style>
</head>

<body>
    <h1 style="text-align: center;">
        2단계 - 구체화하기</h1>


    <h2>
        작업 1 : 아티팩트 1 보완하기
    </h2>
    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 계정의 생성, 수정, 삭제하기
            <span style="font-weight: bold;">목표 :</span> 손님이 계정을 생성, 수정, 삭제하는 것이다.
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 손님이 접수처에 있다.
            2. 손님이 계정을 생성/수정/삭제 하고자 한다.
            <span style="font-weight: bold;">액터 :</span>
            1. 손님(principal): 손님이 유스케이스를 시작한다.
            2. 직원(secondaire)
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 손님이 계정의 생성을 요청한다.
            2. 손님이 회원 또는 전문강사의 계정을 요청한다.
            3. 손님이 필요한 개인정보를 제공한다.
            4. 직원이 계정을 성공적으로 생성하고나서 손님에게 고유번호를 제공한다.
            <span style="font-weight: bold;">Scénarios alternatifs :</span>
            1a. 손님이 계정의 수정 또는 삭제를 요청한다.
            1a.1. 직원은 유스케이스:사용자 검증하기를 수행한다.
            1a.2. 사용자의 정보가 표시된다.
            1a.3. 손님이 그 계정을 없애기를 원한다.
            1a.3. 계정이 성공적으로 삭제된다.

            1a.1a. 손님이 검증에 실패한다.
            1a.1a.1. 유스케이스 종료.

            1a.3a. 손님이 계정의 수정을 요청한다.
            1a.3a.1. 손님이 수정하고자 하는 계정의 정보를 제공한다.
            1a.3a.2. 정보가 성공적으로 수정된다.

            1a.3a.1a. 변경하고자 하는 정보가 올바르지 않다.
            1a.3a.1a.1. :  1a.3a.1. 절차로 간다

            4a. 직원 혹은 손님이 계정 생성을 최종적으로 확인하지 않는다.
            4a.1. 유스케이스 종료.
            <span style="font-weight: bold;">사후조건 :</span> 
        직원이 계정 작업을 성공적으로 처리한다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">Use-case :</span> 서비스 생성/수정/삭제 하기
            <span style="font-weight: bold;">목표 :</span> 전문강사의 서비스를 생성/수정/삭제할 수 있도록 하는것
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 전문강사가 접수처에 있다.
            2. 전문강사가 요청사항을 제시하고자 한다.
            <span style="font-weight: bold;">역할 :</span>
            1. 전문강사 (주): 전문강사가 이 유즈케이스를 시작한다.
            2. 직원(부)
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 전문강사가 서비스의 생성/수정/삭제을 요구한다.
            2. 직원은 '사용자 검증하기' 유즈케이스를 시작시킨다.
            3. 전문강사가 등록한 서비스가 존재한다.
            4. 직원은 서비스를 보여준다.
            5. 전문강사는 원하는 서비스를 선택한다.
            6. 전문강사는 그 서비스를 수정해줄 것을 요청한다.
            7. 전문강사 수정할 정보를 제공한다.
            8. 직원이 서비스 정보를 성공적으로 수정한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            2a. 전문강사 정보가 올바르지 않다.
            2a.1. 프로세스 끝.

            3a. 전문강사는 현재 서비스를 등록한 것이 없다.
            3a.1. 프로세스 끝.
 
            7a. 제공한 정보가 올바르지 않다.
            7a.1. 절차 6으로 간다.

            6a. 전문강사 서비스를 삭제하기를 요청한다.
            6a.1. 직원이 서비스를 성공적으로 삭제한다.

            <span style="font-weight: bold;">사후조건 :</span> 
        직원이 해당 작업을 처리한다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 사용자 검증하기
            <span style="font-weight: bold;">목표 :</span> 사용자가 센터에 들어가는 것을 허용하는 것
            <span style="font-weight: bold;">사전조건 :</span> 
            접수처에 있는 사용자의 계정이 존재한다.
            <span style="font-weight: bold;">역할 :</span>
            1. 사용자(주) :  사용자가 해당 use-case를 시작한다.
            2. 직원 (부) 
            <span style="font-weight: bold;">주 시나리오 :</span>
            1a. 사용자가 직원에게 자신의 회원 고유번호를 제공한다.
            2a. 직원이 회원 번호에 대한 검증을 성공적으로 수행한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1b. 사용자가 직원에게 자신의 강사 고유번호를 제공한다.
            1b.1a 직원이 강사 번호에 대한 검증을 성공적으로 수행한다.
 
            1b.1b 강사가 정지된 강사 번호를 제공한다.
            1b.1b.1 사용자는 들어갈 수 없다.

            2b. 사용자가 정지된 회원 번호를 제공한다.
            2b.1 사용자는 들어갈 수 없다.
            <span style="font-weight: bold;">사후조건 :</span> 
        사용자가 '회원' 또는 '강사'로서 #GYM에 출입할 수 있게 된다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 세션 목록 조회하기
            <span style="font-weight: bold;">목표 :</span> 세션의 목록을 조회한다
            <span style="font-weight: bold;">사전조건 :</span> 
            직원은 세션들의 목록을 조회하길 원한다.
            <span style="font-weight: bold;">액터 :</span>
            1. 직원(주) :  직원이 해당 유스케이스를 시작한다.
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 직원이 세션들의 목록을 보고 싶어한다.
            2. 직원이 세션의 목록을 성공적으로 조회한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1a. 현재 아무 세션도 없다.
            2a. 직원에게 목록이 비어있음을 표시한다.
          
            <span style="font-weight: bold;">사후조건 :</span> 
        직원들은 세션들의 목록을 본다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 센터에 들어가기
            <span style="font-weight: bold;">목표 :</span> 손님이 #GYM 에 들어가게 한다.
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 손님이 접수처에 있다.
            2. 손님이 센터에 출입하고자 한다.
            <span style="font-weight: bold;">액터 :</span>
            1. 손님(principal): 손님이 유스케이스를 시작한다.
            2. 직원(secondaire)
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 손님이 접수처에 있다.
            2. 직원이 '유스케이스: 사용자 검증하기'를 시작한다.
            3. 손님이  #GYM의 서비스를 이용한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            3a. 손님의 검증이 실패한다.
            3a.1. 손님은 #GYM의 서비스를 이용할 수 없다.
            <span style="font-weight: bold;">사후조건 :</span> 
        손님이 #GYM의 서비스를 이용한다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 등록하기
            <span style="font-weight: bold;">목표 :</span> #GYM의 회원이 강의 또는 세션에 등록하게 한다.
            <span style="font-weight: bold;">사전조건 :</span> 
             1. 등록절차는 접수처에서 진행된다.
             2. 회원의 번호가 올바른 번호이다.
            <span style="font-weight: bold;">액터 :</span>
             1. 회원 (주) : 회원이 유스케이스를 시작한다.
             2. 직원 (부) : 직원은 회원 번호를 검증하고 회원을 세션에 등록시킨다.    
            <span style="font-weight: bold;">주 시나리오 :</span>
             1. 회원은 직원에게 자신을 세션에 등록시킬 것을 요청한다.
             2. 직원은 회원의 번호를 검증한다.
             3. 직원이 '유스케이스:세션 조회하기'를 시작한다.
             4. 회원이 원하는 세션을 선택한다.
             5. 직원이 회원과 함께 세션 등록 여부를 최종확인한다.
             6. 소프트웨어는 이 내역을 디스크에 기록한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            2a. 직원이 회원의 번호를 검증하는 데 실패한다.
            2a.1 프로세스 종료

            4a. 회원이 실수로 원치 않는 세션을 선택한다.
            4a.1  절차 4번으로.
            
            5a. 회원이 세션 등록을 취소하길 원한다.
            5a.1 프로세스 종료

            6a. 파일 쓰기에 실패한다.
            6a.1 에러 메시지 출력 후 프로세스 종료


            <span style="font-weight: bold;">사후조건 :</span> 
            소프트웨어가 세션에 등록한 내역을 성공적으로 디스크에 저장한다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 세션 조회하기
            <span style="font-weight: bold;">목표 :</span> 직원이 손님에게 현재 이용가능한 세션 목록을 보여준다.
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 접수처에서 조회가 이루어진다.
            <span style="font-weight: bold;">액터 :</span>
            1. 회원 (주) :  회원이 유스케이스를 시작한다.
            2. 직원 (부) : 직원은 날짜를 입력하여 그 날짜에 이용가능한 세션 정보를 제공한다.
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 회원은 직원에게 현재 이용가능한 서비스의 세션에 대한 정보를 요구한다.
            2. 직원이 시스템에 날짜를 입력한다.
            3. 시스템이 직원에게 해당 날짜에 이용가능한 모든 서비스의 세션들을 보여준다.
            4. 직원이 그에 대한 정보를 회원에게 제공한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1a.1 날짜가 잘못되었으면 시스템이 에러를 생성하고 해당 유스케이스는 종료된다. 
            <span style="font-weight: bold;">사후조건 :</span> 
        시스템이 입력한 날짜의 세션들을 출력하고 직원이 세션 정보를 회원에게 제공한다.</pre>
    </div>

    <br />


    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 등록 현황 조회하기
            <span style="font-weight: bold;">But :</span> 전문강사에게 자신의 서비스 세션에 얼마나 회원이 등록했는지 보여준다.
            <span style="font-weight: bold;">Préconditions :</span> 
            1. 전문강사가 접수처로 간다.
            2. 전문강사는 적어도 하나의 서비스가 등록되어 있다.
            <span style="font-weight: bold;">액터 :</span>
            1. 전문강사(주)
            2. 직원(부)
            <span style="font-weight: bold;">주 시나리오 :</span>
        1. 전문강사는 직원에게 자신의 세션에 등록된 현황을 보고 싶다고 요청한다. 
        2. 전문강사는 해당 세션의 날짜와 시간에 대한 정보를 제공한다. 

        3. 직원은 다음의 정보를 입력한다:
           1) 세션의 날짜와 시간
           2) 전문강사의 번호

        4. 직원이 세션 정보에 접근한다.
        5. 전문강사에게 세션에 대한 정보가 전달된다.

            <span style="font-weight: bold;">대체 시나리오 :</span>
        2a) 전문강사가 알려준 날짜와 시간이 올바르지 않다
          2a.1) 절차 2로
            <span style="font-weight: bold;">사후조건 :</span> 
        전문강사가 그의 세션을 조회한다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 세션 참가하기
            <span style="font-weight: bold;">목표 :</span> 회원이 출석체크하고 세션에 참가할 수 있게됨 
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 유효한 회원번호를 가진 회원일것.
            2. 적어도 하나 이상의 당일 예정된 세션에 등록한 회원일 것.
            <span style="font-weight: bold;">액터 :</span>
            1. 전문강사(주)
            2. 직원(부)
            <span style="font-weight: bold;">주 시나리오 :</span>
        1. 회원이 직원에게 세션 번호를 알려준다.
          1.1) 직원이 시스템에 해당 세션을 검색한다.
        2. 직원이 해당 서비스에 성공적으로 접근한다.
        3. 직원이 회원번호를 입력하여 등록이 되어있는지 판단한다.
        4. 등록이 잘 되어있다.
        5. 회원이 세션에 참가한다.
        6 시스템은 다음을 디스크에 기록한다:
          6.1 현재 날짜와 시각
          6.2 전문강사의 번호
          6.3 회원번호
          6.4 서비스번호
          6.5 비고사항 (비어 있을 수도 있음)

            <span style="font-weight: bold;">대체 시나리오 :</span>
        2a 세션 번호가 올바르지 않다.
          2a.1  1번으로 돌아가기

        4a 등록이 안되어있다.
        4a.1 회원은 세션에 참가할 수 없다.
            <span style="font-weight: bold;">사후조건 :</span> 
        회원은 출석체크하고 세션에 참가하게 된다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 보고서 제작 및 전송.
            <span style="font-weight: bold;">목표 :</span> 관리자가 회계 보고서를 열람한다.
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 직원이 보고서를 보내고자 하거나 시간이 금요일 자정으로 절차가 자동 실행된다.
            <span style="font-weight: bold;">액터 :</span>
            1. 직원(주)이 유즈케이스를 시작한다.
			2. 시스템
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 그 주에 제공된 모든 서비스를 읽어온다.
            2. 해당 정보를 가진 보고서가 작성된다:
                     - 그 주에 돈을 지불해야되는 강사들의 강사번호.
                     - 전문강사 각자의 서비스 개수와 수강료.
                     - 그 주에 서비스를 제공한 강사의 수. 
                     - 서비스의 총 개수.
                     - 수강료의 총합.
            4. 보고서를 전송한다. 
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1a. 그 주에 제공된 서비스에 대한 정보를 읽어오는데 실패한다.
            1a.1 에러를 출력하고 프로세스를 끝낸다.
            <span style="font-weight: bold;">사후조건 :</span> 
        보고서가 작성되고 관리자의 시스템에 전송된다.</pre>
    </div>

    <br />

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 회계 절차 실행시키기
            <span style="font-weight: bold;">목표 :</span> RnB에 정보를 제공한다.
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 금요일 자정이다.
            <span style="font-weight: bold;">액터 :</span>
            1. 시스템
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 강사들의 정보를 불러온다.
            2. TEF 파일을 생성한다.
            3. TEF에 쓰기를 수행한다.
            4. RnB 시스템에 해당 TEF를 전송한다.
            5. 유스케이스:보고서 제작 및 전송 을 실행한다
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1a. 강사들의 정보를 불러오는데 실패한다.
            1a.1 에러메시지 출력 및 유스케이스 종료

            2a. TEF 파일 생성에 실패한다.
            2a.1. 에러메시지 출력 및 유스케이스 종료
            3a. TEF 파일 쓰기에 실패한다.
            3a.1.에러메시지 출력 및 유스케이스 종료
            <span style="font-weight: bold;">사후 조건 :</span> 
        TEF 파일이 RnB 에 전송되고 관리자에게 보고서가 전송됨</pre>
    </div>

    <div class=div_frame>
        <pre style="font-family: 'Open Sans', sans-serif;">
            <span style="font-weight: bold;">use-case :</span> 회원비 및 등록비 납부하기
            <span style="font-weight: bold;">목표 :</span> 회원에게서 회원비 또는 등록비를 받는 것
            <span style="font-weight: bold;">사전조건 :</span> 
            1. 손님이 접수처에 있다.
            2. 손님이 #GYM의 회원이 되거나 어떤 서비스에 등록하고 싶어한다.
            <span style="font-weight: bold;">액터 :</span>
            1. 손님(주 액터): 손님이 이 유스케이스를 시작한다.
            2. 직원(부 액터)
            <span style="font-weight: bold;">주 시나리오 :</span>
            1. 손님이 #GYM에 새로 가입하거나 회원을 갱신하기를 요청한다.
            2. 직원이 회원번호를 요구한다.
            3. 직원이 회원에게 금액을 납부하라고 한다.
            4. 손님이 카드를 제시한다.
			5. 손님이 모든 비용을 정산한다.
            <span style="font-weight: bold;">대체 시나리오 :</span>
            1a. 손님이 서비스에 등록하기를 원한다.
			1a.1 4번 절차로 간다.

	    2a. 번호가 올바르지 않다.
	    2a.1. 유스케이스 종료.

            4a. 지불 수단이 작동하지 않는다.
            4a.1. 유스케이스의 종료.


	    5a 회원이 정지 상태였으면 다시 활성화 된다.
	    5a.1. 유스케이스 종료.
            <span style="font-weight: bold;">사후조건 :</span> 
        회원이 성공적으로 회비와 등록비를 납부한다.</pre>
    </div>

    <h2>
        작업 2 : 클래스 다이어그램
    </h2>
    </br>
    <p>
        <a href="portfolio/artifact2/분석/DiagrammeClasses.vpp">Fichier .vpp 다이어그램</a> </br>
    <h3>이미지:</h3>
    <img src="portfolio/artifact2/분석/DiagrammeClasses.PNG" width=100% alt="DiagrammeClasses">
    </p>
    </br>
    </br>
    </br>
    <h2>
        작업 3 : 시퀀스 다이어그램
    </h2>
    </br>
    <p>
        <a href="portfolio/artifact2/설계/DiagrammeSequences.vpp">Fichier .vpp 다이어그램</a> </br>
    <h3>회원의 생성, 수정, 삭제하기:</h3>
    <img src="portfolio/artifact2/설계/Membre.PNG" width=100%
        alt="Diagramme de séquences ajouter/mettre à jour/supprimer un membre"></br></br>
    <h3>서비스 생성, 수정, 삭제하기:</h3>
    <img src="portfolio/artifact2/설계/Service.PNG" width=100%
        alt="Diagramme de séquences ajouter/mettre à jour/supprimer un service"></br></br>
    <h3>세션에 출석체크하기 :</h3>
    <img src="portfolio/artifact2/설계/ConfirmSeance.PNG" width=100%
        alt="Diagramme de séquences confirmer présence à une séance"></br></br>
    <h3>세션에 등록하기:</h3>
    <img src="portfolio/artifact2/설계/Inscription.PNG" width=100%
        alt="Diagramme de séquences inscription à une séance"></br></br>
    <h3>회계 절차 수행하기:</h3>
    <img src="portfolio/artifact2/설계/Comptable1.PNG" width=100%
        alt="Diagramme de séquences procédure comptable 1"></br></br>
    <img src="portfolio/artifact2/설계/Comptable2.PNG" width=100%
        alt="Diagramme de séquences procédure comptable 2"></br></br>
    </p>
    <h2>
        작업 4 : 프로토타입 작성
    </h2>
    </br>
    <p>
    <h3>Fichier executable .jar:</h3>
    <a href="portfolio/artifact2/Implementation/GYM.jar">Gym.jar</a> </br>
    </p>
    </br>
    </br>
    </br>


</body>

</html>
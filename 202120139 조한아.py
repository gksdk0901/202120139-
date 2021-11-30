import time

Zodiacs={'물병자리':'청색',
        '물고기자리':'빨강색',
        '양자리':' 청록색',
        '황소자리':'금색',
        '쌍둥이자리':'은색',
        '게자리': '분홍색',
        '사자자리':'검정색',
        '처녀자리':' 보라색',
        '천칭자리':' 하얀색',
        '전갈자리':' 파란색',
        '사수자리':' 초록색',
        '염소자리':' 노란색'};
myZodiac=input(str(list(Zodiacs.keys()))+"중 당신의 별자리는?")
print('<%s>행운의 색은 <%s>입니다.'%(myZodiac, Zodiacs[myZodiac]))

print()

Zodiacs={'물병자리':'헤어밴드',
        '물고기자리':'캡모자',
        '양자리':' 선글라스',
        '황소자리':'목걸이',
        '쌍둥이자리':'귀걸이',
        '게자리':' 양말',
        '사자자리':'안경',
        '처녀자리':' 손목시계',
        '천칭자리':' 에코백',
        '전갈자리':' 스카프',
        '사수자리':' 반지',
        '염소자리':' 팔찌'};
print('<%s>행운의 아이템은 <%s>입니다.'%(myZodiac, Zodiacs[myZodiac]))

print()
time.sleep(0.2)

print('행운의 색과 아이템에 어울리는 스타일을 추천해드릴까요?')
answer=input('선택(네, 아니요): ')

while True:
    if answer=='네'  :
        print()
        print('행운의 색과 아이템과 어울리는 추천 스타일을 보여드리겠습니다.')
        time.sleep(0.3)

        import random
        style=['크롭티+청바지',
       '흰색 반팔 셔츠+청바지',
       '맨투맨+테니스 스커트',
       '노란색 원피스+흰색 운동화',
       '반팔+니트조끼+반바지',
       '크롭나시+찢어진 청바지',
       '오프숄더+연청바지',
       '꽃무늬 셔츠+통넓은 검정색 바지',
       '셔츠원피스+니트조끼',
       '골지 원피스+시스루 가디건',
       '나시원피스+볼레로',
       '하늘색 나염 크롭티+청바지',
       '크롭 니트 나시+레이어드 니트 가디건+통넓은 바지',
       '흰티+청치마',
       '흰티+청바지']

        styles={'크롭티+청바지':'크림치즈마켓_모짜렐라 반팔 크롭티+크레디_데일리 봄 롱 데님 와일드',
        '흰색 반팔 셔츠+청바지':'슬로우베리_반팔셔츠+크레디_데일리 봄 롱 데님 와일드',
        '맨투맨+테니스 스커트':'가온_오버핏 맨투맨+바닐라밀크_켐버 테니스스커트',
        '노란색 원피스+흰색 운동화':'리얼코코_세루아 코튼 반팔 롱원피스+베베퀸즈_러블리 스니커즈',
        '반팔+니트조끼+반바지':'프렌치오브_기본 흰티+프렌치오브_스무디 유넥 파스텔 봄 니트조끼+러브어나더_롤업 청반바지',
        '크롭나시+찢어진 청바지':'커먼유니크_레이스 크롭+원더원더_와이드 찢청 팬츠',
        '오프숄더+연청바지':'비바소피_물결 오프숄더 골지 반팔+우너더원더_와이드 찢청 팬츠',
        '꽃무늬 셔츠+통넓은 검정색 바지':'케이엔조이_빅플라워 쉬폰 블라우스+미닛마켓_찰랑 롱 슬랙스 팬츠',
        '셔츠원피스+니트조끼':'케이엔조이_스트릿 스프라이트 셔츠+케이엔조이_니트조끼',
        '골지 원피스+시스루 가디건':'크림치즈마켓_쫀쫀 여름 골지 원피스+비바소피_시스루 물결 긴팔 가디건',
        '나시원피스+볼레로':'루루서울_페인팅 닷 원피스+니드어린_볼레로 니트 크롭 가디건',
        '하늘색 나염 크롭티+청바지':'정이샵_하늘 물나염 버튼 크롭티+크레디_데일리 봄 롱 데님 와일드',
        '크롭 니트 나시+레이어드 니트 가디건+통넓은 바지':'캣스트릿_아련에스닉 니트&가디건 세트+미닛마켓_찰랑 롱 슬랙스 팬츠',
        '흰티+청치마':'프렌치오브_기본 흰티+부기샵_탄탄 데님 스커트',
        '흰티+청바지':'프렌치오브_기본 흰티+원더원더_와이드 찢청 팬츠'}

        def same(i):
            time.sleep(0.3)
            print()
            i=style.pop()
            print(i)
            print()

        def yes(y):
            time.sleep(0.2)
            print()
            y=input(str(list(styles.keys()))+"중 원하시는 스타일을 골라주세요 : ")
            print()
            time.sleep(0.2)
            print('<%s>의 추천 상품은 <%s>입니다.'%(y, styles[y]))
            time.sleep(0.2)
            print()

        def myStar(s):
            random.shuffle(style)
            s=same(style)
            like=input('어떤가요?(좋아요,별로에요): ')

            while True:
                if like=='별로에요':
                    same(style)
                    like=input('어떤가요?(좋아요,별로에요): ')
                elif like=='좋아요':
                    time.sleep(0.1)
                    print()
                    myStyle=input("선택한 스타일을 한 번 더 작성해주세요~! : ")
                    print()
                    print('추천 상품의 관련 정보를 드릴게요~!')
                    print()
                    time.sleep(0.2)
                    print('<%s>의 추천 상품은 <%s>입니다.'%(myStyle, styles[myStyle]))
                    print()
                    answer=input('더 알고 싶은 추천 스타일의 상품 정보가 있나요??(네,아니요): ')

                    while True:
                        if answer=='네':
                            yes(style)
                            answer=input('더 알고 싶은 추천 상품 정보가 있나요??(네,아니요): ')
                        elif answer=='아니요':
                            print()
                            print('♡감사합니다♡')
                            break

                    break
                

        if myZodiac=='물병자리':
            myStar('물병자리')
            break

        elif myZodiac=='물고기자리':
            myStar('물고기자리')
            break

        elif myZodiac=='양자리':
            myStar('양자리')
            break

        elif myZodiac=='황소자리':
            myStar('황소자리')
            break

        elif myZodiac=='쌍둥이자리':
            myStar('쌍둥이자리')
            break

        elif myZodiac=='게자리':
            myStar('게자리')
            break

        elif myZodiac=='사자자리':
            myStar('사자자리')
            break

        elif myZodiac=='처녀자리':
            myStar('처녀자리')
            break

        elif myZodiac=='천칭자리':
            myStar('천칭자리')
            break

        elif myZodiac=='전갈자리':
            myStar('전갈자리')
            break

        elif myZodiac=='사수자리':
            myStar('사수자리')
            break

        else:
            myStar('염소자리')
            break

    elif answer=='아니요':
        print()
        print('♡행복한 하루 보내세요~!♡')
        break
        

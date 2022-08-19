 - 인증(Token 발급 및 갱신) 관련 API
> 
>   | HTTP | Path | Permission | Body | 목적 |
>   | --- | --- | --- | --- | --- |
>   |**GET** |/accounts/user| Access Token | None |유저정보|
>   |**POST** |/accounts/login | None | email, password | 로그인 |
>   |**POST** |/accounts/logout| None | Refresh Token | 로그아웃 |
>   |**POST** |/accounts/registration| None | email, password1, password2 | 회원가입 |
>   |**POST** |/accounts/token/verify| Access Token | Access Token |유효기간 확인|
>   |**POST** |/accounts/token/refresh| Access Token | Refresh Token |Access Token refresh|

---

 - 이미지 업로드 API
>   | HTTP | Path | Permission | Body | 목적 |
>   | --- | --- | --- | --- | --- |
>   |**GET** |/image | Access Token | email, image | 이미지 가져오기 |
>   |**POST** |/image | Access Token | FormData | 이미지 업로드 |

---
 - ML API
>   | HTTP | Path | Permission | Body | 목적 |
>   | --- | --- | --- | --- | --- |
>   |**GET** |/ML | None | None | yoloV5 |
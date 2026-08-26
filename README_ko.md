<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94!%20%F0%9F%91%8B&fontSize=70&fontAlignY=40&desc=Unity%20%EA%B2%8C%EC%9E%84%20%EA%B0%9C%EB%B0%9C%EC%9E%90%20%7C%20%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC%EC%99%80%20%ED%88%B4%EB%A7%81&descSize=20&descAlignY=60)

[![English](https://img.shields.io/badge/Language-English-blue?style=flat-square)](README.md)
[![한국어](https://img.shields.io/badge/Language-한국어-red?style=flat-square)](README_ko.md)
[![日本語](https://img.shields.io/badge/Language-日本語-orange?style=flat-square)](README_ja.md)

### 🚀 소개

Unity 게임 개발자입니다. 프레임워크와 에디터 툴링을 먼저 만들고, 그 위에서 돌아가는 게임을 출시합니다.

공개된 작업물은 대부분 Unity 6용 모듈식 패키지 세트인 **Mu3Library**에 모여 있고, 출시한 게임은 Steam에 있습니다.

</div>

---

## 🛠 기술 스택

<div align="center">

![Unity](https://img.shields.io/badge/Unity-000000?style=for-the-badge&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=for-the-badge&logo=csharp&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![HLSL](https://img.shields.io/badge/HLSL-DBBC04?style=for-the-badge&logo=shaderlab&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

![URP](https://img.shields.io/badge/URP-1a5fb4?style=flat-square)
![Addressables](https://img.shields.io/badge/Addressables-1a5fb4?style=flat-square)
![Localization](https://img.shields.io/badge/Localization-1a5fb4?style=flat-square)
![Input System](https://img.shields.io/badge/Input%20System-1a5fb4?style=flat-square)
![UniTask](https://img.shields.io/badge/UniTask-1a5fb4?style=flat-square)

</div>

---

## 📂 주요 프로젝트

### 🏗 [Mu3Library For Unity](https://github.com/doqltl179/Mu3Library_ForUnity)

<div align="left">

![Unity](https://img.shields.io/badge/Unity-6000.0%2B-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)
![HLSL](https://img.shields.io/badge/HLSL-DBBC04?style=flat-square)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

> **Unity 6용 모듈식 아키텍처 패키지 세트**
>
> 커스텀 DI 컨테이너와 MVP UI 패턴 위에 올린 세 개의 계층형 Unity 패키지입니다. 선택적 연동은 define 심볼로 분리되어 있어, UniTask·Addressables·Localization·Input System·Mobile Notifications를 설치하지 않은 프로젝트도 그대로 컴파일되고 그만큼의 비용도 들지 않습니다.

| 패키지 | 버전 | 의존 |
|---|---|---|
| `Mu3Library_Base` | 0.26.0 | — |
| `Mu3Library_URP` | 0.3.0 | Base |
| `Mu3Library_Game_WatermelonGame` | 0.6.0 | Base, URP |

**주요 기능:**
- 💉 **DI 컨테이너** — Singleton·Transient·Scoped 생명주기, Core 간 필드/프로퍼티 주입
- 🎨 **MVP UI** — View·Presenter·Model 분리, await 가능한 열기/닫기
- 🏗 **Core 모듈** — `IInitializable`·`IUpdatable`·`IDisposable` 기반의 결정적 실행 순서
- 🎵 **오디오** — BGM·SFX·환경음 채널, 믹서 그룹 라우팅, BGM 더킹, await 가능한 페이드, 볼륨 저장
- 🌐 **WebRequest** — GET·POST·PUT·PATCH·DELETE, 재시도 백오프, 요청 중 취소, 다운로드 진행률
- 🎮 **입력 & 알림** — 인터랙티브 리바인딩과 바인딩 오버라이드 저장, Android·iOS 모바일 알림 예약
- 🖼 **URP 화면 효과** — 흑백, 셰이크, 가우시안 블러, 뎁스 아웃라인과 카메라 스택 헬퍼
- 🍉 **Watermelon Game 패키지** — 11단계 2D 머지 보드, 설정 가능한 `BoardConfig`, 플레이 가능한 샘플 씬
- 🧰 **에디터 툴링** — DI 해석 검증기, 런타임 진단, Addressables·Localization 익스포터
- ✅ **EditMode 테스트** 및 영어·한국어·일본어 문서

---

### 🎮 The Echo Escape

<div align="left">

![Unity](https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)
![Steam](https://img.shields.io/badge/Steam-Released-blue?style=flat-square&logo=steam)

</div>

> **Steam에 출시한 공포 게임**
>
> 분위기 있는 스토리텔링과 사운드 디자인을 중심으로 만든 심리 공포 게임입니다. 소스 저장소는 비공개입니다.

**🔗 [Steam에서 플레이하기](https://store.steampowered.com/app/2875300/The_Echo_Escape/)**

<details>
<summary>📺 트레일러 보기</summary>

[![The Echo Escape Trailer](https://img.youtube.com/vi/rbei7quiAF4/0.jpg)](https://youtu.be/rbei7quiAF4)

</details>

---

### 🎵 [PostMV - ghost choir](https://github.com/doqltl179/Post_MV_ghost_choir)

<div align="left">

![Unity](https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)

</div>

> **Unity로 렌더링한 뮤직비디오**
>
> 실시간 시네마틱 렌더링과 오디오·비주얼 동기화를 다룬 실험적인 프로젝트입니다.

<details>
<summary>📺 뮤직비디오 보기</summary>

[![PostMV - ghost choir](https://img.youtube.com/vi/znUe_MXd8lU/0.jpg)](https://youtu.be/znUe_MXd8lU)

</details>

---

## 📊 GitHub 통계

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=doqltl179&theme=transparent" alt="프로필 상세" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=doqltl179&theme=transparent" alt="저장소별 주요 언어" height="200" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=doqltl179&theme=transparent" alt="커밋이 가장 많은 언어" height="200" />

<sub>통계는 공개 저장소만 집계합니다.</sub>

</div>

---

## 📫 연락처 및 링크

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-doqltl179-181717?style=for-the-badge&logo=github)](https://github.com/doqltl179)
[![Steam](https://img.shields.io/badge/Steam-The%20Echo%20Escape-1b2838?style=for-the-badge&logo=steam&logoColor=white)](https://store.steampowered.com/app/2875300/The_Echo_Escape/)
[![YouTube](https://img.shields.io/badge/YouTube-Watch-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/znUe_MXd8lU)

</div>

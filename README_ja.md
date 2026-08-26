<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=こんにちは!%20👋&fontSize=70&fontAlignY=40&desc=Unity%20ゲーム開発者%20%7C%20フレームワーク%20%26%20ツール&descSize=20&descAlignY=60)

[![English](https://img.shields.io/badge/Language-English-blue?style=flat-square)](README.md)
[![한국어](https://img.shields.io/badge/Language-한국어-red?style=flat-square)](README_ko.md)
[![日本語](https://img.shields.io/badge/Language-日本語-orange?style=flat-square)](README_ja.md)

### 🚀 自己紹介

Unity のゲーム開発者です。まずフレームワークとエディタツールを作り、その上で動くゲームをリリースしています。

公開している成果物のほとんどは Unity 6 向けのモジュール型パッケージ群 **Mu3Library** にあり、リリース済みのタイトルは Steam で公開しています。

</div>

---

## 🛠 技術スタック

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

## 📂 主なプロジェクト

### 🏗 [Mu3Library For Unity](https://github.com/doqltl179/Mu3Library_ForUnity)

<div align="left">

![Unity](https://img.shields.io/badge/Unity-6000.0%2B-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)
![HLSL](https://img.shields.io/badge/HLSL-DBBC04?style=flat-square)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

> **Unity 6 向けのモジュール型アーキテクチャパッケージ群**
>
> カスタム DI コンテナと MVP UI パターンの上に構成した、3 階層の Unity パッケージです。オプション連携は define シンボルで分離してあるため、UniTask・Addressables・Localization・Input System・Mobile Notifications を導入していないプロジェクトでもそのままコンパイルでき、そのぶんのコストもかかりません。

| パッケージ | バージョン | 依存 |
|---|---|---|
| `Mu3Library_Base` | 0.26.0 | — |
| `Mu3Library_URP` | 0.3.0 | Base |
| `Mu3Library_Game_WatermelonGame` | 0.6.0 | Base, URP |

**主な機能:**
- 💉 **DI コンテナ** — Singleton・Transient・Scoped のライフタイム、Core をまたぐフィールド/プロパティ注入
- 🎨 **MVP UI** — View・Presenter・Model の分離と、await できる開閉処理
- 🏗 **Core モジュール** — `IInitializable`・`IUpdatable`・`IDisposable` による決定的な実行順序
- 🎵 **オーディオ** — BGM・SFX・環境音チャンネル、ミキサーグループのルーティング、BGM ダッキング、await できるフェード、音量の保存
- 🌐 **WebRequest** — GET・POST・PUT・PATCH・DELETE、リトライのバックオフ、実行中のキャンセル、ダウンロード進捗
- 🎮 **入力と通知** — インタラクティブなリバインドとバインディング上書きの保存、Android・iOS でのモバイル通知のスケジューリング
- 🖼 **URP スクリーンエフェクト** — グレースケール、シェイク、ガウシアンブラー、深度アウトラインとカメラスタックのヘルパー
- 🍉 **Watermelon Game パッケージ** — 11 段階の 2D マージボード、設定可能な `BoardConfig`、プレイ可能なサンプルシーン
- 🧰 **エディタツール** — DI 解決のバリデータ、ランタイム診断、Addressables・Localization のエクスポータ
- ✅ **EditMode テスト**と、英語・韓国語・日本語のドキュメント

---

### 🎮 The Echo Escape

<div align="left">

![Unity](https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)
![Steam](https://img.shields.io/badge/Steam-Released-blue?style=flat-square&logo=steam)

</div>

> **Steam でリリースしたホラーゲーム**
>
> 雰囲気のあるストーリーテリングとサウンドデザインを軸にした心理ホラーです。ソースリポジトリは非公開です。

**🔗 [Steam でプレイする](https://store.steampowered.com/app/2875300/The_Echo_Escape/)**

<details>
<summary>📺 トレーラーを見る</summary>

[![The Echo Escape Trailer](https://img.youtube.com/vi/rbei7quiAF4/0.jpg)](https://youtu.be/rbei7quiAF4)

</details>

---

### 🎵 [PostMV - ghost choir](https://github.com/doqltl179/Post_MV_ghost_choir)

<div align="left">

![Unity](https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)

</div>

> **Unity でレンダリングしたミュージックビデオ**
>
> リアルタイムのシネマティックレンダリングと、音と映像の同期を扱った実験的なプロジェクトです。

<details>
<summary>📺 ミュージックビデオを見る</summary>

[![PostMV - ghost choir](https://img.youtube.com/vi/znUe_MXd8lU/0.jpg)](https://youtu.be/znUe_MXd8lU)

</details>

---

## 📊 GitHub 統計

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=doqltl179&theme=transparent" alt="プロフィール詳細" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=doqltl179&theme=transparent" alt="リポジトリ別の主要言語" height="200" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=doqltl179&theme=transparent" alt="コミットが最も多い言語" height="200" />

<sub>統計は公開リポジトリのみを対象としています。</sub>

</div>

---

## 📫 連絡先とリンク

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-doqltl179-181717?style=for-the-badge&logo=github)](https://github.com/doqltl179)
[![Steam](https://img.shields.io/badge/Steam-The%20Echo%20Escape-1b2838?style=for-the-badge&logo=steam&logoColor=white)](https://store.steampowered.com/app/2875300/The_Echo_Escape/)
[![YouTube](https://img.shields.io/badge/YouTube-Watch-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/znUe_MXd8lU)

</div>

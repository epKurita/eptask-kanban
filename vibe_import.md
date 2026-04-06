# Vibe Kanban Import Draft

## 1. TypeAアプリ開発 lite版実装

- Backlog Key: AIGEN2024-503
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-503
- Source Issue ID: 8150681
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: AIGEN2024-503
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-503
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
* PDS-A Lite版の設計・実装
* RTSPカメラ＋Orin Nanoの構成でカウント専用デバイスを開発する
* TA2025GUIプロジェクトで課題管理

### 完了条件
* Lite版のバックエンド・PDS-Remoteが一通り動作し、現場テスト可能な状態になる
```

## 2. PDS_TypeB試作機開発 Engine実装（マイルストーン：未設定）

- Backlog Key: AIGEN2024-459
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-459
- Source Issue ID: 7849786
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: AIGEN2024-459
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-459
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要


### 完了条件
```

## 3. PDS-Remote カウントライン調整画面実装

- Backlog Key: TA2025GUI-446
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-446
- Source Issue ID: 8150591
- Parent Issue ID: 8150609
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-446
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-446
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
### 概要
FR-006 のフロントエンド側実装。
PDS-Remote 上でライブ映像を表示し、その上にカウントラインを重ねて表示し、ドラッグ操作でライン位置を調整する画面を実装する。
調整結果はタスク8（バックエンド）を経由して Camera Profile に紐づけて保存される。
TA2025GUI-428（画面差分設計）の設計結果に基づく。

### 完了条件
* ライブ映像上にカウントラインが重畳表示されること
* ドラッグ操作でカウントラインの位置を変更できること
* 調整後のライン位置がバックエンドに送信され、即座にカウント判定に反映されること
* 画面を閉じて再度開いた際に、保存済みのライン位置が復元されること
```

## 4. PDS-A Lite開発

- Backlog Key: ABC_T3_PROT-327
- Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-327
- Source Issue ID: 8147411
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: 田中寛樹
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: ABC_T3_PROT-327
Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-327
Assignee: 田中寛樹
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
開発仕様書案
https://docs.google.com/document/d/1N2FuZnJ1x69XYVEZMqpQZYO1NlOUWwjppybjJ_XfKVY/edit?tab=t.0
```

## 5. PDS-Remote 機能実装

- Backlog Key: TA2025GUI-452
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-452
- Source Issue ID: 8150609
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: TA2025GUI-452
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-452
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
PDS-A Lite 向け PDS-Remote（Flutter）の機能実装を管理する親タスク。
TA2025GUI-432「PDS-Remote 連携の最小実装」（デバイス自動検出、カウント値リアルタイム表示）の完了を前提に、仕様書 §7 FR-003「全ユーザー操作を PDS-Remote から実行できる」を実現するための各画面・機能を実装する。
対象リポジトリは ep-typea-app-lite の frontend/ ディレクトリ。
TA2025GUI-428（画面差分設計）の設計結果に基づく。

### 完了条件
* アプリ起動時にイントロ画面（ロゴ + 開始ボタン）が表示されること
* ボトムタブナビゲーション（カウント / ライブ / 設定）が動作すること
* セッション制御（開始/停止/リセット）が PDS-Remote から操作可能であること
* カウントライン位置調整がライブ映像上で操作可能であること
* CSV 取得がセッション単位で実行可能であること
* Lite 向け設定画面（Camera Profile 選択等）が動作すること
* デバイス接続断時のオフライン表示・自動リトライが動作すること
* 既知デバイスへの自動接続が動作すること
* 子タスクが全て完了していること
```

## 6. PDS-Remote セッション制御 UI 実装

- Backlog Key: TA2025GUI-445
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-445
- Source Issue ID: 8150590
- Parent Issue ID: 8150609
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-445
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-445
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
PDS-Remote（Flutter）上でセッションの開始・停止・リセットを操作する UI を実装する。
TA2025GUI-432 のフロントエンド実装計画で Start/Stop/Save ボタンの UI ウィジェット（HeadsRemoteControl）は通常版からポートする方針だが、432 の完了条件はカウント値のリアルタイム表示までであり、ボタンの操作によるバックエンドへのコマンド送信とレスポンス処理は含まれていない。
タスク3（Session Manager）とタスク6（Remote Control Server 拡張）で実装されるバックエンド API に対して、フロントエンドからコマンドを送信し、状態表示に反映する。

### 完了条件
* Start ボタン押下でバックエンドにセッション開始コマンドが送信され、カウントが開始されること
* Stop ボタン押下でセッション停止コマンドが送信され、カウントが停止すること
* Save / Reset 操作が正常に動作すること
* 現在のセッション状態（COUNTING / STOPPED）が画面上にリアルタイムに反映されること（l10n キー: countingStatus / stoppedStatus）
* コマンド送信失敗時にエラーが表示されること
```

## 7. PDS-Remote CSV 取得画面実装

- Backlog Key: TA2025GUI-447
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-447
- Source Issue ID: 8150592
- Parent Issue ID: 8150609
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-447
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-447
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
FR-009「CSV を生成し、PDS-Remote または PDS-Dash から取得できる」のフロントエンド側実装。
セッション一覧を表示し、選択したセッションの CSV をバックエンドからダウンロードする画面を実装する。
CSV フォーマットは §11.4 のcount-only仕様に従う。TA2025GUI-428（画面差分設計）の設計結果に基づく。

### 完了条件
* 完了済みセッションの一覧が表示されること
* セッションを選択して CSV ダウンロードを実行できること
* ダウンロードされた CSV が §11.4 の列定義に準拠していること
* ダウンロード中の進捗が表示されること
* ダウンロード失敗時にエラーが表示され、再試行可能であること
```

## 8. PDS-Remote 設定画面実装

- Backlog Key: TA2025GUI-448
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-448
- Source Issue ID: 8150593
- Parent Issue ID: 8150609
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-448
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-448
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
TA2025GUI-428（画面差分設計）で設計中の Lite 向け設定画面を実装する。
Camera Profile の選択・適用（FR-014）、デバイス情報表示、ネットワーク状態表示などを含む。通常版の system_settings_screen.dart を参考に、Lite で不要な体重系設定を除外し、Camera Profile 選択など Lite 固有の設定項目を追加する。
§12.1 の一般操作と管理者操作の権限分離も画面上で反映する。

### 完了条件
* Camera Profile の一覧表示と選択・適用が動作すること
* 選択した Camera Profile がバックエンドに送信され、Frame Normalizer に反映されること
* デバイス情報（device_id, firmware_version 等）が表示されること
* 体重系の設定項目が含まれていないこと（FR-002）
* 管理者操作（保守モード遷移、OTA 起動等）が一般操作と分離されていること（§12.1）
```

## 9. PDS-Remote オフライン表示実装

- Backlog Key: TA2025GUI-449
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-449
- Source Issue ID: 8150595
- Parent Issue ID: 8150609
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-449
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-449
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
TA2025GUI-432 のフロントエンド実装計画で「Separate task」と明記されている、デバイス接続断時の表示処理を実装する。
TCP 接続断を検知し、オフラインオーバーレイを表示してユーザーに状態を通知する。通常版の offline_overlay.dart を参考にする。
432 の実装計画 Issue 6 で指摘された自動リトライ（exponential backoff）を含む。

### 完了条件
* TCP 接続断時にオフラインオーバーレイが画面上に表示されること
* 自動再接続が設定可能な間隔でリトライされること（432 実装計画 Issue 6: edge device は起動に30秒以上かかりうる）
* 接続復旧時にオーバーレイが自動的に消え、カウント表示が再開されること
* リトライ中であることがユーザーに視覚的に伝わること
```

## 10. PDS-Remote デバイス登録・自動接続実装

- Backlog Key: TA2025GUI-450
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-450
- Source Issue ID: 8150597
- Parent Issue ID: 8150609
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-450
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-450
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
TA2025GUI-432 のフロントエンド実装計画で「Separate task」と明記されている機能。
前回接続したデバイスの情報を永続化し、アプリ起動時に自動的に接続を試みる。通常版の registered_device.dart に相当する機能を Lite 向けに実装する。
FR-005「ローカル LAN 上でデバイスを自動検出できる」と組み合わせ、既知デバイスへの即時接続と未知デバイスのスキャン発見の両方をサポートする。

### 完了条件
* 接続済みデバイスの情報（デバイス名、IP アドレス、デバイスタイプ等）がローカルに保存されること
* アプリ起動時に保存済みデバイスへの自動接続が試みられること
* 自動接続に失敗した場合に UDP スキャンによるデバイス発見にフォールバックすること
* 登録済みデバイスの削除が可能であること
```

## 11. Camera Adapter 堅牢化実装

- Backlog Key: TA2025GUI-435
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-435
- Source Issue ID: 8150573
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-435
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-435
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
最小構成パイプラインで実装する最小限のRTSP受信処理を堅牢化する。
仕様書 §10.2 で Camera Adapter の責務として定義されている「再接続」「時刻管理」を追加実装する。ネットワークカメラはケーブル抜けや一時的なネットワーク断により RTSP 接続が切断されるケースがあり、NFR-004「電源再投入後に自動復帰し、最後の安定状態で再開する」の要件にも関連する。

### 完了条件
* RTSP 接続断が発生した場合に自動再接続が行われ、映像取得が復旧すること
* 再接続中もプロセス全体がクラッシュしないこと
* 再接続のリトライ間隔・最大リトライ回数が設定ファイルで変更可能であること
* フレームのタイムスタンプが NTP 同期済み時刻と整合していること
```

## 12. Frame Normalizer 実装

- Backlog Key: TA2025GUI-436
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-436
- Source Issue ID: 8150574
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-436
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-436
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要

仕様書 §10.2 で定義された Frame Normalizer モジュールを実装する。
Camera Profile（TA2025GUI-426 で設計中）の定義に基づき、カメラ固有の歪み補正、crop/warp/scale、色調補正を行い、推論モデルが期待する入力形式（RealSense RGB 相当、§9.2）に整形する。
§6 の Camera abstraction 原則「カメラ固有処理は隔離し、カウントロジックは共通化する」の実装に該当する。

### 完了条件
* 
* Camera Profile JSON を読み込み、指定された補正パラメータに従ってフレームが変換されること
* 変換後のフレームサイズ・画角が RealSense RGB 相当であること（Camera Profile で規定された crop/warp/scale 条件を満たす）
* Camera Profile が異なるカメラ機種に切り替えた場合でも、Profile の差し替えのみで動作すること
* 推論パイプライン（PigTracker）に変換後フレームを渡し、検出が正常に動作すること
```

## 13. Session Manager 実装

- Backlog Key: TA2025GUI-437
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-437
- Source Issue ID: 8150576
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-437
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-437
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
仕様書 §10.2 / §10.3 で定義されたセッションのライフサイクル管理モジュールを実装する。
計測セッションの開始・停止・リセット（FR-004）を管理し、状態遷移（Standby → Running → Stopped、§10.3）を制御する。
セッション単位で PassageEvent とSession Summary を記録するための基盤となる。
Remote Control Server からの制御コマンド（424 で設計中）を受け付けるインターフェースを持つ。

### 完了条件
* 開始コマンドにより Standby → Running へ遷移し、カウントイベントの記録が開始されること
* 停止コマンドにより Running → Stopped へ遷移し、イベント記録が停止すること
* リセットコマンドによりカウント値が初期化され Standby に戻ること
* 状態遷移が §10.3 の定義（Standby / Running / Stopped / Maintenance）に準拠していること
* セッションごとに一意の session_id が発行されること（§11.3 Session Summary の session_id）
* 異常状態（二重開始、停止中の停止等）に対してエラーを返すこと
```

## 14. Data Manager 実装

- Backlog Key: TA2025GUI-438
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-438
- Source Issue ID: 8150577
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-438
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-438
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要

仕様書 §10.2 の Data Manager モジュールを実装する。
PassageEvent（§11.3: session_id, event_time_utc, direction, track_id, confidence, net_count_after_event）のローカル保存、Session Summary の生成、count-only CSV の生成（§11.4）を担う。
FR-008「カウントイベントとセッションサマリをローカル保存できる。
ネットワーク断中も保持する」の要件を満たす。

### 完了条件

* PassageEvent が §11.3 のスキーマに従ってローカルストレージに記録されること
* セッション停止時に Session Summary（§11.3: session_id, device_id, start_time_utc, end_time_utc, total_forward, total_reverse, total_net, camera_profile_id, firmware_version）が生成されること
* CSV ファイルが §11.4 の列定義（session_id, event_time_utc, direction, track_id, confidence, net_count_after_event）に準拠して出力されること
* 体重列が CSV に含まれないこと（§11.4 注記）
* プロセス再起動後も保存済みデータが失われないこと（FR-008）
```

## 15. Sync Agent 実装

- Backlog Key: TA2025GUI-439
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-439
- Source Issue ID: 8150578
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-439
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-439
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
仕様書 §10.2 の Sync Agent モジュールを実装する。
FR-010「カウントデータをクラウドへ送信できる」および FR-011「ネットワーク断時もカウント継続し、復旧後に再送する。
重複送信防止を含む」の要件に対応する。
§6 の edge-first / offline-first 原則に従い、store-and-forward 方式でイベントをバッファリングし、クラウド復旧後に順序を維持して再送する（§12.3）。

### 完了条件
* カウントイベントおよびセッションサマリがクラウド API へ送信されること
* ネットワーク断時にイベントがローカルにバッファリングされ、カウント処理が中断しないこと
* ネットワーク復旧後にバッファ内のイベントが送信順序を維持して再送されること
* 同一イベントが重複送信されないこと（FR-011）
* クラウド通信が TLS で保護されていること（§12.1）
```

## 16. Remote Control Server 拡張

- Backlog Key: TA2025GUI-440
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-440
- Source Issue ID: 8150579
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-440
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-440
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
TA2025GUI-432 で実装する最小 Remote Control Server（UDP デバイス発見 + TCP getStatus）を拡張し、TA2025GUI-424 で定義中の全コマンドに対応する。
対象コマンド：セッション開始/停止/リセット（FR-004）、カウントライン位置設定（FR-006）、ライブ映像フレーム取得（FR-007）、CSV 取得（FR-009）、Camera Profile 適用（FR-014）。
エラーレスポンスフォーマット（424 で定義）にも準拠する。

### 完了条件
* 424 で定義された全コマンドのリクエストに対して、仕様通りのレスポンスが返ること
* 不正なコマンドや不正なパラメータに対して、定義済みエラーレスポンスが返ること
* 各コマンドが対応するバックエンドモジュール（Session Manager, Data Manager 等）を正しく呼び出すこと
* 複数の PDS-Remote クライアントから同時接続しても競合しないこと
```

## 17. ライブ映像配信実装

- Backlog Key: TA2025GUI-441
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-441
- Source Issue ID: 8150580
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-441
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-441
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
FR-007「ライブ映像を PDS-Remote 上で確認できる」を実装する。
仕様書 §7 FR-007 の備考で「推論用ストリームとは分離した低負荷閲覧経路を推奨」と記載されており、推論パイプラインの負荷に影響を与えない配信方式を設計・実装する。
PDS-Remote からのコマンド（タスク6）によりフレーム配信を開始し、カウントライン位置調整（FR-006）の前提機能となる。

完了条件：
* PDS-Remote からライブ映像取得コマンドを送信し、映像フレームがリアルタイムに受信・表示できること
* ライブ映像配信中に推論パイプラインの FPS が低下しないこと（推論用ストリームとの分離）
* 配信の開始・停止が Remote Control Server 経由で制御可能であること
* ネットワーク帯域が制約される環境でも推論処理が優先されること
```

## 18. カウントライン位置設定実装

- Backlog Key: TA2025GUI-442
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-442
- Source Issue ID: 8150582
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-442
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-442
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
FR-006「PDS-Remote 上でカウントライン位置を調整し、本体へ反映できる」を実装する。
仕様書 §7 FR-006 の備考で「位置情報は Camera Profile を前提に保存する」と記載されており、Camera Profile（TA2025GUI-426）に紐づけてライン位置を永続化する。
PigTracker / Counter のカウント判定ラインを動的に変更するバックエンド処理と、変更結果の保存を含む。

### 完了条件
* PDS-Remote から送信されたカウントライン位置座標が Counter モジュールに反映されること
* 変更されたライン位置が Camera Profile に紐づいてローカルに保存されること
* プロセス再起動後も保存されたライン位置が復元されること
* ライン位置変更後のカウント判定が新しいライン位置に基づいて動作すること
```

## 19. 保守モード実装

- Backlog Key: TA2025GUI-443
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-443
- Source Issue ID: 8150584
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-443
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-443
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
FR-012「管理者向けに保守モードを提供する」および §10.3 の Maintenance 状態を実装する。
§12.1 に記載のサービスボタン押下による再ペアリング許可、§12.3 のログ取得、ネットワーク設定変更を、シリアルターミナル経由で操作可能にする。
§6 Headless but recoverable 原則「画面なしでも保守不能にならない復旧導線を設ける」に該当する。
§8 NFR-008「サービスボタン・LED・ログ取得により画面無しでも復旧できる」の実装を含む。

### 完了条件
* サービスボタン押下により Maintenance 状態へ遷移すること
* Maintenance 状態でシリアルターミナルからログ取得、ネットワーク設定変更、再ペアリングが実行可能であること
* 状態 LED により電源、ネットワーク、同期、保守モードの状態が視覚的に識別可能であること（§12.3）
* Maintenance 状態から Standby 状態へ復帰できること
* サービスボタン押下時のみ再ペアリングが許可されること（§12.1）
```

## 20. NTP 時刻同期実装

- Backlog Key: TA2025GUI-444
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-444
- Source Issue ID: 8150586
- Parent Issue ID: 8150607
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-444
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-444
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
NFR-007「NTP によりイベント時刻の整合を保つ」を実装する。
CSV の event_time_utc（§11.4）、Session Summary の start_time_utc / end_time_utc（§11.3）、クラウド同期時のイベント順序（§12.3「順序を維持して再送」）の整合性に直結する。
仕様書 §8 NFR-007 の備考に「バッテリー強化」との注記があり、電源断時の時刻保持方針も含めて対応する。

### 完了条件
* 起動時に NTP サーバーと時刻同期が行われること
* NTP 同期成功後のイベント時刻（event_time_utc）が UTC / ISO8601 形式で正確に記録されること
* NTP サーバーに接続できない場合でもプロセスが起動し、ローカル時刻でイベント記録が継続されること
* 電源再投入後に時刻が大幅にずれない対策が実装されていること（RTC / バッテリーバックアップ）
```

## 21. バックエンド機能実装

- Backlog Key: TA2025GUI-451
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-451
- Source Issue ID: 8150607
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-451
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-451
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
PDS-A Lite バックエンド（C++）の機能実装を管理する親タスク。
TA2025GUI-429「基本構成の確立」（リポジトリ作成、最小パイプライン、PDS-Remote 最小連携）の完了を前提に、仕様書 §10.2 で定義された各ソフトウェアモジュール（Camera Adapter 堅牢化、Frame Normalizer、Session Manager、Data Manager、Sync Agent、Remote Control Server 拡張、ライブ映像配信、カウントライン位置設定、保守モード、NTP 時刻同期）の実装を行う.
対象リポジトリは ep-typea-app-lite の backend/ ディレクトリ。

### 完了条件
* 仕様書 §7 の機能要件 FR-001〜FR-014 のうち v1 対象範囲が全てバックエンド側で動作すること
* 仕様書 §10.3 の状態遷移（Standby / Running / Stopped / Maintenance）が正しく機能すること
* PDS-Remote からの全制御コマンド（TA2025GUI-424 で定義）に対してバックエンドが応答すること
* 子タスク（1〜10）が全て完了していること
```

## 22. 管理コンソールエンドポイント追加

- Backlog Key: TA2025GUI-363
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-363
- Source Issue ID: 7747064
- Parent Issue ID: 7736986
- Status: Open
- Priority: Normal
- Assignee: 西村 堅太郎
- Due: -

```text
Backlog Key: TA2025GUI-363
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-363
Assignee: 西村 堅太郎
Priority: Normal
Status (source): Open
Due: -

Original Description:
(no description)
```

## 23. 管理コンソールダウンロード機能追加

- Backlog Key: TA2025GUI-364
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-364
- Source Issue ID: 7747067
- Parent Issue ID: 7736986
- Status: Open
- Priority: Normal
- Assignee: 西村 堅太郎
- Due: -

```text
Backlog Key: TA2025GUI-364
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-364
Assignee: 西村 堅太郎
Priority: Normal
Status (source): Open
Due: -

Original Description:
アップロードされたログファイルやmp4をダウンロードする機能の追加実装
```

## 24. 量子化ベンチマーク

- Backlog Key: TA2025GUI-189
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-189
- Source Issue ID: 7322146
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Batnasan Baasanchuluun
- Due: -

```text
Backlog Key: TA2025GUI-189
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-189
Assignee: Batnasan Baasanchuluun
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
ある程度精度が出るまで保留にしてたタスク
推論モデルを16ビット半精度浮動小数点数にし、パラメータ数が大きいとモデルと比較
FPS大幅低下しない、モデル精度の大幅な劣化が起きないことが確認できたら採用する
```

## 25. CVATのプロジェクト整理

- Backlog Key: PDSB-482
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-482
- Source Issue ID: 8142767
- Parent Issue ID: 7664819
- Status: In Progress
- Priority: Normal
- Assignee: 影澤
- Due: -

```text
Backlog Key: PDSB-482
Backlog URL: https://eco-pork.backlog.com/view/PDSB-482
Assignee: 影澤
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
(no description)
```

## 26. 1~3ロットの肥育データの分析検討

- Backlog Key: SBIR_PJT-1180
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1180
- Source Issue ID: 8097274
- Parent Issue ID: -
- Status: In Progress
- Priority: High
- Assignee: 東間千芽
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: SBIR_PJT-1180
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1180
Assignee: 東間千芽
Priority: High
Status (source): In Progress
Due: 2026-04-10T00:00:00Z

Original Description:
## 目的
1~3ロットの肥育データからできることを提案する
https://claude.ai/artifacts/364748cd-a819-4b25-9823-62fbf97efff8

## 完了条件

## 検討履歴
コメント記載
 - 3/23の週のはじめに鈴木さんにいったん報告
 - 4/6の週（仮）に社長に報告

## 残論点
* [ ]
```

## 27. [Frontend]カメラ詳細画面

- Backlog Key: TA2025GUI-394
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-394
- Source Issue ID: 8039191
- Parent Issue ID: 8039171
- Status: In Progress
- Priority: Normal
- Assignee: Terada Misaki
- Due: -

```text
Backlog Key: TA2025GUI-394
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-394
Assignee: Terada Misaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
- 既存の詳細設定モード画面で扱っていた「豚認識感度」設定と「精度優先露出制御」設定をこちらのカメラ   - 詳細設定画面で行えるようにする
    - リモート接続設定の場合、カメラごとにこの設定を保持する必要がある
      - remote_cameras.jsonの仕様を拡張し、設定内容を保持できるようにする。また、カメラ一覧取得コマンドでこれらのパラメータが返ってくるようにする
- 保存ボタンを配置する
  - 設定を保存してカメラ一覧モード画面に戻る
- 取消ボタンを配置する
  - 設定を保存せずにカメラ一覧モード画面に戻る
- デザインファイルにはメインメニュータブが表示されているため、デザインを修正する
```

## 28. 最小構成パイプライン実装・動作確認

- Backlog Key: TA2025GUI-434
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-434
- Source Issue ID: 8150260
- Parent Issue ID: 8150232
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-434
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-434
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
### 概要
RTSP カメラ → PigTracker → Counter のパイプラインを Orin Nano 上で実装し、カウント値が標準出力に出ることを確認する

### 完了条件
Orin Nano 上でパイプラインが動作し、豚の通過時にカウント値が変化する
```

## 29. [設計] RemoteControl API コマンド仕様の作成

- Backlog Key: TA2025GUI-424
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-424
- Source Issue ID: 8149305
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-424
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-424
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
### 概要
PDS-A Lite バックエンド（C++）と Lite 版 PDS-Remote（新規 Flutter アプリ）間の通信仕様を設計する。
UDP デバイス発見と TCP 制御通信の両方を対象とする。

### 設計が必要な内容

### UDP デバイス発見（ポート 6000）
- 通常版の発見プロトコル（PIG_DATASTATION_DISCOVERY_REQUEST / RESPONSE）を踏襲するか、変更するかを決定する
- ステータスチェック（PIG_DATASTATION_STATUS_CHECK）の扱いを決定する
- レスポンス JSON のフォーマット（デバイス名、デバイス種別（Lite / 通常版）等）を定義する

### TCP 制御通信（ポート 1129）
- メッセージフォーマット（通常版と同じ 4バイト長さプレフィックス + JSON を踏襲するか）を決定する
- 以下のコマンドのリクエスト / レスポンス JSON を定義する
  - カウント値取得（getStatus 相当）
  - セッション開始 / 停止 / リセット（FR-004）
  - カウントライン位置設定（FR-006）
  - ライブ映像確認（FR-007）
  - CSV 取得（FR-009）
  - Camera Profile 適用（FR-014）
- エラーレスポンスのフォーマットを定義する
- 通常版の setWeightMode / changeDomain / DetectFloorDistance は Lite では不要
```

## 30. 量子化による精度劣化および処理能力の確認

- Backlog Key: TA2025GUI-423
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-423
- Source Issue ID: 8147871
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: Batnasan Baasanchuluun
- Due: -

```text
Backlog Key: TA2025GUI-423
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-423
Assignee: Batnasan Baasanchuluun
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要

TypeAの最新データセットを使い、量子化による精度劣化および処理能力の変化を確認する
https://eco-pork.slack.com/archives/C068822NLBY/p1775201387137239

* FPS
* box mask map50, box mask map50-95
* メモリ使用量
* モデルサイズ
```

## 31. 実行環境のディレクトリ構成

- Backlog Key: TA2025GUI-431
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-431
- Source Issue ID: 8150238
- Parent Issue ID: 8150232
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: TA2025GUI-431
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-431
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
TypeA 通常版の実行環境（/app_typea/ 配下のディレクトリ構造、設定ファイル、暗号化 engine ファイル、ログ出力先など）を整理し、Lite 版で不要なもの（体重系、RealSense 関連）と追加が必要なもの（lite_config.json、Camera Profile 設定ファイル）を洗い出す。結果をドキュメント化する

### 完了条件
lite版実行環境をドキュメント化する
```

## 32. 基本構成の確立

- Backlog Key: TA2025GUI-429
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-429
- Source Issue ID: 8150232
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: -
- Due: -

```text
Backlog Key: TA2025GUI-429
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-429
Assignee: -
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
Lite版の開発基盤を整備する親タスク
```

## 33. 体重推計用データセット作成

- Backlog Key: PDS_TB_PROT-151
- Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-151
- Source Issue ID: 7885544
- Parent Issue ID: 7883978
- Status: In Progress
- Priority: Normal
- Assignee: 影澤
- Due: -

```text
Backlog Key: PDS_TB_PROT-151
Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-151
Assignee: 影澤
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
NVRからデータを取得し、体重データと紐付ける
学習用のデータセットを作成する

### 完了条件
```

## 34. TypeBテスト用データ作成

- Backlog Key: PDSB-481
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-481
- Source Issue ID: 8140594
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: 田中寛樹
- Due: 2026-04-03T00:00:00Z

```text
Backlog Key: PDSB-481
Backlog URL: https://eco-pork.backlog.com/view/PDSB-481
Assignee: 田中寛樹
Priority: Normal
Status (source): Open
Due: 2026-04-03T00:00:00Z

Original Description:
SDF
ARK

改めてNVRから過去日付のデータを収集、イメージセットを作成する

NVRとネットワークの負荷を確認しながら通常運用に支障が発生しないように注意が必要
```

## 35. Jetson Orin Nano デコードのパフォーマンス計測

- Backlog Key: TA2025GUI-421
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-421
- Source Issue ID: 8147069
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-421
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-421
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
### 概要

* RTSPを受信してデコードするだけの処理を作成し、長時間稼働させる
* 描画は不要
* 発熱やメモリ使用量を確認する
* Orin NX 16Gと比較する（通常版TypeA）

### 完了条件

テスト結果を記録する
```

## 36. [設計] Camera Profile JSON スキーマ定義の作成

- Backlog Key: TA2025GUI-426
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-426
- Source Issue ID: 8149311
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-426
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-426
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
## 概要
承認済みネットワークカメラ機種ごとの Camera Profile を JSON として定義する。
CameraAdapter と FrameNormalizer の両方に影響するため、実装前に確定が必要。

## 定義が必要なフィールド（仕様書 §11.2 より）

- `camera_model_id`
- 推奨解像度 / fps
- RTSP パス形式
- 内部パラメータ / 歪み係数
- RealSense RGB 相当へ合わせる crop / warp / scale 条件
- 露出 / ゲイン / WB の標準値
- 推奨取付高さ / 俯角 / 設置治具情報
```

## 37. [設計] PDS-Remote 追加画面差分設計

- Backlog Key: TA2025GUI-428
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-428
- Source Issue ID: 8149313
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-428
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-428
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
## 概要
ep-typea-controller（PDS-Remote）に対して PDS-A Lite 向けに必要な追加画面・権限設計を定義する

## 背景
仕様書 §14.2 にて「PDS-Remote の画面差分：未決。既存アプリへの追加画面・権限設計を別紙で確定」と明記されている。
仕様書では「既存アプリを拡張して正式 UI とする」方針（§5.2）。

## 定義が必要な内容
- 既存画面のうち Lite で不要なもの（体重モード関連）
- Lite 向けに追加が必要な画面
  - Camera Profile 選択・適用画面
  - カウントライン位置調整画面（FR-006）
  - CSV 取得画面（FR-009）
  - セッション管理画面（FR-004）
- 一般操作と管理者操作の権限分離（仕様書 §12.1）
```

## 38. [設計] モジュール間インターフェース定義の作成

- Backlog Key: TA2025GUI-425
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-425
- Source Issue ID: 8149308
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: TA2025GUI-425
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-425
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: 2026-04-06T00:00:00Z

Original Description:
## 概要
PDS-A Lite を構成する各モジュール間の呼び出し関係・データ型・スレッド境界を定義し、実装の認識ズレを防ぐ。

## 定義が必要なインターフェース

### メイン処理パイプライン
```
CameraAdapter
  → FrameNormalizer   : cv::Mat（生フレーム）
  → PigTracker::Update(cv::Mat, bool) : std::vector<Pig>
  → Counter           : 通過イベント（方向・track_id・信頼度）
  → SessionManager    : PassageEvent
  → DataManager       : イベント記録・CSV 生成
  → SyncAgent         : クラウド送信キュー
```

### 制御系
```
RemoteControlServer
  → SessionManager    : 開始 / 停止 / リセット
  → DataManager       : CSV 取得
  → CameraAdapter     : ライブフレーム取得
```
```

## 39. 開発機台数確認

- Backlog Key: ABC_T3_PROT-331
- Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-331
- Source Issue ID: 8149324
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: -
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: ABC_T3_PROT-331
Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-331
Assignee: -
Priority: Normal
Status (source): Open
Due: 2026-04-06T00:00:00Z

Original Description:
### 概要
* 社内にある `Jetson Orin Nano 8G `のうち、lite版の開発で使用可能なものの台数を確認する
* 実装担当する可能性のある人数分確保できない場合、追加購入するのか決める
```

## 40. 【Claude自動化】GAS v19デプロイ — 議事録Docs週次自動分割

- Backlog Key: EP_ALL_PJT-850
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-850
- Source Issue ID: 8149263
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: あらふか
- Due: -

```text
Backlog Key: EP_ALL_PJT-850
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-850
Assignee: あらふか
Priority: Normal
Status (source): Open
Due: -

Original Description:
## 背景
議事録Docsのタブ数が66超でV8ランタイムのメモリ上限を超過しクラッシュする問題の根本対策。
週次（ISO週番号ベース）でDocsを自動分割するGAS v19を開発済み。コードは完成しているがApps Scriptへのデプロイが未完了。

## 完成済み成果物
- `claude-hub/workspaces/gemini-meeting-minutes/outputs/code-v19.gs`（日本語コメント版）
- `claude-hub/workspaces/gemini-meeting-minutes/outputs/code-v19-ascii.gs`（ASCII版）
- `claude-hub/workspaces/gemini-meeting-minutes/designs/2026-03-31_weekly-doc-split.md`（設計書）

## 残タスク
1. Apps Scriptエディタでv19コードを既存コード.gsに上書き保存
2. 「デプロイを管理」→「新しいバージョン」で公開
3. GAS APIエンドポイント経由で動作テスト（insert_markdownアクション）
4. SKILL.md更新（週次Doc関連のSTEP追加、デプロイURL変更があれば.env更新）

## 注意事項
- Apps ScriptエディタのUI操作が必要（clasp未設定）
- マルチバイト文字問題がある場合はASCII版を使用
- Apps Scriptプロジェクト: https://script.google.com/home/projects/1hMxuDUXcTEjTSy-MAIKKk7fj35NxxrbGifl8_RKe2zAEuoVUvGAL7Fsc/edit

## 関連
- HANDOFF: HO-008
```

## 41. 面積版体重推計202604031341データセット作成

- Backlog Key: PDS_TB_PROT-248
- Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-248
- Source Issue ID: 8149218
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: PDS_TB_PROT-248
Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-248
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
* 姿勢情報追加による精度の変化確認用
* 全データではなく一部のデータ（精度自体は低下する）https://eco-pork.slack.com/archives/C068822NLBY/p1775185273807219
* 姿勢ラベル追加完了したデータセットで、姿勢情報ありと姿勢情報なしのモデルを作成し精度を比較する

### 完了条件
結果を記録する
```

## 42. Jetson Orin Nano 8G パフォーマンス再検証

- Backlog Key: TA2025GUI-418
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-418
- Source Issue ID: 8146955
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: TA2025GUI-418
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-418
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要

* RTSPのデコードしながら推論処理を動かしFPSを計測する
* カメラFPS下回らないか確認する
* メモリの推移を30分程度確認する
* 25Wモードで運用した場合の発熱　その他想定外の挙動がないか
```

## 43. スケジュール確認・マイルストーン設定

- Backlog Key: ABC_T3_PROT-328
- Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-328
- Source Issue ID: 8147881
- Parent Issue ID: 8147411
- Status: Open
- Priority: Normal
- Assignee: -
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: ABC_T3_PROT-328
Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-328
Assignee: -
Priority: Normal
Status (source): Open
Due: 2026-04-06T00:00:00Z

Original Description:
(no description)
```

## 44. パラメータ受け渡し用API実装

- Backlog Key: PDS_TB_PROT-246
- Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-246
- Source Issue ID: 8138910
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: Masaki Muraoka
- Due: -

```text
Backlog Key: PDS_TB_PROT-246
Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-246
Assignee: Masaki Muraoka
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
分類用のlibが直接設定ファイルを読む構造となっているため、専用の設定ファイルが必要となっている
lib側にパラメータ受け取り用のAPIを設置し、アプリ側で読み込んだ設定を渡せるようにする。

参考は、ep-weight-predictorリポジトリ

### 完了条件
マージされる
```

## 45. 頭数モードクレーム

- Backlog Key: PDS_CS-35
- Backlog URL: https://eco-pork.backlog.com/view/PDS_CS-35
- Source Issue ID: 8040083
- Parent Issue ID: 7798231
- Status: In Progress
- Priority: Normal
- Assignee: Masaki Muraoka
- Due: 2026-03-20T00:00:00Z

```text
Backlog Key: PDS_CS-35
Backlog URL: https://eco-pork.backlog.com/view/PDS_CS-35
Assignee: Masaki Muraoka
Priority: Normal
Status (source): In Progress
Due: 2026-03-20T00:00:00Z

Original Description:
サン・ダイコー小野さん経由で農場主から頭数のカウントがずれるとのこと
・設置環境の写真共有を依頼
・頭数制度のズレ幅をヒアリング依頼
・ネット環境の確認依頼
```

## 46. AgventureLabs: デンマーク大使館ルートではなく日本側責任者への挨拶・インプット

- Backlog Key: EP_ALL_PJT-849
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-849
- Source Issue ID: 8149118
- Parent Issue ID: 8097178
- Status: Open
- Priority: High
- Assignee: 沼澤祐介
- Due: 2026-04-05T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-849
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-849
Assignee: 沼澤祐介
Priority: High
Status (source): Open
Due: 2026-04-05T00:00:00Z

Original Description:
■サマリー
AgventureLabs: デンマーク大使館ルートではなく日本側責任者への挨拶・インプット

■詳細
会議名: 【内M@Meet】AgventureLabs補助金（2026年4月3日）
Gemini会議メモより
内容: デンマーク大使館ルートではなく、日本側の責任者への挨拶とインプットを試みる。
```

## 47. Danish Crown日本法人マーケティング責任者との面談調整（4/15前）

- Backlog Key: EP_ALL_PJT-848
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-848
- Source Issue ID: 8149117
- Parent Issue ID: -
- Status: Open
- Priority: High
- Assignee: 沼澤祐介
- Due: -

```text
Backlog Key: EP_ALL_PJT-848
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-848
Assignee: 沼澤祐介
Priority: High
Status (source): Open
Due: -

Original Description:
■サマリー
Danish Crown日本法人マーケティング責任者との面談調整（4/15前）

■詳細
会議名: 【内M@Meet】AgventureLabs補助金（2026年4月3日）
Gemini会議メモより
内容: デンマーク大使館を通じた海外企業との連携強化の一環。Danish Crown日本法人のマーケティング責任者との面談を4月15日前までに調整する。
```

## 48. PDS-A Lite版開発仕様書のレビューコメント提出

- Backlog Key: EP_ALL_PJT-847
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-847
- Source Issue ID: 8149116
- Parent Issue ID: 8097178
- Status: Open
- Priority: High
- Assignee: 沼澤祐介
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-847
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-847
Assignee: 沼澤祐介
Priority: High
Status (source): Open
Due: 2026-04-06T00:00:00Z

Original Description:
■サマリー
PDS-A Lite版開発仕様書のレビューコメント提出

■詳細
依頼者: 田中寛樹 (#dev_pds)
チャンネル: #dev_pds
日時: 2026/04/03 16:10
内容: PDS-A Lite版の開発仕様書案を作成したので確認コメントをお願いしますとのこと。
```

## 49. R6補正グローバルサウス補助金 交付申請内容の不備修正・再申請

- Backlog Key: EP_ALL_PJT-846
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-846
- Source Issue ID: 8149115
- Parent Issue ID: -
- Status: Open
- Priority: High
- Assignee: 沼澤祐介
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-846
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-846
Assignee: 沼澤祐介
Priority: High
Status (source): Open
Due: 2026-04-06T00:00:00Z

Original Description:
■サマリー
R6補正グローバルサウス補助金 交付申請内容の不備修正・再申請

■詳細
送信者: R6補正GS補助金（小規模実証等）事務局
件名: 【R6補正グローバルサウス未来志向型共創等事業費補助金（小規模実証等）】交付申請内容の不備・確認事項
日時: 2026/04/03 16:25
内容: 申請内容に不備あり。不備内容を確認し速やかに修正および申請を行うよう指示。
```

## 50. SusHiTech成長加速プログラム フィードバック面談の日程調整・返信

- Backlog Key: EP_ALL_PJT-845
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-845
- Source Issue ID: 8149112
- Parent Issue ID: 8097178
- Status: Open
- Priority: Normal
- Assignee: 沼澤祐介
- Due: 2026-04-06T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-845
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-845
Assignee: 沼澤祐介
Priority: Normal
Status (source): Open
Due: 2026-04-06T00:00:00Z

Original Description:
■サマリー
SusHiTech成長加速プログラム フィードバック面談の日程調整・返信

■詳細
送信者: 濱田直樹 (SusHi Tech Global事務局ガイドメンター / デロイト)
件名: 【ご案内】成長加速プログラムのフィードバック面談について
日時: 2026/04/03 20:17
内容: 3/19に成長加速プログラム運営事務局よりご案内のあった審査結果を踏まえたブラッシュアップ面談の実施希望確認。アジェンダ①審査結果伝達、②今後の支援プログラム等。希望する場合は返信が必要。
```

## 51. 第3ロット 出荷予測（Ver2）の振り返りと精度検証

- Backlog Key: SBIR_PJT-1184
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1184
- Source Issue ID: 8100935
- Parent Issue ID: 8097274
- Status: In Progress
- Priority: Normal
- Assignee: 東間千芽
- Due: 2026-04-03T00:00:00Z

```text
Backlog Key: SBIR_PJT-1184
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1184
Assignee: 東間千芽
Priority: Normal
Status (source): In Progress
Due: 2026-04-03T00:00:00Z

Original Description:
## 概要
- Ver2の計算式をAIにより自動化して実施した第3ロットの出荷予測について、精度を振り返る（計画タイミング：96日齢時点）。
- 精度を確認：残渣（体重・日数）、σ、外れ値除去の様子など
- Ver2の再現性があるか、ロットごとの増体傾向が予測精度に与える影響
- 【追加】DG決め打ちとの精度比較・豚群単位のロス推計・仮説ベースの改善試算

## 完了条件

## 検討履歴
コメント記載
```

## 52. レンズ汚れ判定障害物検知実装

- Backlog Key: PDSB-442
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-442
- Source Issue ID: 8093527
- Parent Issue ID: 8126942
- Status: In Progress
- Priority: Normal
- Assignee: 奥野資司
- Due: 2026-04-03T00:00:00Z

```text
Backlog Key: PDSB-442
Backlog URL: https://eco-pork.backlog.com/view/PDSB-442
Assignee: 奥野資司
Priority: Normal
Status (source): In Progress
Due: 2026-04-03T00:00:00Z

Original Description:
### 概要
ロジックは@Li Yachao さんが対応中
仕様確定後cpp化しTypeBへの組み込み実装をおこなう

関連タスク：
PDS_TB_PROT-213 カメラ異常検知（良品学習）の手法検討

* pythonコードのcpp化
* 組み込むための仕様決め
* 実装
* テスト
```

## 53. アノテーション作業

- Backlog Key: AIGEN2024-468
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-468
- Source Issue ID: 7915589
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: 遠藤麻佑子
- Due: -

```text
Backlog Key: AIGEN2024-468
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-468
Assignee: 遠藤麻佑子
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
アノテーション作業が開発のボトルネックになっているため、
アノテーション作業、最終的にアルバイトさんのレビューができるようにする。
```

## 54. 3Dスキャナのセットアップとスキャンテストまでの実施

- Backlog Key: AIGEN2024-499
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-499
- Source Issue ID: 8140107
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: 遠藤麻佑子
- Due: -

```text
Backlog Key: AIGEN2024-499
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-499
Assignee: 遠藤麻佑子
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
計測作業に向けて、3Dスキャナ「FARO Orbis Premium」のセットアップを行う。
ハードウェアの設置・接続、専用ソフトウェアのインストール・ライセンス認証、動作確認（テストスキャンの実施）までを完了させる。
```

## 55. 【上原ファーム】3月分データ提供

- Backlog Key: EP_ALL_PJT-844
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-844
- Source Issue ID: 8147860
- Parent Issue ID: 6535780
- Status: Open
- Priority: Normal
- Assignee: あらふか
- Due: 2026-04-05T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-844
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-844
Assignee: あらふか
Priority: Normal
Status (source): Open
Due: 2026-04-05T00:00:00Z

Original Description:
- [ ] 繁殖データ
- [ ] 肥育データ

※ 2026/4/3 上原ファーム西川様よりメールにて3月分繁殖データ集計依頼あり
```

## 56. 【JF PDS-B実証プロジェクト情報共有】JF Japan Farmと4月末の現調スケジュールを調整し参加者4名枠を確保する

- Backlog Key: PDSB-458
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-458
- Source Issue ID: 8121998
- Parent Issue ID: 7612365
- Status: In Progress
- Priority: Normal
- Assignee: 中島　賢司
- Due: 2026-04-17T00:00:00Z

```text
Backlog Key: PDSB-458
Backlog URL: https://eco-pork.backlog.com/view/PDSB-458
Assignee: 中島　賢司
Priority: Normal
Status (source): In Progress
Due: 2026-04-17T00:00:00Z

Original Description:
## 目的
施工計画策定に向けた機器設置場所の最終確認と業者への引き渡し準備のため。

## 背景・経緯
中島から現在18-21〜30棟で出荷中であり6週間で完了すると次の空舎期間（4月中旬）が来るという情報が共有された。4月中旬の空舎では施工タイミングが間に合わないため施工は7月下旬〜8月中旬を目標とし、4月末に現調を設定することで合意した。田中は現調に宮崎・新ジョインメンバーも同行を希望し、中島は4名程度で調整すると応答した。栗田からバイオセキュリティの厳しさ（温泉入浴・着替え・シャワーの事前プロセスが必須で最低2日間スケジュールが必要）の補足があり全員が認識を合わせた。

**結論:** 中島が4月末を目標にJFと現調スケジュールを調整。田中・宮崎・新ジョインメンバー計4名参加予定。
（2026-03-26 JF PDS-B実証プロジェクト情報共有 にて決定）

## 前提条件
田中・宮崎・新ジョインメンバーのスケジュール確認が必要

## 完了要件
JFとの日程合意・4名参加確定・業者も含めた現調日程が確定していること

## 関連情報
- 会議: JF PDS-B実証プロジェクト情報共有（2026-03-26）
- テーマ: テーマ① 現地調査スケジュール
```

## 57. コミュニティ運営

- Backlog Key: EP_ALL_PJT-833
- Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-833
- Source Issue ID: 8135725
- Parent Issue ID: 8132333
- Status: In Progress
- Priority: Normal
- Assignee: 本多洋子
- Due: 2026-04-08T00:00:00Z

```text
Backlog Key: EP_ALL_PJT-833
Backlog URL: https://eco-pork.backlog.com/view/EP_ALL_PJT-833
Assignee: 本多洋子
Priority: Normal
Status (source): In Progress
Due: 2026-04-08T00:00:00Z

Original Description:
スケジュール

1
	第1回セミナーのテーマ・告知文・アンケート確定
	鈴木→本多
	4月第1週

2
	運営自動化パイプライン構築
	Claude
	4月第1週

3
	広報業務の移管先確定
	鈴木
	4月第1週

4
	荒深・中島・佐藤にテーマ別分担共有
	鈴木
	4月第1週

5
	Slack（外部向け）開設準備
	本多
	5月第1週
```

## 58. Final testing/inspection checklist

- Backlog Key: US_PDS-423
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-423
- Source Issue ID: 8147454
- Parent Issue ID: 8124988
- Status: Open
- Priority: Normal
- Assignee: Saeki Kurita
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: US_PDS-423
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-423
Assignee: Saeki Kurita
Priority: Normal
Status (source): Open
Due: 2026-04-10T00:00:00Z

Original Description:
(no description)
```

## 59. Establish Documentation Review Process

- Backlog Key: US_PDS-422
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-422
- Source Issue ID: 8147451
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Daichi Takamatsu
- Due: 2026-04-07T00:00:00Z

```text
Backlog Key: US_PDS-422
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-422
Assignee: Daichi Takamatsu
Priority: Normal
Status (source): In Progress
Due: 2026-04-07T00:00:00Z

Original Description:
(no description)
```

## 60. List up what else need to be tested during the install

- Backlog Key: US_PDS-416
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-416
- Source Issue ID: 8134921
- Parent Issue ID: 8124988
- Status: In Progress
- Priority: Normal
- Assignee: Saeki Kurita
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: US_PDS-416
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-416
Assignee: Saeki Kurita
Priority: Normal
Status (source): In Progress
Due: 2026-04-10T00:00:00Z

Original Description:
(no description)
```

## 61. Create procedure on how to setup VPN router

- Backlog Key: US_PDS-413
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-413
- Source Issue ID: 8134912
- Parent Issue ID: 8124988
- Status: In Progress
- Priority: Normal
- Assignee: Saeki Kurita
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: US_PDS-413
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-413
Assignee: Saeki Kurita
Priority: Normal
Status (source): In Progress
Due: 2026-04-10T00:00:00Z

Original Description:
(no description)
```

## 62. Setup/Testing Procedure for EP onsite member

- Backlog Key: US_PDS-399
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-399
- Source Issue ID: 8124988
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Saeki Kurita
- Due: 2026-04-14T00:00:00Z

```text
Backlog Key: US_PDS-399
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-399
Assignee: Saeki Kurita
Priority: Normal
Status (source): In Progress
Due: 2026-04-14T00:00:00Z

Original Description:
(no description)
```

## 63. Trip prep

- Backlog Key: US_PDS-408
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-408
- Source Issue ID: 8125177
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Daichi Takamatsu
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: US_PDS-408
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-408
Assignee: Daichi Takamatsu
Priority: Normal
Status (source): In Progress
Due: 2026-04-10T00:00:00Z

Original Description:
(no description)
```

## 64. Test VPN router

- Backlog Key: US_PDS-418
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-418
- Source Issue ID: 8134934
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Henry Liu
- Due: 2026-04-17T00:00:00Z

```text
Backlog Key: US_PDS-418
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-418
Assignee: Henry Liu
Priority: Normal
Status (source): In Progress
Due: 2026-04-17T00:00:00Z

Original Description:
(no description)
```

## 65. Installation (target)

- Backlog Key: US_PDS-395
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-395
- Source Issue ID: 8124950
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: -
- Due: 2026-04-23T00:00:00Z

```text
Backlog Key: US_PDS-395
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-395
Assignee: -
Priority: Normal
Status (source): Open
Due: 2026-04-23T00:00:00Z

Original Description:
(no description)
```

## 66. CVATへ姿勢情報の一括反映

- Backlog Key: PDS_TB_PROT-247
- Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-247
- Source Issue ID: 8143249
- Parent Issue ID: 7977537
- Status: Open
- Priority: Normal
- Assignee: Batnasan Baasanchuluun
- Due: -

```text
Backlog Key: PDS_TB_PROT-247
Backlog URL: https://eco-pork.backlog.com/view/PDS_TB_PROT-247
Assignee: Batnasan Baasanchuluun
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要
TypeBのアノテーションデータへ姿勢情報を一括反映させる

### 完了条件
反映完了する
```

## 67. 第一段階終了したデータセットの体重推計対象豚の一括ロック処理

- Backlog Key: PDSB-473
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-473
- Source Issue ID: 8129886
- Parent Issue ID: 7664819
- Status: In Progress
- Priority: Normal
- Assignee: Li Yachao
- Due: -

```text
Backlog Key: PDSB-473
Backlog URL: https://eco-pork.backlog.com/view/PDSB-473
Assignee: Li Yachao
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
(no description)
```

## 68. 人認識（or 頭部）モデル学習

- Backlog Key: TA2025GUI-422
- Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-422
- Source Issue ID: 8147146
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: Li Yachao
- Due: -

```text
Backlog Key: TA2025GUI-422
Backlog URL: https://eco-pork.backlog.com/view/TA2025GUI-422
Assignee: Li Yachao
Priority: Normal
Status (source): Open
Due: -

Original Description:
### 概要

* 軽量モデルでbboxを予測する
* bbox内にblurをかけることを想定している
* 動画書き出しの時に使うのでFPSは30以上を目指したい
* 実行環境はJetson Orin NX 16G


使用するデータ：
`pigcounter_xxx`を取得し、カラーを学習させる
```

## 69. 色ラベルの色について

- Backlog Key: PDSB-480
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-480
- Source Issue ID: 8140435
- Parent Issue ID: 7664819
- Status: Open
- Priority: Normal
- Assignee: 影澤
- Due: -

```text
Backlog Key: PDSB-480
Backlog URL: https://eco-pork.backlog.com/view/PDSB-480
Assignee: 影澤
Priority: Normal
Status (source): Open
Due: -

Original Description:
色が暗い場合、ロックの状態やその他の文字が見にくくなるため、次回登録時からは明るい色にしていただきたいです。
![image][pasted-2026.04.01-15.58.52.png]
![image][pasted-2026.04.01-15.59.13.png]
```

## 70. 室蘭／土地検討

- Backlog Key: SBIR_PJT-1194
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1194
- Source Issue ID: 8146183
- Parent Issue ID: 8098176
- Status: In Progress
- Priority: Normal
- Assignee: 武　祐紀
- Due: 2026-04-30T00:00:00Z

```text
Backlog Key: SBIR_PJT-1194
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1194
Assignee: 武　祐紀
Priority: Normal
Status (source): In Progress
Due: 2026-04-30T00:00:00Z

Original Description:
目標
4月中に土地確定（※期日は要調整）

候補地
G:\共有ドライブ\★Eco-Pork_全体\05_プロダクト部\04_プロジェクト\02_SBIR\営業関連\日鉄興和不動産農業／室蘭\土地

MUST
・用途地域：市街化調整区域or指定なし（畜舎特例法が使えるので）
・1.5ha以上
・大型通行可

HIGH WANT（ほぼMUST？）
・放流できる河川の近く
・住宅や周辺施設から距離が離れている

WANT
・白地
・と畜場やその他施設との距離、インフラが良い
・積雪が少ない／市による除雪がきちんとされている
```

## 71. 第3ロットデータの各個体のデータのプロットと、第2ロットのデータとの比較

- Backlog Key: SBIR_PJT-1183
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1183
- Source Issue ID: 8100934
- Parent Issue ID: 8097274
- Status: In Progress
- Priority: High
- Assignee: 中村　悠利菜
- Due: 2026-04-10T00:00:00Z

```text
Backlog Key: SBIR_PJT-1183
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1183
Assignee: 中村　悠利菜
Priority: High
Status (source): In Progress
Due: 2026-04-10T00:00:00Z

Original Description:
## 概要

## 目的

## 完了条件

## 検討履歴
コメント記載

## 残論点
* [ ]
```

## 72. 豚房を対象とする場合の課題洗い出しとスケジュールの検討

- Backlog Key: DEV_WE3D-34
- Backlog URL: https://eco-pork.backlog.com/view/DEV_WE3D-34
- Source Issue ID: 7846801
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Li Yachao
- Due: 2026-01-06T00:00:00Z

```text
Backlog Key: DEV_WE3D-34
Backlog URL: https://eco-pork.backlog.com/view/DEV_WE3D-34
Assignee: Li Yachao
Priority: Normal
Status (source): In Progress
Due: 2026-01-06T00:00:00Z

Original Description:
(no description)
```

## 73. Coordination with Andy

- Backlog Key: US_PDS-404
- Backlog URL: https://eco-pork.backlog.com/view/US_PDS-404
- Source Issue ID: 8124999
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Ernesto Estrada
- Due: 2026-04-03T00:00:00Z

```text
Backlog Key: US_PDS-404
Backlog URL: https://eco-pork.backlog.com/view/US_PDS-404
Assignee: Ernesto Estrada
Priority: Normal
Status (source): In Progress
Due: 2026-04-03T00:00:00Z

Original Description:
(no description)
```

## 74. 日鉄興和不動産農業／室蘭PJ

- Backlog Key: SBIR_PJT-1181
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1181
- Source Issue ID: 8098176
- Parent Issue ID: -
- Status: In Progress
- Priority: High
- Assignee: 武　祐紀
- Due: 2026-07-31T00:00:00Z

```text
Backlog Key: SBIR_PJT-1181
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1181
Assignee: 武　祐紀
Priority: High
Status (source): In Progress
Due: 2026-07-31T00:00:00Z

Original Description:
日鉄興和不動産農業の案件管理

各種資料
G:\共有ドライブ\★Eco-Pork_全体\05_プロダクト部\04_プロジェクト\02_SBIR\営業関連\日鉄興和不動産農業／室蘭

これまでの議事録
・https://docs.google.com/document/d/1I92fQNo28Bs5LW6z5DEERRbKn6b0DmN6XIOoTIhWxro/edit?tab=t.54hsdy8yaycy
・https://docs.google.com/document/d/1fAlN_KVmg8w9YxoRZ0_Vi9w3qI-KRtobJzndiWRcZbI/edit?tab=t.0
・https://docs.google.com/document/d/1VmW-WMfwghHP7IvwdiXjb04Zpx2Xycc7lu73Rr_axkI/edit?tab=t.7gfuuwsxiell
```

## 75. Engine配布スクリプト作成

- Backlog Key: PDSB-408
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-408
- Source Issue ID: 8015960
- Parent Issue ID: -
- Status: In Progress
- Priority: High
- Assignee: 奥野資司
- Due: 2026-03-30T00:00:00Z

```text
Backlog Key: PDSB-408
Backlog URL: https://eco-pork.backlog.com/view/PDSB-408
Assignee: 奥野資司
Priority: High
Status (source): In Progress
Due: 2026-03-30T00:00:00Z

Original Description:
## 概要
Engine配信機能実装完了までの間に使用する、Engine手動配布スクリプトの追加
```

## 76. オーバーレイかかっていない端末の対応方法を決める

- Backlog Key: PDSB-483
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-483
- Source Issue ID: 8146345
- Parent Issue ID: -
- Status: Open
- Priority: Normal
- Assignee: 田中寛樹
- Due: 2026-04-03T00:00:00Z

```text
Backlog Key: PDSB-483
Backlog URL: https://eco-pork.backlog.com/view/PDSB-483
Assignee: 田中寛樹
Priority: Normal
Status (source): Open
Due: 2026-04-03T00:00:00Z

Original Description:
本番機および撮影専用機でオーバーレイかかっていない端末が残っているため、どのように対応するか検討する。

* リモートで設定（安全のためにはできるだけ避けた方が良い？）
* 現地で設定
* 社内でセットアップ動作確認したものと入れ替え
```

## 77. [データセット]作成&アノテーション

- Backlog Key: PDSB-127
- Backlog URL: https://eco-pork.backlog.com/view/PDSB-127
- Source Issue ID: 7664819
- Parent Issue ID: -
- Status: In Progress
- Priority: High
- Assignee: Terada Misaki
- Due: 2025-12-24T00:00:00Z

```text
Backlog Key: PDSB-127
Backlog URL: https://eco-pork.backlog.com/view/PDSB-127
Assignee: Terada Misaki
Priority: High
Status (source): In Progress
Due: 2025-12-24T00:00:00Z

Original Description:
TypeB用データセットを作成する。

アノテーションルール

フィッシュアイ（補正前の生データ）に対してアノテーションする
対象は全ての豚かつ不完全な豚も全てアノテーションして頭数が正しくなるようにする

TypeB用のデータセット管理表
https://docs.google.com/spreadsheets/d/161EnNAZE2xQgagPOb7SwYkwEJu2uDjsXfNBAYn_EFiI/edit?gid=0#gid=0
```

## 78. LCD液晶パネルの新モデルのデータ確認

- Backlog Key: ABC_T3_PROT-291
- Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-291
- Source Issue ID: 7749116
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Saeki Kurita
- Due: 2026-02-27T00:00:00Z

```text
Backlog Key: ABC_T3_PROT-291
Backlog URL: https://eco-pork.backlog.com/view/ABC_T3_PROT-291
Assignee: Saeki Kurita
Priority: Normal
Status (source): In Progress
Due: 2026-02-27T00:00:00Z

Original Description:
### LCD液晶パネルの新モデル

現行版（ABC-TypeA_prod_20250829 v16）と新モデルのデータをPDS typeAのassemblyファイルに入れて比較する。
* 新モデルへの仕様変更
* 現行モデルへの設変
が必要な点を列挙し、液晶側の仕様変更についてデンシトロン側と共有することで検収とする。

## 元の課題
PROD-57 LCD液晶パネルの新モデルのデータ確認
```

## 79. RTX Pro 6000セットアップ

- Backlog Key: AIGEN2024-498
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-498
- Source Issue ID: 8134850
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Batnasan Baasanchuluun
- Due: -

```text
Backlog Key: AIGEN2024-498
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-498
Assignee: Batnasan Baasanchuluun
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 完了条件
RTX Pro 6000セットアップ完了
```

## 80. 室蘭／法令確認

- Backlog Key: SBIR_PJT-1195
- Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1195
- Source Issue ID: 8146208
- Parent Issue ID: 8098176
- Status: In Progress
- Priority: Normal
- Assignee: 武　祐紀
- Due: 2026-04-30T00:00:00Z

```text
Backlog Key: SBIR_PJT-1195
Backlog URL: https://eco-pork.backlog.com/view/SBIR_PJT-1195
Assignee: 武　祐紀
Priority: Normal
Status (source): In Progress
Due: 2026-04-30T00:00:00Z

Original Description:
目標
不動産ビジネススキームを実現するためにクリアしなければいけない法令を把握

関連法令
メイン
・農地法
・農業振興地域の整備に関する法律（農振法）
・農業経営基盤強化促進法

サブ
・不動産登記法
・都市計画法
・建築基準法
・土地改良法

とりあえず全部入れたNotebookLM
https://notebooklm.google.com/notebook/46e14495-c28e-4baa-971f-4247fe47daf2
```

## 81. TypeAアプリ開発 マイルストーン未設定

- Backlog Key: AIGEN2024-348
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-348
- Source Issue ID: 7573616
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Katushiro Miyazaki
- Due: -

```text
Backlog Key: AIGEN2024-348
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-348
Assignee: Katushiro Miyazaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要


### 完了条件
```

## 82. TypeB - WEBフロントエンド・バックエンド実装

- Backlog Key: AIGEN2024-366
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-366
- Source Issue ID: 7595105
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: 西村 堅太郎
- Due: -

```text
Backlog Key: AIGEN2024-366
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-366
Assignee: 西村 堅太郎
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
TypeB - フロントエンド実装

### 完了条件
---
```

## 83. アノテーション作業

- Backlog Key: AIGEN2024-218
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-218
- Source Issue ID: 7094239
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Terada Misaki
- Due: -

```text
Backlog Key: AIGEN2024-218
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-218
Assignee: Terada Misaki
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要
自身のアノテーション作業の進捗状況
アノテーターさんの作業進捗状況の共有

[アノテーション作業状況整理（スプレッドシート）](https://docs.google.com/spreadsheets/d/1TLu8TVMAh2LI_fxfxVGLLH39qxkWbzElLx0Gmr171M0/edit?gid=259298860#gid=259298860)
CVAT ： アノテーション作業状況
アノテーター管理 ： 契約状況
```

## 84. Tailscale Flow Monitor（通信活動監視ツール）の開発

- Backlog Key: AIGEN2024-502
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-502
- Source Issue ID: 8146173
- Parent Issue ID: 8142713
- Status: Open
- Priority: Normal
- Assignee: 田中寛樹
- Due: -

```text
Backlog Key: AIGEN2024-502
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-502
Assignee: 田中寛樹
Priority: Normal
Status (source): Open
Due: -

Original Description:
## 概要

Tailscale Network Flow Logsを定期取得・保存し、通信活動監視と通信途絶の原因調査を行うWebアプリケーション。

- AIGEN2024-500（デバイス命名規則策定）と並行して開発
- 命名規則確定後にカテゴリ推定ルールを更新

## 機能

- **ログ永続保存**: Tailscale APIから15分間隔で取得しSQLiteに保存（詳細ログ1年、以降は日次集計）
- **通信活動監視**: 選択したデバイスの通信活動を監視し、途絶時にSlack通知
- **ダッシュボード**: ノード一覧・ステータス（Online/Warning/Offline）・アラート表示
- **ノード詳細**: 時系列トラフィックグラフ、通信相手一覧、フローログ閲覧
- **通信分析**: 異常検出（RX=0、片方向通信、トラフィック急減）、ノードペア比較
- **フローマップ**: Sankey Diagramによるノード間通信フロー可視化

## 技術スタック

Node.js + Express + SQLite (better-sqlite3) / Alpine.js + Chart.js / Nothing Design System（ダークモード）

## 現在の状態

- 実装完了、htanaka-z100 (100.76.126.72:3000) で稼働中
- 30日分のバックフィル完了（DB: ~235MB、139ノード）

## 残タスク

- [ ] AIGEN2024-500の命名規則確定後、カテゴリ推定ルールを更新
- [ ] pm2での永続化設定
- [ ] Slack Webhook URLの設定・通知テスト
- [ ] 運用ドキュメント整備

## 関連

- サーバー: htanaka-z100:~/tailscale-flow-monitor
- URL: http://100.76.126.72:3000
```

## 85. M&W設置

- Backlog Key: AIGEN2024-481
- Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-481
- Source Issue ID: 7985691
- Parent Issue ID: -
- Status: In Progress
- Priority: Normal
- Assignee: Saeki Kurita
- Due: -

```text
Backlog Key: AIGEN2024-481
Backlog URL: https://eco-pork.backlog.com/view/AIGEN2024-481
Assignee: Saeki Kurita
Priority: Normal
Status (source): In Progress
Due: -

Original Description:
### 概要

M&W農場にtypeBを設置する

### 完了条件

検収し、NVRに映像が保存されていることを確認する
```

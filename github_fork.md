## 請問github的fork要怎麼用?

# GitHub 的「Fork」功能詳解

GitHub 的 **"Fork"** 功能，中文常翻譯為「分支」或「派生」，是 GitHub 上一個非常核心且強大的協作方式。它允許您將一個公開的專案（Repository）完整複製到您自己的 GitHub 帳戶下，形成一個獨立的副本。這個副本與原專案是分開的，您可以自由地在您的 Forked Repository 中進行任何修改，而不會影響到原始專案。

---

## 為什麼要使用 Fork？

Fork 主要有以下幾個常見用途：

* **參與開源專案貢獻**：這是 Fork 最主要的應用場景。當您想要為一個您不擁有寫入權限的開源專案提交修改、修復 Bug 或新增功能時，您需要先 Fork 這個專案。在您的 Fork 中完成開發後，您可以透過 **Pull Request (PR)** 的方式，將您的修改建議發送給原始專案的維護者，讓他們審查並決定是否合併到主專案中。
* **個人實驗與修改**：您可以 Fork 任何您感興趣的專案，然後在您的副本中進行實驗、學習或根據自己的需求進行客製化修改，而不用擔心會影響到原始專案。
* **從現有專案基礎建立新專案**：如果您想基於一個現有的專案開始一個全新的專案，但又不希望未來與原始專案同步更新，您可以 Fork 它，然後將其視為自己專案的起點。

---

## GitHub Fork 的基本流程

使用 Fork 的標準流程通常包含以下幾個步驟：

### 1. Fork 原始儲存庫

* **目的**：在您的 GitHub 帳戶下創建原始專案的獨立副本。
* **操作**：
    1.  在 GitHub 上瀏覽到您想要 Fork 的原始儲存庫頁面。
    2.  在頁面右上角，您會看到一個 **"Fork"** 按鈕。點擊它。
    3.  GitHub 會提示您選擇 Fork 到哪個帳戶（如果是個人帳戶通常直接顯示您的帳號），確認後，GitHub 會自動幫您建立一個新的儲存庫，其內容與原始儲存庫完全相同。
    4.  完成後，您將被重新導向到您自己的 Forked Repository 頁面，網址會變成 `https://github.com/您的用戶名/專案名`。

### 2. 將 Forked Repository 克隆到本地

* **目的**：將您 GitHub 帳戶中的 Forked Repository 下載到您的本地電腦，以便進行開發。
* **操作**：
    1.  在您 Forked Repository 的 GitHub 頁面，點擊綠色的 **"< > Code"** 按鈕。
    2.  複製 HTTPS 或 SSH 的 URL。
    3.  開啟您的終端機 (Terminal) 或命令提示字元 (Command Prompt)，並導航到您想要存放專案的資料夾。
    4.  執行 `git clone [您複製的URL]` 命令。例如：
        ```bash
        git clone [https://github.com/您的用戶名/專案名.git](https://github.com/您的用戶名/專案名.git)
        ```

### 3. 設定原始儲存庫為 "upstream" 遠端

* **目的**：這一步非常重要，它讓您能夠追蹤原始專案的更新，並將其同步到您的 Fork 中。
* **操作**：
    1.  進入您剛剛克隆到本地的專案資料夾：
        ```bash
        cd 專案名
        ```
    2.  添加一個新的遠端儲存庫，通常命名為 `upstream`，指向原始專案的 URL。執行：
        ```bash
        git remote add upstream [原始專案的URL]
        ```
        例如：
        ```bash
        git remote add upstream [https://github.com/原始專案擁有者/原始專案名.git](https://github.com/原始專案擁有者/原始專案名.git)
        ```
    3.  您可以執行 `git remote -v` 來驗證是否成功添加了 `origin`（您的 Fork）和 `upstream`（原始專案）。

### 4. 在本地進行修改並提交

* **目的**：在您的 Forked Repository 的本地副本中進行程式碼修改、新增檔案、修復 Bug 等操作。
* **操作**：
    1.  在您本地的專案中進行所需的修改。
    2.  使用 Git 命令提交您的更改：
        ```bash
        git add .        # 將所有修改的檔案加入暫存區
        git commit -m "您的提交訊息" # 提交更改並附上說明
        ```

### 5. 推送更改到您的 Forked Repository

* **目的**：將您在本地所做的更改推送到您 GitHub 上的 Forked Repository。
* **操作**：
    ```bash
    git push origin [您的分支名稱] # 通常是 main 或 master
    ```
    例如：
    ```bash
    git push origin main
    ```

### 6. 建立 Pull Request (PR)

* **目的**：向原始專案的維護者提出修改建議，請求他們將您的更改合併到原始專案中。
* **操作**：
    1.  回到您 GitHub 上的 Forked Repository 頁面。
    2.  GitHub 會自動檢測到您的分支比原始專案有新的提交，並在頁面頂部或中間顯示一個 **"Contribute"** 按鈕或 **"Pull request"** 提示。
    3.  點擊該按鈕，然後點擊 **"Open pull request"** 或 **"Create pull request"**。
    4.  撰寫詳細的 Pull Request 說明，解釋您所做的更改、原因以及任何相關的資訊。
    5.  確認目標分支是原始專案的主分支（通常是 `main` 或 `master`），來源分支是您的 Fork 中的分支。
    6.  點擊 **"Create pull request"**。

---

## 如何同步您的 Fork 與原始專案的最新變更？

由於原始專案可能會持續更新，您的 Fork 很快就會過時。為了確保您的 Fork 保持最新狀態，您需要定期同步：

1.  確保您在您的 Fork 的主分支上：
    ```bash
    git checkout main # 或 master
    ```
2.  從原始專案 (upstream) 抓取最新的變更：
    ```bash
    git fetch upstream
    ```
3.  將抓取到的變更合併到您的本地分支：
    ```bash
    git merge upstream/main # 或 upstream/master
    ```
4.  將更新推送到您的 Forked Repository：
    ```bash
    git push origin main # 或 origin master
    ```

---

## Fork vs. Branch

這兩個概念經常被混淆，但它們有著本質上的不同：

* **Fork (分支/派生)**：是整個儲存庫的 **獨立副本**，通常在 **不同的 GitHub 帳戶之間** 進行。您的 Fork 可以擁有自己的協作者、問題追蹤等等，與原始儲存庫是相互獨立的。主要用於您不擁有原始專案寫入權限，但想貢獻或基於此專案開發的情況。
* **Branch (分支)**：是同一個儲存庫中的 **不同開發線**。多個 Branch 存在於 **同一個儲存庫內**。它主要用於在不影響主程式碼的情況下進行新功能開發或 Bug 修復，完成後可以合併回主分支。您通常對自己的儲存庫創建 Branch。

希望這份詳細的說明能幫助您理解並使用 GitHub 的 Fork 功能！如果您有任何更具體的問題，歡迎隨時提出。
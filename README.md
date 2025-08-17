# 复旦大学新版教务系统课表解析工具

由于新版教务系统上线，WakeUp 课表原有的自动导入功能已不可用。本工具实现解析新版教务系统的 JSON 数据，并将其转换为 WakeUp 课表所需的 CSV 格式的逻辑。

    ⚠️ 本工具仅负责数据格式转换。请用户自行登录教务系统获取原始 JSON 数据，并手动导入生成的 CSV 文件至 WakeUp 课表。

## 使用说明

### 1. 获取课表 JSON 数据

1. 登录新版教务系统，进入个人课表页面。
2. 打开浏览器开发者工具（快捷键 F12），切换到“网络（Network）”面板。
3. 查找类似 `getLesson?semesterId=<semesterId>&studentId=<studentId>` 的请求，复制其响应内容（JSON 数据）。
4. 将该 JSON 数据保存为项目根目录下的 `data.json` 文件。

### 2. 安装依赖

    ```bash
    pip install pandas
    ```

### 3. 运行脚本

    ```bash
    python main.py
    ```

脚本运行结束后，会在当前目录生成 `output.csv` 文件。

### 4. 导入 WakeUp 课表

1. 打开 WakeUp 课表 App。
2. 选择“从 Excel 模板导入”功能。
3. 上传刚刚生成的 `output.csv` 文件，完成课表导入。

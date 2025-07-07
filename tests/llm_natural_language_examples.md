
# LLM 自然语言调用工具示例

本文档提供了可用于调用语言模型（LLM）工具的自然语言提示示例。

## 音频工具 (Audio Tools)

---

### 1. `create_audio_by_tts_tool`

**工具调用:**
```python
create_audio_by_tts_tool(
    text="你好，我是飞影数字人，很高兴认识你。",
    voice="ZlOFcVt9CmXCFHwV8wvKUA",
    title="测试音频"
)
```

**自然语言示例:**
> "帮我用文字生成一段音频，内容是'你好，我是飞影数字人，很高兴认识你。'，声音用'ZlOFcVt9CmXCFHwV8wvKUA'，标题是'测试音频'。"

---

### 2. `query_audio_task_tool`

**工具调用:**
```python
query_audio_task_tool(
    task_id="jeaDl3YtFLR3uO2nuiAz1A"
)
```

**自然语言示例:**
> "查询一下ID为'jeaDl3YtFLR3uO2nuiAz1A'的音频生成任务的状态。"

---

## 数字人工具 (Avatar Tools)

---

### 1. `create_avatar_by_video_tool`

**工具调用:**
```python
create_avatar_by_video_tool(
    title="测试数字人123",
    video_url="https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/converted_media/fa6bd8c5-850f-4728-b681-3bb41e41f76c.mp4"
)
```

**自然语言示例:**
> "用这个视频创建一个数字人形象，标题是'测试数字人123'，视频地址是'https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/converted_media/fa6bd8c5-850f-4728-b681-3bb41e41f76c.mp4'。"

---

### 2. `create_avatar_by_image_tool`

**工具调用:**
```python
create_avatar_by_image_tool(
    title="测试数字人图片上传",
    image_url="https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/static/uploads/preview_c970a538565911f0a7a200163e7f9c5a.mp4.jpg"
)
```

**自然语言示例:**
> "我想用这张图片创建一个数字人，标题叫'测试数字人图片上传'，图片地址是'https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/static/uploads/preview_c970a538565911f0a7a200163e7f9c5a.mp4.jpg'。"

---

### 3. `query_avatar_task_tool`

**工具调用:**
```python
query_avatar_task_tool(
    task_id="mGZ9eqUcFfqmnf3i"
)
```

**自然语言示例:**
> "帮我查一下这个数字人任务的进度，ID是'mGZ9eqUcFfqmnf3i'。"

---

## 视频工具 (Video Tools)

---

### 1. `create_video_by_audio_tool`

**工具调用:**
```python
create_video_by_audio_tool(
    avatar="0ezhDusZR1FI9Qi042MTrg",
    audio_url="https://hfcdn.lingverse.co/39903f565d0a8aa3745e9b5d99c6dfa1/6865577F/hf/local/1000020056/audios/38c97451-15e5-4e7c-a17b-2d8134df219b.wav",
    title="音频驱动视频测试"
)
```

**自然语言示例:**
> "用这个音频'https://hfcdn.lingverse.co/39903f565d0a8aa3745e9b5d99c6dfa1/6865577F/hf/local/1000020056/audios/38c97451-15e5-4e7c-a17b-2d8134df219b.wav'和数字人'0ezhDusZR1FI9Qi042MTrg'来生成一个视频，标题是'音频驱动视频测试'。"

---

### 2. `create_video_by_tts_tool`

**工具调用:**
```python
create_video_by_tts_tool(
    avatar="0ezhDusZR1FI9Qi042MTrg",
    voice="iLafe9ZZZrjgiCulLLTXNw",
    text="这是一个测试视频，用于测试文本驱动视频创建功能。",
    title="文本驱动视频测试",
    st_show=1
)
```

**自然语言示例:**
> "请用文字'这是一个测试视频，用于测试文本驱动视频创建功能。'，数字人'0ezhDusZR1FI9Qi042MTrg'和声音'iLafe9ZZZrjgiCulLLTXNw'创建一个带字幕的视频，标题是'文本驱动视频测试'。"

---

### 3. `query_video_task_tool`

**工具调用:**
```python
query_video_task_tool(
    task_id="9fV1PigNwIBQ_qRplYl7Lw"
)
```

**自然语言示例:**
> "查询一下ID为'9fV1PigNwIBQ_qRplYl7Lw'的视频任务状态。"

---

## 声音工具 (Voice Tools)

---

### 1. `create_voice_tool`

**工具调用:**
```python
create_voice_tool(
    title="测试声音克隆",
    voice_type=8,
    audio_url="https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/static/uploads/e26794fe7e1c11efb9a600163e48bee7.wav"
)
```

**自然语言示例:**
> "帮我克隆一个声音，标题是'测试声音克隆'，声音类型是8，用这个音频'https://wechat-luobo.oss-cn-shanghai.aliyuncs.com/static/uploads/e26794fe7e1c11efb9a600163e48bee7.wav'。"

---

### 2. `query_voice_task_tool`

**工具调用:**
```python
query_voice_task_tool(
    task_id="IQwWBZARey1TfTC9kCcdvw"
)
```

**自然语言示例:**
> "查询一下声音克隆任务'IQwWBZARey1TfTC9kCcdvw'的状态。"

---

### 3. `edit_voice_tool`

**工具调用:**
```python
edit_voice_tool(
    voice_id="your_voice_id",
    rate="1.2",
    volume="1.1",
    pitch="0.9"
)
```

**自然语言示例:**
> "把声音'your_voice_id'的语速调到1.2，音量调到1.1，音高调到0.9。"

---

### 4. `list_voices_tool`

**工具调用:**
```python
list_voices_tool(
    page=1,
    size=10,
    kind=2
)
```

**自然语言示例:**
> "帮我看看我自己克隆的声音有哪些，给我看第一页，每页10个。"

---

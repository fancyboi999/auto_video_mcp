[top](https://api.hifly.cc/hifly.html#lv-totop)

[中文](https://api.hifly.cc/hifly.html#) \| [English](https://api.hifly.cc/hifly_en.html)

# 飞影数字人 API V2

> 本文档适用于第三方系统接入飞影数字人的技术文档

## 通用

所有接口采用 **Bearer Token** 认证方式，需要在请求的 Header 中填入"Authorization":"Bearer ${token}"，token 可以在 [个人中心->API 明细](https://hifly.cc/setting) 获取。

在调用接口时，如果 token 验证失败，会返回 401 状态，其他业务异常时会返回 200 状态，需要通过响应体中的 [code 错误码](https://api.hifly.cc/hifly.html#%E9%94%99%E8%AF%AF%E7%A0%81) 来识别具体的异常原因。

## 接口列表

### 数字人克隆

#### 创建视频数字人

- 接口:

POST /api/v2/hifly/avatar/create\_by\_video

- 请求参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| title | string | 名称，默认"未命名" |
| video\_url | url string | 视频 URL 地址，与 file\_id 二选一必填，支持 mp4、mov 格式且使用 h264 编码，500MB 以内，分辨率范围 360p ～ 4K，时长范围 5 秒～ 30 分钟。注意：相同 URL 视为同一个数字人。 字符长度不超过 500 |
| file\_id | string | 文件 ID，与 video\_url 二选一必填 |

- 响应参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:


```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/avatar/create_by_video"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "我的数字人",
    "video_url": "https://example.com/my_video.mp4"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/avatar/create_by_video" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "我的数字人", "video_url": "https://example.com/my_video.mp4"}'

```

- 返回示例:

```json code-highlight
{
  "code": 0,
  "message": "",
  "task_id": "1234567890123456",
  "request_id": "req123456789"
}

```

#### 创建图片数字人

> **此接口会产生积分消耗。**

> **此接口为企业会员权益**

- 接口:

POST /api/v2/hifly/avatar/create\_by\_image

- 请求参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| title | string | 名称，默认"未命名" |
| image\_url | url string | 图片 URL 地址，与 file\_id 二选一必填 |
| file\_id | string | 文件 ID，与 image\_url 二选一必填 |
| model | int | 模型类型， 1:视频 2.0， 2:视频 2.1，默认 2 |

- 响应参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:


Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/avatar/create_by_image"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "我的图片数字人",
    "image_url": "https://example.com/my_image.jpg",
    "model": 2
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/avatar/create_by_image" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "我的图片数字人", "image_url": "https://example.com/my_image.jpg", "model": 2}'

```

- 返回示例:

```json code-highlight
{
  "code": 0,
  "message": "",
  "task_id": "1234567890123456",
  "request_id": "req123456789"
}

```

#### 查询任务状态

- 接口:

GET /api/v2/hifly/avatar/task

- 请求参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id ，必填 |

- 响应参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| status | int | 状态， 1:等待中2:处理中3:完成4:失败 |
| avatar | string | 数字人标识 |
| request\_id | string | 请求码 |

- 请求示例:


Python 示例:

```python code-highlight
import requests

task_id = "1234567890123456"
url = f"https://hfw-api.hifly.cc/api/v2/hifly/avatar/task?task_id={task_id}"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/avatar/task?task_id=1234567890123456" \
   -H "Authorization: Bearer YOUR_TOKEN"

```

- 返回示例:

```json code-highlight
{
  "code": 0,
  "message": "",
  "status": 3,
  "avatar": "av_abc123xyz",
  "request_id": "req123456789"
}

```

#### 查询公共数字人

> 查询公共数字人

- 接口地址

GET /api/v2/hifly/avatar/list

- 请求参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| page | int | 当前页，默认 1 |
| size | int | 每页数量，默认 20 |
| kind | int | 数字人分类，2:公共数字人，默认 2 |

- 响应参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| data | array | 数组 |
| `avatar` | string | 数字人标识 |
| `kind` | int | 数字人类型，2:公共数字人 |
| `title` | string | 数字人名称 |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/avatar/list"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
params = {
    "page": 1,
    "size": 10,
    "kind": 1
}

response = requests.get(url, headers=headers, params=params)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/avatar/list?page=1&size=10&kind=2" \
   -H "Authorization: Bearer YOUR_TOKEN"

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "data": [\
      {\
        "avatar": "avatar_abc123",\
        "kind": 2,\
        "title": "公共数字人1"\
      },\
      {\
        "avatar": "avatar_def456",\
        "kind": 2,\
        "title": "公共数字人2"\
      }\
    ],
    "request_id": "req123456789"
}


```


### 声音克隆

#### 创建声音

- 接口地址

POST /api/v2/hifly/voice/create

- 请求参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| title | string | 声音名称，必填，不超过 20 个字 |
| voice\_type | int | 声音类型，必填，8:声音克隆基础版 v2，目前只支持 8 |
| audio\_url | url string | 声音文件 URL，支持 mp3、m4a、wav 格式，20M 以内，时长范围 5 秒～ 3 分钟。和 file\_id 二选一必填 |
| file\_id | string | 音频文件 ID，和 audio\_url 二选一必填 |

- 响应参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/voice/create"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "我的声音",
    "voice_type": 8,
    "audio_url": "https://example.com/my_audio.mp3"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/voice/create" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "我的声音", "voice_type": 8, "audio_url": "https://example.com/my_audio.mp3"}'

```

- 返回示例:

```json code-highlight
{
  "code": 0,
  "message": "",
  "task_id": "1234567890123456",
  "request_id": "req123456789"
}

```

#### 修改声音的参数

- 接口地址

POST /api/v2/hifly/voice/edit

- 请求参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| voice | string | 声音标识，必填 |
| rate | string | 语速，必填，值为 0.5 和 2.0 之间，默认 1.0，字符串格式 |
| volume | string | 音量，必填，值为 0.1 和 2.0 之间，默认 1.0，字符串格式 |
| pitch | string | 语调，必填，值为 0.1 和 2.0 之间，默认 1.0，字符串格式 |

- 响应参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/voice/edit"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "voice": "voice_abc123",
    "rate": "1.2",
    "volume": "1.0",
    "pitch": "0.9"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/voice/edit" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"voice": "voice_abc123", "rate": "1.2", "volume": "1.0", "pitch": "0.9"}'

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "request_id": "req123456789"
}


```


#### 查询声音列表

> 查询已完成克隆的声音、以及公版声音

- 接口地址

GET /api/v2/hifly/voice/list

- 请求参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| page | int | 当前页，默认 1 |
| size | int | 每页数量，默认 20 |
| kind | int | 声音分类，1:自己克隆的，2:公共声音，默认 1 |

- 响应参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| data | array | 声音数组 |
| `voice` | string | 声音标识 |
| `type` | int | 声音类型，10:公版声音, 20:高保真声音, 8:基础版声音 V2 |
| `title` | string | 声音名称 |
| `rate` | string | 语速 |
| `volume` | string | 音量 |
| `pitch` | string | 语调 |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/voice/list"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
params = {
    "page": 1,
    "size": 10,
    "kind": 1
}

response = requests.get(url, headers=headers, params=params)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/voice/list?page=1&size=10&kind=1" \
   -H "Authorization: Bearer YOUR_TOKEN"

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "data": [\
      {\
        "voice": "voice_abc123",\
        "type": 20,\
        "title": "我的声音",\
        "rate": "1.0",\
        "volume": "1.0",\
        "pitch": "1.0"\
      },\
      {\
        "voice": "voice_def456",\
        "type": 10,\
        "title": "公共声音1",\
        "rate": "1.0",\
        "volume": "1.0",\
        "pitch": "1.0"\
      }\
    ],
    "request_id": "req123456789"
}


```


#### 查询任务状态

- 接口:

GET /api/v2/hifly/voice/task

- 请求参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id ，必填 |

- 响应参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| status | int | 状态， 1:等待中2:处理中3:完成4:失败 |
| voice | string | 声音标识 |
| demo\_url | url string | 试听声音文件地址 |
| request\_id | string | 请求码 |

- 请求示例:


Python 示例:

```python code-highlight
import requests

task_id = "1234567890123456"
url = f"https://hfw-api.hifly.cc/api/v2/hifly/voice/task?task_id={task_id}"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/voice/task?task_id=1234567890123456" \
   -H "Authorization: Bearer YOUR_TOKEN"

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "status": 3,
    "voice": "voice_abc123",
    "demo_url": "https://example.com/demo_audio.mp3",
    "request_id": "req123456789"
}


```


### 创作

#### 视频创作（声音驱动）

> **此接口会产生积分消耗。**
> 如果已经有音频文件，可以使用此接口快速创建视频。

- 接口:

POST /api/v2/hifly/video/create\_by\_audio

- 请求参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| audio\_url | url string | 音频文件地址，支持 mp3、m4a、wav 等格式，100M 以内，时长范围 5 秒 ～ 30 分钟。与 file\_id 二选一必填 |
| file\_id | string | 音频文件 ID。与 audio\_url 二选一必填 |
| avatar | string | 数字人标识，必填 |
| title | string | 作品名称，默认"未命名"，不超过 20 个字。 |

- 响应参数:

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/video/create_by_audio"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "音频驱动视频",
    "audio_url": "https://example.com/my_audio.mp3",
    "avatar": "av_abc123xyz",
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/video/create_by_audio" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "音频驱动视频", "audio_url": "https://example.com/my_audio.mp3", "avatar": "av_abc123xyz"}'

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "task_id": "1234567890123456",
    "request_id": "req123456789"
}


```


#### 视频创作（文本驱动）

> **此接口会产生积分消耗。**
> 如果没有音频文件，需要生成音频，可以使用此接口快速创建视频。

- 接口:

POST /api/v2/hifly/video/create\_by\_tts

- 请求参数:


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| voice | string | 声音标识，必填，参考 [创建声音](https://api.hifly.cc/hifly.html#voiceCreate) ,或通过 [声音列表](https://api.hifly.cc/hifly.html#voiceList) 获取声音 |
| text | string | 文本内容，必填，不超过 10000 字，不支持 html 标签 |
| avatar | string | 数字人标识 ，必填 |
| title | string | 作品名称，默认"未命名"，不超过 20 个字。 |
| st\_show | int | 是否显示字幕，1:显示，0:不显示，默认不显示 |
| st\_font\_name | string | 字体，如抖音美好体、荆南波波黑、Alimama FangYuanTi VF、云峰飞云体、三极泼墨体、快看世界体等，登陆飞影查看更多 |
| st\_font\_size | int | 字号，默认 100 |
| st\_primary\_color | string | 文字颜色，格式：#ff0000 |
| st\_outline\_color | string | 文字描边颜色，格式：#ff0000 |
| st\_width | int | 字幕区域宽度，默认 600 |
| st\_height | int | 字幕区域高度，默认 100 |
| st\_pos\_x | int | 字幕区域左上角的 X 坐标，默认 60 |
| st\_pos\_y | int | 字幕区域左上角的 Y 坐标，默认 900 |

[字幕使用说明](https://api.hifly.cc/subtitle.png)

- 响应参数:

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/video/create_by_tts"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "文本驱动视频",
    "text": "这是一段测试文本，用于生成数字人视频。",
    "voice": "voice_abc123",
    "avatar": "av_abc123xyz"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/video/create_by_tts" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "文本驱动视频", "text": "这是一段测试文本，用于生成数字人视频。", "voice": "voice_abc123", "avatar": "av_abc123xyz"}'

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "task_id": "1234567890123456",
    "request_id": "req123456789"
}


```


#### 音频创作

> **此接口会产生积分消耗。**
> 可以使用此接口快速创建音频。

- 接口:

POST /api/v2/hifly/audio/create\_by\_tts

- 请求参数:


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| voice | string | 声音标识，必填，参考 [创建声音](https://api.hifly.cc/hifly.html#voiceCreate) ,或通过 [声音列表](https://api.hifly.cc/hifly.html#voiceList) 获取声音 |
| text | string | 文本内容，必填，不超过 10000 字，不支持 html 标签 |
| title | string | 作品名称，默认"未命名"，不超过 20 个字。 |

- 响应参数:

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| task\_id | string | 任务 id |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/audio/create_by_tts"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "title": "音频创作",
    "text": "这是一段测试文本，用于生成音频。",
    "voice": "voice_abc123"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/audio/create_by_tts" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "音频创作", "text": "这是一段测试文本，用于生成音频。", "voice": "voice_abc123"}'

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "task_id": "1234567890123456",
    "request_id": "req123456789"
}


```


#### 查询创作任务状态

- 接口:

GET /api/v2/hifly/video/task

- 请求参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id，必填 |

- 响应参数:



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| status | int | 作品状态， 1:等待中2:处理中3:完成4:失败 |
| video\_Url | url string | 合成的视频地址。这是一个临时地址，请尽快转存。url 中会带有 query 参数，下载视频时请确保已兼容。 |
| duration | int | 作品时长，单位:秒 |
| request\_id | string | 请求码 |

- 请求示例:


Python 示例:

```python code-highlight
import requests

task_id = "1234567890123456"
url = f"https://hfw-api.hifly.cc/api/v2/hifly/video/task?task_id={task_id}"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/video/task?task_id=1234567890123456" \
   -H "Authorization: Bearer YOUR_TOKEN"

```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "status": 3,
    "video_Url": "https://example.com/videos/abc123.mp4?token=xyz789",
    "duration": 45,
    "request_id": "req123456789"
}


```


### 系统

#### 消息回调

任务完成后，会主动将消息推送到回调地址。默认只回调 **创作任务** 的消息，开启 V2 事件回调后，会回调 **数字人克隆** 及 **声音克隆** 的消息。

如果响应状态码不为 200，则视为通知失败， **5 分钟内会重试**，之后不再重试。

可以在 [个人中心](https://hifly.cc/setting) 设置回调地址及开启 V2 事件回调。

##### 数字人克隆任务

- 请求参数



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| type | int | 消息类型，2：数字人克隆 |
| status | int | 状态， 3:完成4:失败 |
| avatar | string | 数字人标识 |

- 返回示例:


```json code-highlight
{
    "task_id": "1234567890123456",
    "message": "",
    "code": 0,
    "type": 2,
    "status": 3,
    "avatar": "av_abc123xyz"
}


```


##### 声音克隆任务

- 请求参数



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| type | int | 消息类型，3：声音克隆 |
| status | int | 状态， 3:完成4:失败 |
| voice | string | 声音标识 |
| demo\_url | url string | 试听声音文件地址 |

- 返回示例:


```json code-highlight
{
    "task_id": "1234567890123456",
    "message": "",
    "code": 0,
    "type": 3,
    "status": 3,
    "voice": "voice_abc123",
    "demo_url": "https://example.com/demo_audio.mp3"
}


```


##### 创作任务

- 请求参数



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| task\_id | string | 任务 id |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| status | int | 作品状态，3:完成4:失败 |
| video\_Url | url string | 合成的视频地址。这是一个临时地址，请尽快转存。 url 中会带有 query 参数，下载视频时请确保已兼容。 |
| type | int | 消息类型，1：作品 |
| duration | int | 作品时长，单位:秒 |
| title | string | 作品名称 |

- 返回示例:


```json code-highlight
{
    "task_id": "1234567890123456",
    "status": 3,
    "video_Url": "https://example.com/videos/abc123.mp4?token=xyz789",
    "type": 1,
    "duration": 45,
    "message": "",
    "code": 0,
    "title": "我的视频创作"
}


```


#### 上传文件

> 先获取上传地址，然后再上传文件

##### 获取上传地址

- 接口:

POST /api/v2/hifly/tool/create\_upload\_url

- 请求参数



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| file\_extension | string | 后缀名，如 mp4、mp3 等，必填 |

- 响应参数



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| upload\_url | string | 上传地址 |
| content\_type | string | 文件 mime-type，在上传时需要设置 Content-Type |
| file\_id | string | 文件 ID |
| request\_id | string | 请求码 |

- 请求示例:


Python 示例:

```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/tool/create_upload_url"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
payload = {
    "file_extension": "mp4"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

```

cURL 示例:

```bash code-highlight
curl -X POST "https://hfw-api.hifly.cc/api/v2/hifly/tool/create_upload_url" \
   -H "Authorization: Bearer YOUR_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"file_extension": "mp4"}'

```

- 返回示例:


```json code-highlight
{
    "upload_url": "https://upload.hifly.cc/test%2Fa.mp4?Expires=1745576446&OSSAccessKeyId=LTAI5tPx2KRcdE3ihKTp5c36&Signature=rY86EuJEqzwYkOPnwOJDHPwP9Ew%3D",
    "content_type": "video/mp4",
    "file_id": "file_abc123xyz",
    "request_id": "req123456789"
}


```


##### 上传文件

- 说明
  - 使用 PUT 方式将文件上传到 upload\_url
  - 使用 binary 方式上传文件
  - 设置 请求头中的 Content-Type
- 示例


Python 示例:

```python code-highlight
import requests

# 假设我们已经从上一步获取了上传地址
upload_url = "https://upload.hifly.cc/test%2Fa.mp4?Expires=1745576446&OSSAccessKeyId=LTAI5tPx2KRcdE3ihKTp5c36&Signature=rY86EuJEqzwYkOPnwOJDHPwP9Ew%3D"
content_type = "video/mp4"
file_path = "/path/to/your/file.mp4"

with open(file_path, 'rb') as file:
    headers = {
        "Content-Type": content_type
    }
    response = requests.put(upload_url, headers=headers, data=file)
    print(f"状态码: {response.status_code}")

```

cURL 示例:

```bash code-highlight
curl -i -X PUT -T ./my_video.mp4 \
   -H 'Content-Type: video/mp4' \
   'https://upload.hifly.cc/test%2Fa.mp4?Expires=1745576446&OSSAccessKeyId=LTAI5tPx2KRcdE3ihKTp5c36&Signature=rY86EuJEqzwYkOPnwOJDHPwP9Ew%3D'

```

#### 查询账户积分

> 可以在 [个人中心](https://hifly.cc/setting) 设置积分预警提醒。

- 接口地址

GET /api/v2/hifly/account/credit

- 请求参数

无

- 响应参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| message | string | 失败时返回错误信息 |
| code | int | 失败时错误码 |
| left | int | 积分余额 |
| request\_id | string | 请求码 |

- 请求示例:

Python 示例:


```python code-highlight
import requests

url = "https://hfw-api.hifly.cc/api/v2/hifly/account/credit"
headers = {
      "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)
print(response.json())


```


cURL 示例:


```bash code-highlight
curl -X GET "https://hfw-api.hifly.cc/api/v2/hifly/account/credit" \
     -H "Authorization: Bearer YOUR_TOKEN"


```

- 返回示例:


```json code-highlight
{
    "code": 0,
    "message": "",
    "left": 10000,
    "request_id": "req123456789"
}


```


## 错误码

| 值 | 描述 |
| --- | --- |
| 11 | 参数不正确 |
| 14 | 找不到资源 |
| 1001 | 正在生成中的作品数量达到上限 |
| 1002 | 积分不足 |
| 1005 | 开通会员 |
| 1006 | 会员等级不够 |
| 1009 | 高保真声音已售罄 |
| 1011 | 声音与名人相似 |
| 1013 | 高保真声音达到克隆数量上限 |
| 1015 | 提交的作品数量达到上限 |
| 2003 | 无效 Token |
| 2011 | 文件大小超过限制 |
| 2012 | 文件类型不支持 |
| 2013 | 获取音频资源失败 |
| 2014 | 获取视频资源失败 |
| 2015 | 数字人克隆失败 |
| 2016 | 获取图片资源失败 |